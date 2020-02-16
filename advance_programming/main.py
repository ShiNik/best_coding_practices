from util import get_full_input_path, print_image_properties
import  display_image as di

import cv2

def generate_displayer(displayer_type):
    switcher = {
        'channel': di.DisplayColorChannels(),
        'color': di.DisplayColorImage(),
        'gray': di.DisplayGrayScaleImage(),
        'resized': di.DisplayResizedImage(),
        'tiled': di.DisplayTiledImage(),
        'threshold': di.DisplayThreshldImage(),
        'convlution': di.DisplayConvlutionImage(),
    }

    displayer = switcher.get(displayer_type.lower(), None)

    if displayer == None:
        raise AssertionError("displayer_type is invalid!")

    return displayer

def main():
    #read image
    #When you use opencv (imread, VideoCapture), the images are loaded in the BGR color space.
    file_name = get_full_input_path("Color_Image.jpg")
    image = cv2.imread(file_name)
    print_image_properties(image)

    # Display color channel image
    displayer = generate_displayer("channel")
    displayer.show(image)

    # Display color image
    displayer = generate_displayer("color")
    displayer.show(image)

    # Display gray scale image
    displayer = generate_displayer("gray")
    displayer.show(image)

    # Display resized image
    argument_list = {'scale_percent': 60} # percent of original size
    displayer = generate_displayer("resized")
    displayer.show(image, **argument_list)

    # Display image update
    tile_size = {"height":2, "width":2}
    colors = [[100,0,100], [0,255,200], [10,100,25],[10,14,100]]
    argument_list = {'tile_size': tile_size,'colors':colors }
    displayer = generate_displayer("tiled")
    displayer.show(image, **argument_list)

    # Display threshold image
    argument_list = {'threshold_value': 70, 'max_value': 255}
    displayer = generate_displayer("threshold")
    displayer.show(image, **argument_list)


    file_name = get_full_input_path("Color_Image_convlution.jpg")
    image = cv2.imread(file_name)
    print_image_properties(image)
    displayer = generate_displayer("convlution")
    displayer.show(image)

main()


