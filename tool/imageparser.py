#!/usr/bin/env python3

import os
import os.path as path
from PIL import Image

imagelist=[]
for root, dirs, files in os.walk("gfx"):
    for file in files:
        fdir = path.join(root,file)
        if path.splitext(fdir)[-1] == ".png":
            imagelist.append(fdir)           

for image in imagelist:
    readname = path.splitext(image)[0]
    writename = readname+"-32bpp.png"

    with Image.open(image) as im:
        if im.mode == "P":
            xsize,ysize = im.size
            outim = im.convert("RGBA")
            for x in range(xsize):
                for y in range (ysize):
                    if im.getpixel((x,y)) == 0:
                        outim.putpixel((x,y),(0,0,255,0))
            outim.save(writename)