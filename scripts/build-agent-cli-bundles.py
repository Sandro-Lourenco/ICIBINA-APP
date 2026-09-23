#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import io
import json
import shutil
import urllib.request
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / "external-skills-lock.json"
LOCAL_SKILLS = ROOT / ".agents" / "skills"
LOCAL_RULES = ROOT / ".agents" / "rules"
CODEX_PLUGIN = ROOT / "plugins" / "codex" / "icibina-engineering"
AGY_STAGING_PLUGIN = ROOT / "plugins" / "antigravity" / "icibina-engineering"
AGY_WORKSPACE_PLUGIN = ROOT / ".agents" / "plugins" / "icibina-engineering"
MARKETPLACE = ROOT / ".agents" / "plugins" / "marketplace.json"
BUILD_MANIFEST = ROOT / ".agents" / "cli-bundle-build.json"

parser = argparse.ArgumentParser(description="Build reviewed ICIBINA skill bundles for Codex CLI and Antigravity 2.0 CLI")
parser.add_argument("--include-manual", action="store_true")
parser.add_argument("--include-motion-plus", action="store_true", help="opt-in Motion+ MCP; default plugin includes only the public Motion MCP")
args = parser.parse_args()


def tree_hash(root: Path) -> str:
    h = hashlib.sha256()
    for f in sorted(x for x in root.rglob("*") if x.is_file()):
        rel = f.relative_to(root).as_posix().encode()
        h.update(len(rel).to_bytes(4, "big"))
        h.update(rel)
        b = f.read_bytes()
        h.update(len(b).to_bytes(8, "big"))
        h.update(b)
    return h.hexdigest()


def copytree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)


def clean_plugin(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    (path / "skills").mkdir(parents=True)


def download_repo_zip(repo: str, ref: str, cache: dict[tuple[str, str], bytes]) -> bytes:
    key = (repo, ref)
    if key not in cache:
        url = f"https://codeload.github.com/{repo}/zip/{ref}"
        print(f"download {repo}@{ref}")
        with urllib.request.urlopen(url, timeout=90) as r:
            cache[key] = r.read()
    return cache[key]


def extract_skill(item: dict, target: Path, cache: dict[tuple[str, str], bytes]) -> None:
    data = download_repo_zip(item["repo"], item["ref"], cache)
    z = zipfile.ZipFile(io.BytesIO(data))
    root_prefix = z.namelist()[0].split("/")[0]
    src = item["source_path"].strip("./")
    prefix = f"{root_prefix}/{src}/" if src else f"{root_prefix}/"
    members = [n for n in z.namelist() if n.startswith(prefix) and not n.endswith("/")]
    if not members:
        raise SystemExit(f"source_path not found: {item['repo']} {item['source_path']}")
    target.mkdir(parents=True, exist_ok=True)
    for n in members:
        rel = Path(n[len(prefix):])
        out = target / rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_bytes(z.read(n))
    if not (target / "SKILL.md").exists():
        raise SystemExit(f"SKILL.md missing after extraction: {target}")


lock = json.loads(LOCK.read_text(encoding="utf-8"))
clean_plugin(CODEX_PLUGIN)
clean_plugin(AGY_STAGING_PLUGIN)

# Local project orchestrators are source-controlled and bundled into both agents.
local_names = []
for skill_dir in sorted(LOCAL_SKILLS.iterdir()):
    if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
        local_names.append(skill_dir.name)
        copytree(skill_dir, CODEX_PLUGIN / "skills" / skill_dir.name)
        copytree(skill_dir, AGY_STAGING_PLUGIN / "skills" / skill_dir.name)

cache: dict[tuple[str, str], bytes] = {}
external_records = []
for item in lock["sources"]:
    if item.get("redistribution", "allowed") == "blocked" or item.get("mode") == "reference-only":
        print(f"skip redistribution-blocked/reference-only skill: {item['target_name']}")
        continue
    if item["mode"] == "manual" and not args.include_manual:
        continue
    name = item["target_name"]
    for plugin in (CODEX_PLUGIN, AGY_STAGING_PLUGIN):
        extract_skill(item, plugin / "skills" / name, cache)
    external_records.append({
        "name": item["name"], "repo": item["repo"], "ref": item["ref"],
        "target_name": name, "mode": item["mode"], "license": item["license"],
        "tree_sha256": tree_hash(CODEX_PLUGIN / "skills" / name),
    })

# Codex portable Agent Plugin. Skills are auto-discovered from skills/.
(CODEX_PLUGIN / "plugin.json").write_text(json.dumps({
    "$schema": "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
    "name": "icibina-engineering",
    "version": "5.8.0",
    "description": "ICIBINA senior engineering skills for frontend, backend, database, QA, security, observability, payments and architecture.",
    "keywords": ["icibina", "react", "fastapi", "postgresql", "qa", "security"],
    "extensions": {
        "com.openai": {
            "interface": {
                "displayName": "ICIBINA Engineering",
                "shortDescription": "Senior engineering workflows and reviewed specialist skills for ICIBINA."
            }
        }
    }
}, indent=2) + "\n", encoding="utf-8")
codex_mcps={"motion": {"type": "http", "url": "https://mcp.motion.dev"}}
if args.include_motion_plus:
    codex_mcps["motion-plus"]={"type":"http","url":"https://mcp.motion.dev/plus"}
(CODEX_PLUGIN / "mcp.json").write_text(json.dumps({"mcpServers":codex_mcps}, indent=2) + "\n", encoding="utf-8")

# Antigravity 2.0 / CLI plugin. Rules and remote MCP use Antigravity's native schema.
(AGY_STAGING_PLUGIN / "plugin.json").write_text(json.dumps({
    "name": "icibina-engineering",
    "version": "5.8.0",
    "description": "ICIBINA senior engineering skills, rules and Motion MCP integration."
}, indent=2) + "\n", encoding="utf-8")
if LOCAL_RULES.exists():
    copytree(LOCAL_RULES, AGY_STAGING_PLUGIN / "rules")
agy_mcps={"motion": {"serverUrl": "https://mcp.motion.dev"}}
if args.include_motion_plus:
    agy_mcps["motion-plus"]={"serverUrl":"https://mcp.motion.dev/plus"}
(AGY_STAGING_PLUGIN / "mcp_config.json").write_text(json.dumps({"mcpServers":agy_mcps}, indent=2) + "\n", encoding="utf-8")

# Antigravity workspace activation happens only after native CLI validation in install-antigravity-workspace-plugin.py.

MARKETPLACE.parent.mkdir(parents=True, exist_ok=True)
MARKETPLACE.write_text(json.dumps({
    "name": "icibina-local",
    "interface": {"displayName": "ICIBINA Local Engineering"},
    "plugins": [{
        "name": "icibina-engineering",
        "source": {"source": "local", "path": "./plugins/codex/icibina-engineering"},
        "policy": {"installation": "INSTALLED_BY_DEFAULT", "authentication": "ON_INSTALL"},
        "category": "Developer Tools"
    }]
}, indent=2) + "\n", encoding="utf-8")

BUILD_MANIFEST.write_text(json.dumps({
    "schema_version": 1,
    "bundle_version": "5.8.0",
    "local_skills": local_names,
    "external_skills": external_records,
    "codex_plugin": str(CODEX_PLUGIN.relative_to(ROOT)),
    "antigravity_staging_plugin": str(AGY_STAGING_PLUGIN.relative_to(ROOT)),
    "antigravity_workspace_plugin": str(AGY_WORKSPACE_PLUGIN.relative_to(ROOT)),
    "codex_tree_sha256": tree_hash(CODEX_PLUGIN),
    "antigravity_tree_sha256": tree_hash(AGY_STAGING_PLUGIN),
    "motion_plus_enabled": args.include_motion_plus,
}, indent=2) + "\n", encoding="utf-8")

print(f"built Codex plugin: {CODEX_PLUGIN.relative_to(ROOT)}")
print(f"built Antigravity staging plugin: {AGY_STAGING_PLUGIN.relative_to(ROOT)}")
print(f"external reviewed skills bundled: {len(external_records)}")
