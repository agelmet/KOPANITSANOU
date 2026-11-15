import os
from PIL import Image, ImageFilter, ImageEnhance
M='/home/claude/mat'; O='/home/claude/kop/site/assets/img'
P='akrivi-kopanitsanou-'
def save(im,name,w=None,q=82):
    im=im.convert('RGB')
    if w and im.width>w: im=im.resize((w,round(im.height*w/im.width)),Image.LANCZOS)
    im.save(f'{O}/{P}{name}.webp','WEBP',quality=q,method=6); return im.size
def up(im,f=1.5):
    im=im.resize((round(im.width*f),round(im.height*f)),Image.LANCZOS)
    return im.filter(ImageFilter.UnsharpMask(radius=1.2,percent=60,threshold=2))
sizes={}
p1=Image.open(f'{M}/portrait1.png').convert('RGB')
p1=p1.filter(ImageFilter.UnsharpMask(radius=1,percent=40,threshold=2))
sizes['hero-900']=save(p1,'eikastiki-psychotherapeftria-neo-psychiko-portreto-900',900,84)
sizes['hero-640']=save(p1,'eikastiki-psychotherapeftria-neo-psychiko-portreto-640',640,82)
p2=Image.open(f'{M}/portrait2.png').convert('RGB')
sizes['icps']=save(up(p2,1.4),'icps-msc-eikastikis-psychotherapeias',700,82)
names={'p01':'evropaiko-pistopoiitiko-psychotherapeias-ecp','p02':'atelie-polythrona-fotistiko','p03':'atelie-pinakes-kyma-galini',
'p04':'grafeio-neo-psychiko-fos','p05':'atelie-niki-samothrakis','p06':'atelie-xylines-figoures','p07':'atelie-kavaletto-parathyro',
'p08':'atelie-vivlia','p09':'atelie-chromata-pinelia','p10':'atelie-eikastikis-psychotherapeias-neo-psychiko','p11':'atelie-grafeio'}
for k,v in names.items():
    im=Image.open(f'{M}/{k}.jpg'); im=up(im,1.5)
    sizes[k]=save(im,v,1200,80)
    sizes[k+'s']=save(im,v+'-600',600,78)
import json; print(json.dumps(sizes))
# og image
og=Image.new('RGB',(1200,630),(19,50,40))
ph=p1.copy(); ph=ph.resize((500,round(500*ph.height/ph.width)),Image.LANCZOS); og.paste(ph.crop((0,40,500,670)),(700,0))
og.save('/home/claude/kop/site/assets/img/og.jpg',quality=86)
