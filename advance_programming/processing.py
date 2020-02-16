import numpy as np
import cv2

def get_image_size(image):
    return image.shape

def get_image_width(image):
    return image.shape[1]

def get_image_heigh(image):
    return image.shape[0]

def get_channel_form_image_by_channel_Id(image, chnnel_id):
    channel = image[:,:,chnnel_id]
    return channel

def get_color_channel_from_image_by_channel_Id(image, chnnel_id):
    # extract a channel
    channel = get_channel_form_image_by_channel_Id(image, chnnel_id)

    # create empty image with same shape as that of src image
    channel_image = np.zeros(image.shape, dtype=np.uint8)

    # assign each channel of src to an empty image
    channel_image[:, :, chnnel_id]  = channel
    return channel_image

def get_grayscale_image(image):
    shape = len(image.shape)
    if shape != 3:
        raise AssertionError("input image has " + str(shape) + " channels but it must have 3 channels!")
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return grayscale_image

def get_resized_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return resized_image

def get_threshlded_image(image, threshold_value, max_value):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    invered_image = cv2.bitwise_not(gray)
    _,thresholded_image = cv2.threshold(invered_image, threshold_value, max_value, cv2.THRESH_BINARY)
    return thresholded_image

def get_tiled_image(image,tile_count, colors):
    if len(image.shape) != 3:
        raise AssertionError("invalid input image!")
    if image.shape[2]!= 3:
        raise AssertionError("input image has " + str(image.shape[2]) + " channels but it must have 3 channels!")

    if not isinstance(colors, list):
        raise AssertionError("colors should be provided as a list")
    if len(colors)== 0:
        raise AssertionError("colors is empty!")
    if not isinstance(tile_count, dict):
        raise AssertionError("tile_size should be provided as a dict")

    tiled_image = image.copy()
    image_width = image.shape[1]
    image_height = image.shape[0]

    tile_width =int(image_width/tile_count["width"])
    tile_height = int(image_height / tile_count["height"])

    # loop without using lambda  function
    image_tiles = []
    use_lambda = True
    if use_lambda:
        image_tiles = [tiled_image[y:y + tile_height, x:x + tile_width] for y in range(0, image_height, tile_height)
                       for x in range(0, image_width, tile_width)]
    else:
        for y in range(0, image_height, tile_height):
            for x in range(0, image_width, tile_width):
                image_tiles.append(tiled_image[y:y + tile_height, x:x + tile_width])


    if len(image_tiles) < len(colors):
        raise AssertionError("number of colors does not match number of tiles")

    for tile_index in range(len(colors)):
        image_tiles[tile_index][:,:] = colors[tile_index]

    return tiled_image

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

