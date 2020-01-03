from PIL import Image
import sys
import os

pathfile = sys.argv[1]
outputpath = sys.argv[2]


def convert():
    if not os.path.exists(outputpath):
        os.mkdir(f".\{outputpath}")

    filelist = os.listdir(pathfile)
    for x in filelist:
        if x.endswith(".jpg"):
            im = Image.open(pathfile + x)
            tmp = os.path.splitext(x)
            im.save(outputpath + tmp[0] + ".png", "png")


if __name__ == '__main__':
    convert()
