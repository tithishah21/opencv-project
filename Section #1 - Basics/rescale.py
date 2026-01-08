import cv2 as cv
img = cv.imread('../Resources/Photos/cat_large.jpg')
cv.imshow('Cat', img)
def rescaleFrame(frame, scale=0.75):
    width = int( frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dim = (width, height)
    return cv.resize(frame, dim, interpolation=cv.INTER_AREA)
cv.waitKey(0)
