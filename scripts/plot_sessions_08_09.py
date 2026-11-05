#!/usr/bin/env python3
"""Rebuild the source example's lightweight, offline SVG diagram.

No third-party plotting dependency. Intended as a reproducible study visual,
not a screenshot of the handwritten lecture or a claim of instructor authorship.
"""
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]


def coord(z,y):
    return f'{80+(z-1)*72:.1f},{340-y*260:.1f}'

m=' '.join(coord(z,y) for z,y in [(2,0),(5,1),(12,0)])
n=' '.join(coord(z,y) for z,y in [(2,0),(4,1),(10,0)])
cx,cy=80+(14/3-1)*72,340-(8/9)*260

svg='''<svg xmlns="http://www.w3.org/2000/svg" width="960" height="415" viewBox="0 0 960 415" role="img" aria-labelledby="title desc">
<title id="title">Two triangular fuzzy numbers and the exact crossing</title>
<desc id="desc">M has vertices (2,0),(5,1),(12,0). N has vertices (2,0),(4,1),(10,0). Their nonzero interior crossing is z equal to fourteen thirds, membership eight ninths.</desc>
<rect width="960" height="415" fill="#fff"/>
<line x1="100" y1="340" x2="930" y2="340" stroke="#64748b" stroke-width="2"/>
<line x1="110" y1="355" x2="110" y2="55" stroke="#64748b" stroke-width="2"/>
<line x1="103" y1="80" x2="915" y2="80" stroke="#e5e7eb" stroke-dasharray="4 5"/>
<text x="79" y="85" text-anchor="end" fill="#334155" font-family="sans-serif" font-size="18">1</text>
<text x="80" y="360" text-anchor="end" fill="#334155" font-family="sans-serif" font-size="18">0</text>
<text x="920" y="372" text-anchor="end" fill="#334155" font-family="sans-serif" font-size="18">z</text>
<polyline points="'''+m+'''" stroke="#1769aa" fill="none" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<polyline points="'''+n+'''" stroke="#ca6c21" fill="none" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="'''+f'{cx:.1f}'+'''" cy="'''+f'{cy:.1f}'+'''" r="6" fill="#111827" stroke="#fff" stroke-width="2"/>
<line x1="'''+f'{cx:.1f}'+'''" y1="'''+f'{cy+10:.1f}'+'''" x2="'''+f'{cx:.1f}'+'''" y2="340" stroke="#475569" stroke-dasharray="5 5"/>
<text x="'''+f'{cx+25:.1f}'+'''" y="'''+f'{cy-20:.1f}'+'''" fill="#111827" font-family="sans-serif" font-size="18">(14/3, 8/9)</text>
<text x="440" y="49" fill="#1769aa" font-family="sans-serif" font-size="21" font-weight="bold">M = (2, 5, 12)</text>
<text x="680" y="49" fill="#ca6c21" font-family="sans-serif" font-size="21" font-weight="bold">N = (2, 4, 10)</text>
'''
for value in [2,4,5,10,12]:
    x=80+(value-1)*72
    svg+=f'<line x1="{x:.1f}" y1="340" x2="{x:.1f}" y2="348" stroke="#64748b"/><text x="{x:.1f}" y="370" text-anchor="middle" font-family="sans-serif" font-size="18" fill="#334155">{value}</text>\n'
svg+='</svg>\n'
for suffix in ('.svg','.fa.svg'):
    target=ROOT/'site_docs/assets'/('session09_pair'+suffix)
    target.parent.mkdir(parents=True,exist_ok=True)
    target.write_text(svg,encoding='utf-8')
    print('Wrote',target)
