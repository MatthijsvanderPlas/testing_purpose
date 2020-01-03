from PIL import Image
import sys
import os


def convert():
    Path = sys.argv[1]
    if os.path.exists(sys.argv[2] ):
        pass
    else:
        os.mkdir(f".\{sys.argv[2]}")

    filelist = os.listdir(Path)
    for x in filelist:
        if x.endswith(".jpg"):
            im = Image.open(Path + x)
            tmp = x.split(".")
            im.save(sys.argv[2] + tmp[0]+".png", "png")


if __name__ == '__main__':
    convert()
