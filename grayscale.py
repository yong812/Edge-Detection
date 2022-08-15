from ctypes import resize
from multiprocessing.spawn import import_main_path
from os import path
from PIL import Image
import numpy as np
import cv2



#img.convert('L') 灰度图像，每个像素用8个bit表示，0表示黑色，255表示白色，其他颜色表示不同的灰度；
# 转换公式：L=R*299/1000+G*587/1000+B*114/1000
# # 通过PIL.Image类的resize方法对图片进行缩放

#将图像resize
# def resize_I():
#     img = Image.open(path,"r")
#     print("原来的图片大小： " + str(np.array(img).shape))
#     img1 = img.resize((128, 128))  # resize
#     print("缩放后的图片大小：" + str(np.array(img1).shape))
#     # img.show()
#     img1.show()
#     # return img1

# # 将图像灰度化
# def convert_L():
#     path = "C:/Users/qqqc/Desktop/gs/1.jpg"
#     img1 = Image.open(path,"r")
#     image_L = img1.convert('L')
#     # image.show()
#     image_L.show()
#     # return image_L

# if __name__=="__main__":
#     resize_I()
#     # convert_L()




if __name__=="__main__":
    path = "./gs/1.jpg"
    img = Image.open(path, "r")
    print("original image size: " + str(np.array(img).shape))
    img1 = img.resize((128, 128))  # resize
    print("resize image size:" + str(np.array(img1).shape))
    # img.show()# show original image
    # img1.show()#show resize image

    image_L = img1.convert('L')# grayscale resize image
    image_L1 = img.convert('L')# grayscale original image
    # image_L1.show()
    # image_L.show()
    # print(image_L)
    image_L.save("./gs/gray_1.jpg")
