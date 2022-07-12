#颜色反转
#直接使用 ImageChops 中定义的反转函数进行图像颜色反转
#pip install pillow（需求库）

from PIL import Image, ImageChops

def invert_color(fname):
    img = Image.open(fname)
    img_inverted = ImageChops.invert(img)
    img_inverted.save(fname.replace('.', '_inverted.'))
    return img_inverted
    
if __name__ == '__main__':
    invert_color('1.jpg')
