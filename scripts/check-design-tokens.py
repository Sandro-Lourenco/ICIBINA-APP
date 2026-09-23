#!/usr/bin/env python3
from pathlib import Path
import json,sys
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'design-system/integrative-medicine/tokens.json').read_text(encoding='utf-8'))

def rgb(h):
 h=h.lstrip('#'); return [int(h[i:i+2],16)/255 for i in (0,2,4)]
def linear(c): return c/12.92 if c<=.04045 else ((c+.055)/1.055)**2.4
def lum(h):
 r,g,b=map(linear,rgb(h)); return .2126*r+.7152*g+.0722*b
def ratio(a,b):
 x,y=lum(a),lum(b); hi,lo=max(x,y),min(x,y); return (hi+.05)/(lo+.05)
def colors(theme): return {k:v['$value'] for k,v in data['themes'][theme]['color'].items()}

checks={
 'light':[
  ('foreground','background',4.5),('mutedForeground','surface',4.5),('primary','surface',4.5),
  ('danger','surface',4.5),('warning','surface',4.5),('info','surface',4.5),('success','surface',4.5),
 ],
 'dark':[
  ('foreground','background',4.5),('mutedForeground','surface',4.5),('primary','surface',4.5),
  ('danger','surface',4.5),('warning','surface',4.5),('info','surface',4.5),('success','surface',4.5),
  ('focus','surface',3.0),('border','surface',3.0),
 ],
 'studentImmersive':[
  ('foreground','background',4.5),('mutedForeground','surface',4.5),('primary','surface',4.5),
  ('accent','surface',4.5),('danger','surface',4.5),('warning','surface',4.5),('info','surface',4.5),('success','surface',4.5),
  ('focus','surface',3.0),('border','surface',3.0),
 ]
}
failed=[]
for theme,pairs in checks.items():
 c=colors(theme)
 print(f'[{theme}]')
 for a,b,minr in pairs:
  r=ratio(c[a],c[b]); print(f'{a}/{b}: {r:.2f}:1 (min {minr})')
  if r<minr: failed.append((theme,a,b,r,minr))
if failed:
 for row in failed: print('FAIL',row)
 sys.exit(1)
print('design-token-contrast: OK (light + dark + studentImmersive)')
