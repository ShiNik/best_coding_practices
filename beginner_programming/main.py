import cv2
import matplotlib.pyplot as plt
import numpy as np

def convolve(image, kernel):
    (iH, iW) = image.shape[:2]
    (kH, kW) = kernel.shape[:2]

    pad = (kW - 1) // 2
    image = cv2.copyMakeBorder(image, pad, pad, pad, pad,
                               cv2.BORDER_REPLICATE)
    output = np.zeros((iH, iW), dtype= np.int64)

    for y in np.arange(pad, iH + pad):
        for x in np.arange(pad, iW + pad):
            output[y - pad, x - pad] = (image[y - pad:y + pad + 1, x - pad:x + pad + 1] * kernel).sum()
    return output

image_path = "D:\\ImageManipulation\\beginner_programming\\images\\Color_Image_convlution.jpg"
image = cv2.imread(image_path)
# let img1 be an image with no features
laplacian = np.array((
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]), dtype="int")

# construct the Sobel x-axis kernel
sobelX = np.array((
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]), dtype="int")

# construct the Sobel y-axis kernel
sobelY = np.array((
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]), dtype="int")


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#opencv edge
laplacian_image = cv2.Laplacian(gray,cv2.CV_64F)
sobelx_image = cv2.Sobel(gray,cv2.CV_64F,1,0,ksize=3)
sobely_image = cv2.Sobel(gray,cv2.CV_64F,0,1,ksize=3)

conv_x = convolve(gray, sobelX)
#post processing on conv_x
print("max: ", np.max(conv_x),", min: ", np.min(conv_x))
# conv_x = np.absolute(conv_x)
max = np.max(conv_x)
min = np.min(conv_x)
# Normalize (scaling the gray level to range on using int)
conv_x = (conv_x - min) *255 / (max-min)
conv_x = conv_x.astype(np.uint8)
print("max: ", np.max(conv_x),", min: ", np.min(conv_x))
treshold_edge = 0
conv_x[conv_x<treshold_edge]=0

conv_y = convolve(gray, sobelY)
#post processing on conv_y
print("max: ", np.max(conv_y),", min: ", np.min(conv_y))
# conv_y = np.absolute(conv_y)
max = np.max(conv_y)
min = np.min(conv_y)
# Normalize (scaling the gray level to range on using int)
conv_y = (conv_y - min) *255 / (max-min)
conv_y = conv_y.astype(np.uint8)
print("max: ", np.max(conv_y),", min: ", np.min(conv_y))
treshold_edge = 0
conv_y[conv_y<treshold_edge]=0

conv_laplacian = convolve(gray, laplacian)
#post processing on conv_laplacian
print("max: ", np.max(conv_laplacian),", min: ", np.min(conv_laplacian))
# conv_laplacian = np.absolute(conv_laplacian)
max = np.max(conv_laplacian)
min = np.min(conv_laplacian)
# Normalize (scaling the gray level to range on using int)
conv_laplacian = (conv_laplacian - min) *255 / (max-min)
conv_laplacian = conv_laplacian.astype(np.uint8)
print("max: ", np.max(conv_laplacian),", min: ", np.min(conv_laplacian))
treshold_edge = 0
conv_laplacian[conv_laplacian<treshold_edge]=0

#merger X and Y
conv_x_y = conv_x.copy()
conv_x_y = conv_x.__add__(conv_y)

cv2.imwrite('D:\\ImageManipulation\\beginner_programming\\images\\conv_gray_Image.jpg', gray)
cv2.imwrite('D:\\ImageManipulation\\beginner_programming\\images\\conv_x.jpg', conv_x)
cv2.imwrite('D:\\ImageManipulation\\beginner_programming\\images\\conv_y.jpg', conv_y)
cv2.imwrite('D:\\ImageManipulation\\beginner_programming\\images\\conv_x_y.jpg', conv_x_y)
cv2.imwrite('D:\\ImageManipulation\\beginner_programming\\images\\conv_laplacian.jpg', conv_laplacian)

fig, axarr = plt.subplots(3,2,figsize=(100, 100))
fig.suptitle("Convlution", fontsize=16)
axarr[0,0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axarr[0,0].title.set_text('Original image')
axarr[0,1].imshow(gray, cmap=plt.get_cmap('gray'))
axarr[0,1].title.set_text('grayscale image')
axarr[1,0].imshow(conv_x, cmap=plt.get_cmap('gray'))
axarr[1,0].title.set_text('sobelX')
axarr[1,1].imshow(conv_y, cmap=plt.get_cmap('gray'))
axarr[1,1].title.set_text('sobelY')
axarr[2,0].imshow(conv_x_y, cmap=plt.get_cmap('gray'))
axarr[2,0].title.set_text('conv_x_y')
axarr[2,1].imshow(conv_laplacian, cmap=plt.get_cmap('gray'))
axarr[2,1].title.set_text('laplacian')
plt.show()

#read image
#When you use opencv (imread, VideoCapture), the images are loaded in the BGR color space.
image_path = "D:\\ImageManipulation\\beginner_programming\\images\\Color_Image.jpg"
image = cv2.imread(image_path)

print(image.shape)
print(type(image.shape))
print("image width: ",image.shape[1])
print("image height: ",image.shape[0])

#extract red channel
blue_channel = image[:,:,0]
green_channel = image[:,:,1]
red_channel = image[:,:,2]

fig, axarr = plt.subplots(2,2,figsize=(100, 100))
fig.suptitle("color image", fontsize=16)
axarr[0,0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axarr[0,0].title.set_text('Original image')
axarr[0,1].imshow(blue_channel, cmap=plt.get_cmap('gray'))
axarr[0,1].title.set_text('blue channel')
axarr[1,0].imshow(green_channel, cmap=plt.get_cmap('gray'))
axarr[1,0].title.set_text('green channl')
axarr[1,1].imshow(red_channel, cmap=plt.get_cmap('gray'))
axarr[1,1].title.set_text('red channl')
plt.show()

image_size = [350,200]
resized_image = cv2.resize(image, (image_size[0], image_size[1]))

fig, axarr = plt.subplots(1,2, figsize=(100, 100))
fig.suptitle("image Resizing", fontsize=16)
axarr[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axarr[0].title.set_text('color image')
axarr[1].imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
axarr[1].title.set_text('resized image')
plt.show()

Modified_image = image.copy()
# Modified_image[1:30,:] = [100,0,100]
# Modified_image[30:60,:] = [0,255,200]
# Modified_image[60:,:] = [10,100,25]

Modified_image[1:100,:] = [100,0,100]
Modified_image[100:200,:] = [0,255,200]
Modified_image[200:,:] = [10,100,25]

fig, axarr = plt.subplots(1,2, figsize=(100, 100))
fig.suptitle("Updating image", fontsize=16)
axarr[0].imshow(cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
axarr[0].title.set_text('resized image')
axarr[1].imshow(cv2.cvtColor(Modified_image, cv2.COLOR_BGR2RGB))
axarr[1].title.set_text('updated image')
plt.show()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
fig, axarr = plt.subplots(1,2, figsize=(100, 100))
fig.suptitle("Image type", fontsize=16)
axarr[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axarr[0].title.set_text('color image')
axarr[1].imshow(gray, cmap=plt.get_cmap('gray'))
axarr[1].title.set_text('gray image')
plt.show()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert_image = cv2.bitwise_not(gray)
plt.imshow(invert_image, cmap=plt.get_cmap('gray'))
plt.show()
ret,thresh1 = cv2.threshold(invert_image,70,255,cv2.THRESH_BINARY)
plt.imshow(thresh1, cmap=plt.get_cmap('gray'))
plt.show()

cv2.imwrite('D:\\ImageManipulation\\beginner_programming\\images\\Color_Image_resized.jpg',cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))
cv2.imwrite('D:\\ImageManipulation\\beginner_programming\\images\\Color_Image_modified.jpg',cv2.cvtColor(Modified_image, cv2.COLOR_BGR2RGB))
cv2.imwrite('D:\\ImageManipulation\\beginner_programming\\images\\Color_Image_new.jpg',cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
cv2.imwrite('D:\\ImageManipulation\\beginner_programming\\images\\gray_Image.jpg', gray)







