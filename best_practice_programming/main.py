from util import get_full_input_path, print_image_properties
import display_image as di

import cv2
def main():
    file_name = get_full_input_path("Color_Image_convlution.jpg")
    image = cv2.imread(file_name)
    print_image_properties(image)
    di.display_convlution(image)

    #read image
    #When you use opencv (imread, VideoCapture), the images are loaded in the BGR color space.
    file_name = get_full_input_path("Color_Image.jpg")
    image = cv2.imread(file_name)
    print_image_properties(image)

    # Display threshold image
    threshold_value, max_value = 70,255
    di.display_threshld_image(image,  threshold_value, max_value)

    # Display image update
    tile_size = {"height":2, "width":2}
    colors = [[100,0,100], [0,255,200], [10,100,25],[10,14,100]]
    di.display_tiled_image(image, tile_size, colors)

    # Display resied image
    scale_percent = 60  # percent of original size
    di.display_resized_image(image, scale_percent)

    # Display gray scale image
    di.display_gray_scale_image(image)

    # Display color image
    di.display_color_channels(image)
    di.display_color_image(image)

main()


