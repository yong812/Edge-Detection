#颜色反转


from PIL import Image, ImageChops

def invert_color(fname):
    im = Image.open(fname)
    im_inverted = ImageChops.invert(im)
    im_inverted.save(fname.replace('.', '_inverted.'))
    return im_inverted
    
if __name__ == '__main__':
    invert_color('test.jpg')