import cv2
from matplotlib import pyplot as plt
import numpy as np

image_file="/home/ashok/PycharmProjects/CodingManiac/pro/syn.jpg"
img=cv2.imread(image_file)

def display(im_path):
    dpi=80
    im_data=plt.imread(im_path)
    height,width,depth=im_data.shape
    figsize=width/float(dpi),height/float(dpi)
    fig=plt.figure(figsize=figsize)
    ax=fig.add_axes([0,0,1,1,])
    ax.axis('off')
    ax.imshow(im_data,cmap='gray')
    plt.show()
# display(image_file)
def inverted_img(img):
    inv_img=cv2.bitwise_not(img)
    cv2.imwrite("/home/ashok/PycharmProjects/CodingManiac/pro/inverted.jpg",inv_img)
    # display("/home/ashok/PycharmProjects/CodingManiac/pro/inverted.jpg")
# inverted_img(img)

def greyscale(image):
    return cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gre_=greyscale(img)
# cv2.imwrite("/home/ashok/PycharmProjects/CodingManiac/pro/greys.jpg",gre_)
# display("/home/ashok/PycharmProjects/CodingManiac/pro/greys.jpg")
thresh,im_bw=cv2.threshold(gre_, 210,300,cv2.THRESH_BINARY)
cv2.imwrite("/home/ashok/PycharmProjects/CodingManiac/pro/image_bw.jpg",im_bw)
# display("/home/ashok/PycharmProjects/CodingManiac/pro/image_bw.jpg")

def noise_remo(image):
    kernel=np.ones((1,1),np.uint8)
    image=cv2.dilate(image,kernel,iterations=1)
    kernel=np.ones((1,1),np.uint8)
    image=cv2.erode(image,kernel,iterations=1)
    image=cv2.morphologyEx(image,cv2.MORPH_CLOSE,kernel)
    image=cv2.medianBlur(image,3)
    return (image)
no_noise=noise_remo(im_bw)
cv2.imwrite("/home/ashok/PycharmProjects/CodingManiac/pro/no_noise_img.jpg",no_noise)
# display("/home/ashok/PycharmProjects/CodingManiac/pro/no_noise_img.jpg")
def thin_font(image):
    image=cv2.bitwise_not(image)
    kernel=np.ones((2,2),np.uint8)
    image=cv2.erode(image,kernel,iterations=1)
    image=cv2.bitwise_not(image)
    return (image)
# eroded_image=thin_font(no_noise)
# cv2.imwrite("/home/ashok/PycharmProjects/CodingManiac/pro/thin_font_img.jpg",eroded_image)
# display("/home/ashok/PycharmProjects/CodingManiac/pro/thin_font_img.jpg")

def thick_font(image):
    image=cv2.bitwise_not(image)
    kernel=np.ones((2,2),np.uint8)
    image=cv2.dilate(image,kernel,iterations=1)
    image=cv2.bitwise_not(image)
    return (image)
# dialted=thick_font(no_noise)
# cv2.imwrite("/home/ashok/PycharmProjects/CodingManiac/pro/dilated.jpg",dialted)

def deskewing(cvImage) -> float :
    newImage=cvImage.copy()
    gray=cv2.cvtColor(newImage,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(9,9),0)
    thresh=cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]
    kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(30,5))
    dilate=cv2.dilate(thresh,kernel,iterations=2)

    contours,hierarchy=cv2.findContours(dilate,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours,key=cv2.contourArea,reverse=True)
    for c in contours:
        rect=cv2.boundingRect(c)
        x,y,w,h=rect
        cv2.rectangle(newImage,(x,y),(x+w,y+h),(0,255,0),2)

    largestContour=contours[0]
    print(len(contours))
    minAreaRect=cv2.minAreaRect(largestContour)
    cv2.imwrite("/home/ashok/PycharmProjects/CodingManiac/pro/boxes.jpg",newImage)
    angle=minAreaRect[-1]
    if angle < -45:
        angle=90+angle
    return -1.0*angle
def rotateImage(cvImage,angle:float):
    newImage=cvImage.copy()
    (h,w)=newImage.shape[:2]
    center=(w//2,h//2)
    M=cv2.getRotationMatrix2D(center,angle,1.0)
    newImage=cv2.warpAffine(newImage,M,(w,h),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REPLICATE)
    return newImage
def deskew(cvImage):
    angle=deskewing(cvImage)
    return rotateImage(cvImage,-1.0*angle)
# fixed=deskew(img)
# cv2.imwrite("/home/ashok/PycharmProjects/CodingManiac/pro/fix_image.jpg",fixed)

def rem_bord(image):
    contours,hierarchy=cv2.findContours(image,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cntsSorted=sorted(contours,key=lambda x:cv2.contourArea(x))
    cnt=cntsSorted[-1]
    x,y,w,h=cv2.boundingRect(cnt)
    crop=image[y:y+h,x:x+w]
    return (crop)

# no_border=rem_bord(no_noise)
# cv2.imwrite("/home/ashok/PycharmProjects/CodingManiac/pro/no_border_image.jpg", no_border)




