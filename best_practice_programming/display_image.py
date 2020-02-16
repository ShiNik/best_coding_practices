from  util import get_plot_configs, get_plot_size, plot_image, get_full_output_path
import processing

import cv2
import numpy as np

blue_channel_id = 0
green_channel_id = 1
red_channel_id = 2

def get_channels(image):
    blue_channel = processing.get_channel_form_image_by_channel_Id(image, blue_channel_id)
    green_channel = processing.get_channel_form_image_by_channel_Id(image, green_channel_id)
    red_channel = processing.get_channel_form_image_by_channel_Id(image, red_channel_id)
    return blue_channel, green_channel, red_channel

def get_image_channels(image):
    blue_image = processing.get_color_channel_from_image_by_channel_Id(image, blue_channel_id)
    green_image = processing.get_color_channel_from_image_by_channel_Id(image, green_channel_id)
    red_image = processing.get_color_channel_from_image_by_channel_Id(image, red_channel_id)
    return blue_image, green_image, red_image

def display_color_channels(image, save_image = True):
    #extract red channel
    blue_channel, green_channel, red_channel = get_channels(image)

    key_values, color_map_type = get_plot_configs()

    plot_title = "color image and its channels"
    image_info = [{key_values[0]: image, key_values[1]: "Original image", key_values[2]: color_map_type["color"]},
                  {key_values[0]: blue_channel, key_values[1]: "blue channel", key_values[2]: color_map_type["gray"]},
                  {key_values[0]: green_channel, key_values[1]: "green channl", key_values[2]: color_map_type["gray"]},
                  {key_values[0]: red_channel, key_values[1]: "red channl", key_values[2]: color_map_type["gray"]},
                  ]

    plot_size = get_plot_size(len(image_info))
    plot_image(plot_size=plot_size, plot_title=plot_title, image_info=image_info, key_values=key_values)

    if save_image:
        file_name = get_full_output_path("blue_channel.jpg")
        cv2.imwrite(file_name, blue_channel)

        file_name = get_full_output_path("green_channel.jpg")
        cv2.imwrite(file_name, green_channel)

        file_name = get_full_output_path("red_channel.jpg")
        cv2.imwrite(file_name, red_channel)

def display_color_image(image, save_image = True):
    blue_image, green_image, red_image = get_image_channels(image)

    key_values, color_map_type = get_plot_configs()
    plot_title = "color image and its channels"
    image_info = [{key_values[0]: image, key_values[1]: "Original image", key_values[2]: color_map_type["color"]},
                  {key_values[0]: blue_image, key_values[1]: "blue channel", key_values[2]: color_map_type["color"]},
                  {key_values[0]: green_image, key_values[1]: "green channl", key_values[2]: color_map_type["color"]},
                  {key_values[0]: red_image, key_values[1]: "red channl", key_values[2]: color_map_type["color"]},
                  ]

    plot_size = get_plot_size(len(image_info))
    plot_image(plot_size=plot_size, plot_title=plot_title, image_info=image_info, key_values=key_values)

    if save_image:
        file_name = get_full_output_path("Color_Image_blue.jpg")
        cv2.imwrite(file_name, cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))

        file_name = get_full_output_path("Color_Image_green.jpg")
        cv2.imwrite(file_name, cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))

        file_name = get_full_output_path("Color_Image_red.jpg")
        cv2.imwrite(file_name, cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))

def display_gray_scale_image(image, save_image = True):
    grayscale_imag = processing.get_grayscale_image(image)

    key_values, color_map_type = get_plot_configs()

    plot_title = "Image type"
    image_info = [{key_values[0]: image, key_values[1]: "color image", key_values[2]: color_map_type["color"]},
                  {key_values[0]: grayscale_imag, key_values[1]: "gray Image", key_values[2]: color_map_type["gray"]},
                  ]

    plot_size = get_plot_size(len(image_info))
    plot_image(plot_size=plot_size, plot_title=plot_title, image_info=image_info, key_values=key_values)

    if save_image:
        file_name = get_full_output_path("gray_Image.jpg")
        cv2.imwrite(file_name, grayscale_imag)

def display_resized_image(image, scale_percent, save_image = True):
    resized_image = processing.get_resized_image(image, scale_percent)

    key_values, color_map_type = get_plot_configs()

    plot_title = "resize image by " + str(scale_percent) + " of its size"
    image_info = [{key_values[0]: image, key_values[1]: "original image", key_values[2]: color_map_type["color"]},
                  {key_values[0]: resized_image, key_values[1]: "resized image", key_values[2]: color_map_type["color"]},
                  ]

    plot_size = get_plot_size(len(image_info))
    plot_image(plot_size=plot_size, plot_title=plot_title, image_info=image_info, key_values=key_values)

    if save_image:
        file_name = get_full_output_path("Color_Image_resized.jpg")
        cv2.imwrite(file_name, cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))

def display_tiled_image(image,tile_count, colors, save_image = True):
    tiled_image = processing.get_tiled_image(image, tile_count, colors)

    key_values, color_map_type = get_plot_configs()

    plot_title = "tiled image "
    image_info = [{key_values[0]: image, key_values[1]: "original image", key_values[2]: color_map_type["color"]},
                  {key_values[0]: tiled_image, key_values[1]: "tiled image", key_values[2]: color_map_type["color"]},
                  ]

    plot_size = get_plot_size(len(image_info))
    plot_image(plot_size=plot_size, plot_title=plot_title, image_info=image_info, key_values=key_values)

    if save_image:
        file_name = get_full_output_path("Color_Image_modified.jpg")
        cv2.imwrite(file_name, cv2.cvtColor(tiled_image, cv2.COLOR_BGR2RGB))

def display_threshld_image(image, threshold_value, max_value, save_image = True):
    threshlded_image = processing.get_threshlded_image(image, threshold_value, max_value)

    key_values, color_map_type = get_plot_configs()

    plot_title = "Image type"
    image_info = [{key_values[0]: image, key_values[1]: "color image", key_values[2]: color_map_type["color"]},
                  {key_values[0]: threshlded_image, key_values[1]: "thresholded Image", key_values[2]: color_map_type["gray"]},
                  ]

    plot_size = get_plot_size(len(image_info))
    plot_image(plot_size=plot_size, plot_title=plot_title, image_info=image_info, key_values=key_values)

    if save_image:
        file_name = get_full_output_path("Color_Image_thresholded.jpg")
        cv2.imwrite(file_name, threshlded_image)

def post_process_conv_image(image, treshold_edge = 0, perform_absolute = False):
    # post processing on conv_x
    print("max: ", np.max(image), ", min: ", np.min(image))
    if perform_absolute:
        image = np.absolute(image)
    max = np.max(image)
    min = np.min(image)
    # Normalize (scaling the gray level to range on using int)
    image = (image - min) * 255 / (max - min)
    image = image.astype(np.uint8)
    print("max: ", np.max(image), ", min: ", np.min(image))
    image[image < treshold_edge] = 0

def display_convlution(image, save_image = True):
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

    conv_x = processing.convolve(gray, sobelX)
    post_process_conv_image(conv_x)

    conv_y = processing.convolve(gray, sobelY)
    post_process_conv_image(conv_y)

    conv_laplacian = processing.convolve(gray, laplacian)
    post_process_conv_image(conv_laplacian)

    # merger X and Y
    conv_x_y = conv_x.copy()
    conv_x_y = conv_x.__add__(conv_y)

    key_values, color_map_type = get_plot_configs()

    plot_title = "Edge extraction"
    image_info = [{key_values[0]: image, key_values[1]: "Original image", key_values[2]: color_map_type["color"]},
                  {key_values[0]: gray, key_values[1]: "grayscale image", key_values[2]: color_map_type["gray"]},
                  {key_values[0]: conv_x, key_values[1]: "sobelX image", key_values[2]: color_map_type["gray"]},
                  {key_values[0]: conv_y, key_values[1]: "sobelY image", key_values[2]: color_map_type["gray"]},
                  {key_values[0]: conv_x_y, key_values[1]: "sobelX_Y image", key_values[2]: color_map_type["gray"]},
                  {key_values[0]: conv_laplacian, key_values[1]: "laplacian image", key_values[2]: color_map_type["gray"]},
                  ]
    plot_size = get_plot_size(len(image_info))
    plot_image(plot_size=plot_size, plot_title=plot_title, image_info=image_info, key_values=key_values)

    if save_image:
        file_name = get_full_output_path("conv_gray_Image.jpg")
        cv2.imwrite(file_name, gray)

        file_name = get_full_output_path("conv_x.jpg")
        cv2.imwrite(file_name, conv_x)

        file_name = get_full_output_path("conv_y.jpg")
        cv2.imwrite(file_name, conv_y)

        file_name = get_full_output_path("conv_x_y.jpg")
        cv2.imwrite(file_name, conv_x_y)

        file_name = get_full_output_path("conv_laplacian.jpg")
        cv2.imwrite(file_name, conv_laplacian)