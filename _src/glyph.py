from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
import sys,json
f=TTFont(sys.argv[1]); gs=f.getGlyphSet(); cmap=f.getBestCmap()
out={}
for ch in sys.argv[2]:
    g=cmap[ord(ch)]; p=SVGPathPen(gs); gs[g].draw(p); b=BoundsPen(gs); gs[g].draw(b)
    out[ch]={'d':p.getCommands(),'b':b.bounds,'upm':f['head'].unitsPerEm}
print(json.dumps(out))
