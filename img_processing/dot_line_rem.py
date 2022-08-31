import util
import cv2

grayImage = cv2.imread("sc.jpeg", 0)

h = float(grayImage.shape[0])

maxVal = 255
blockSize = 15
C = 12.0*(90.0/h)

print("C:" + str(C))

showImages = []

bw = cv2.adaptiveThreshold(grayImage, maxVal, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, C)
bw = ~bw

showImages.append(grayImage.copy())
showImages.append(bw.copy())

vertical = bw.copy()

# Specify size on vertical axis
# verticalsize = vertical.shape[0] / 20
verticalsize = 4

# Create structure element for extracting vertical lines through morphology operations
verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, verticalsize))

# Apply morphology operations
vertical = cv2.erode(vertical, verticalStructure, None, (-1,-1))
showImages.append(vertical.copy())

vertical = cv2.dilate(vertical, verticalStructure, None, (-1,-1))
showImages.append(vertical.copy())

util.showOpenCVImagesGrid(showImages, 2, 2, titles=["grayImage", "adaptiveThreshold", "after erode", "after dilate"])

