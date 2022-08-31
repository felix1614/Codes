import cv2
import pytesseract
from pytesseract import Output

img=cv2.imread("/home/ashok/PycharmProjects/CodingManiac/pro/sc.jpeg")
from PIL import Image

# img=Image.open("price.jpg")
# cust_conf=r'--oem 3 --psm 6'
# d=pytesseract.image_to_data(img,output_type=Output.DICT)
# keys=list(d.keys())
# pattern='DOLOR SIT'
# n_boxes=len(d['text'])
# for i in range(n_boxes):
#     if int(d['conf'][i])>60:
#         (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
#         img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#
# cv2.imshow('img', img)
# cv2.waitKey(0)~
# print(c)
# def grayscale_(path):
#     return cv2.cvtColor(path,cv2.COLOR_BGR2GRAY)
# d=grayscale_(img)
# cust_conf=r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6'
# cust_conf=r'-c tessedit_char_whitelist=abcdefghijklmnopqrstuvwxyz --psm 6'
config=('-| eng --oem 1 --psm 3')
c=pytesseract.image_to_string(img,config=config)
# with open("/home/ashok/PycharmProjects/CodingManiac/pro/test.txt","a") as t:
#     t.write("\n".join([i for i in c.split("\n") if "sarah" in i]))
# t.close()
# d={"item":i for i in c.split("\n") if "sarah" in i}
print(c)



