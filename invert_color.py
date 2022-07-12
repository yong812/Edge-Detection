#颜色反转


from PIL import Image, ImageChops

def invert_color(fname):
    img = Image.open(fname)
    img_inverted = ImageChops.invert(img)
    img_inverted.save(fname.replace('.', '_inverted.'))
    return img_inverted
    
if __name__ == '__main__':
    invert_color('1.jpg')
