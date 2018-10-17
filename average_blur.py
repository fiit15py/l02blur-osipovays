from PIL import Image
from math import pi, log, exp
import numpy as np

img = Image.open('darwin.png')
img.load()

print("Image size is", img.size)
print("Image mode is", img.mode)

print("getdata[1]=", img.getdata()[1])
a = np.array(img, dtype=np.uint8).reshape(img.size[::-1])
print("a[0,1]=", a[0,1])

b = a[900:1150, 900:1100]
pic = Image.fromarray(b)

def average_blur(img, r):
    w, h = img.size
    a = np.array(img.getdata(), dtype=np.uint8).reshape(h, w)
    b = np.zeros((h,w), dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            s = 0
            up, bt = max(i-r,0), min(i+r+1,h)
            lf, rt = max(j-r,0), min(j+r+1,w)
            n = (bt-up)*(rt-lf)
            for y in range(up,bt):
                for x in range(lf,rt):
                    s += a[y,x]
            b[i,j] = s / n

    return Image.fromarray(b)

average_blur(Image.fromarray(b),5)