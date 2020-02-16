from  util import get_plot_configs, get_plot_size, plot_image, get_full_output_path
import processing
from  image_info import ImageInfo

import cv2
import numpy as np
from abc import ABC, abstractmethod

class DisplayImage():
    def __init__(self, plot_title, save_image = True):
        self.key_values, self.color_map_type = get_plot_configs()
        self.save_image = save_image
        self.plot_title = plot_title

    def plot_image(self, image_info):
        plot_size = get_plot_size(len(image_info))
        plot_image(plot_size=plot_size, plot_title=self.plot_title, image_info=image_info, key_values=self.key_values)

    @abstractmethod
    def show(self, image,**args):
        raise AssertionError("invalid call!")
class DisplayColorChannels(DisplayImage):
    def __init__(self, plot_title= "color image and its channels", save_image = True):
        super().__init__(plot_title, save_image)

    def show(self, image, **args ):
        if not isinstance(args, dict):
            raise AssertionError("args should be provided as a dict")
        if len(args)!=0:
            raise AssertionError("args is invalid!")

        blue_channel, green_channel, red_channel = ImageInfo.get_channels(image)

        image_info = [{self.key_values[0]: image,         self.key_values[1]: "Original image", self.key_values[2]: self.color_map_type["color"]},
                      {self.key_values[0]: blue_channel,  self.key_values[1]: "blue channel",   self.key_values[2]: self.color_map_type["gray"]},
                      {self.key_values[0]: green_channel, self.key_values[1]: "green channl",   self.key_values[2]: self.color_map_type["gray"]},
                      {self.key_values[0]: red_channel,   self.key_values[1]: "red channl",     self.key_values[2]: self.color_map_type["gray"]},
                      ]

        self.plot_image(image_info)

        if self.save_image:
            file_name = get_full_output_path("blue_channel.jpg")
            cv2.imwrite(file_name, blue_channel)

            file_name = get_full_output_path("green_channel.jpg")
            cv2.imwrite(file_name, green_channel)

            file_name = get_full_output_path("red_channel.jpg")
            cv2.imwrite(file_name, red_channel)

class DisplayColorImage(DisplayImage):
    def __init__(self, plot_title= "color image and its channels", save_image = True):
        super().__init__(plot_title, save_image)

    def show(self, image, **args ):
        if not isinstance(args, dict):
            raise AssertionError("args should be provided as a dict")
        if len(args)!=0:
            raise AssertionError("args is invalid!")

        blue_image, green_image, red_image = ImageInfo.get_image_channels(image)

        image_info = [{self.key_values[0]: image,       self.key_values[1]: "Original image", self.key_values[2]: self.color_map_type["color"]},
                      {self.key_values[0]: blue_image,  self.key_values[1]: "blue channel",   self.key_values[2]: self.color_map_type["color"]},
                      {self.key_values[0]: green_image, self.key_values[1]: "green channl",   self.key_values[2]: self.color_map_type["color"]},
                      {self.key_values[0]: red_image,   self.key_values[1]: "red channl",     self.key_values[2]: self.color_map_type["color"]},
                      ]

        self.plot_image(image_info)

        if self.save_image:
            file_name = get_full_output_path("Color_Image_blue.jpg")
            cv2.imwrite(file_name, cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB))

            file_name = get_full_output_path("Color_Image_green.jpg")
            cv2.imwrite(file_name, cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB))

            file_name = get_full_output_path("Color_Image_red.jpg")
            cv2.imwrite(file_name, cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB))

class DisplayGrayScaleImage(DisplayImage):
    def __init__(self, plot_title= "Image Type", save_image = True):
        super().__init__(plot_title, save_image)

    def show(self, image, **args ):
        if not isinstance(args, dict):
            raise AssertionError("args should be provided as a dict")
        if len(args)!=0:
            raise AssertionError("args is invalid!")

        grayscale_imag = processing.get_grayscale_image(image)

        image_info = [{self.key_values[0]: image,          self.key_values[1]: "color image", self.key_values[2]: self.color_map_type["color"]},
                      {self.key_values[0]: grayscale_imag, self.key_values[1]: "grayscaled image",  self.key_values[2]: self.color_map_type["gray"]},
                      ]

        self.plot_image(image_info)

        if self.save_image:
            file_name = get_full_output_path("gray_Image.jpg")
            cv2.imwrite(file_name, grayscale_imag)

class DisplayResizedImage(DisplayImage):
    def __init__(self, plot_title= "Resized Image", save_image = True):
        super().__init__(plot_title, save_image)

    def show(self, image, **args ):
        if not isinstance(args, dict):
            raise AssertionError("args should be provided as a dict")
        if len(args)!=1:
            raise AssertionError("args is invalid!")

        scale_percent = next(iter(args.values()))
        resized_image = processing.get_resized_image(image, scale_percent)

        self.plot_title = "Resized image by " + str(scale_percent) + " of its size"
        image_info = [{self.key_values[0]: image,         self.key_values[1]: "original image", self.key_values[2]: self.color_map_type["color"]},
                      {self.key_values[0]: resized_image, self.key_values[1]: "resized image",  self.key_values[2]: self.color_map_type["color"]},
                      ]

        self.plot_image(image_info)

        if self.save_image:
            file_name = get_full_output_path("Color_Image_resized.jpg")
            cv2.imwrite(file_name, cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB))

class DisplayTiledImage(DisplayImage):
    def __init__(self, plot_title= "Tiled Image", save_image = True):
        super().__init__(plot_title, save_image)

    def show(self, image, **args ):
        if not isinstance(args, dict):
            raise AssertionError("args should be provided as a dict")
        if len(args)!=2:
            raise AssertionError("args is invalid!")

        arg_list = list(args.keys())
        tile_count = args[arg_list[0]]
        colors = args[arg_list[1]]
        tiled_image = processing.get_tiled_image(image, tile_count, colors)

        image_info = [{self.key_values[0]: image, self.key_values[1]:       "original image", self.key_values[2]: self.color_map_type["color"]},
                      {self.key_values[0]: tiled_image, self.key_values[1]: "tiled image",    self.key_values[2]: self.color_map_type["color"]},
                      ]

        self.plot_image(image_info)

        if self.save_image:
            file_name = get_full_output_path("Color_Image_modified.jpg")
            cv2.imwrite(file_name, cv2.cvtColor(tiled_image, cv2.COLOR_BGR2RGB))

class DisplayThreshldImage(DisplayImage):
    def __init__(self, plot_title="Thresholded Image", save_image=True):
        super().__init__(plot_title, save_image)

    def show(self, image, **args):
        if not isinstance(args, dict):
            raise AssertionError("args should be provided as a dict")
        if len(args) != 2:
            raise AssertionError("args is invalid!")

        arg_list = list(args.keys())
        threshold_value = args[arg_list[0]]
        max_value = args[arg_list[1]]
        threshlded_image = processing.get_threshlded_image(image, threshold_value, max_value)

        image_info = [{self.key_values[0]: image,            self.key_values[1]: "color image",       self.key_values[2]: self.color_map_type["color"]},
                      {self.key_values[0]: threshlded_image, self.key_values[1]: "thresholded Image", self.key_values[2]: self.color_map_type["gray"]},
                      ]

        self.plot_image(image_info)

        if self.save_image:
            file_name = get_full_output_path("Color_Image_thresholded.jpg")
            cv2.imwrite(file_name, threshlded_image)

class DisplayConvlutionImage(DisplayImage):
    def __init__(self, plot_title= "Edge Extraction", save_image = True):
        super().__init__(plot_title, save_image)
        self.laplacian = np.array((
            [0, 1, 0],
            [1, -4, 1],
            [0, 1, 0]), dtype="int")

        # construct the Sobel x-axis kernel
        self.sobelX = np.array((
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]), dtype="int")

        # construct the Sobel y-axis kernel
        self.sobelY = np.array((
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]), dtype="int")

    def post_process_conv_image(self, image, treshold_edge=0, perform_absolute=False):
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

    def show(self, image, **args ):
        if not isinstance(args, dict):
            raise AssertionError("args should be provided as a dict")
        if len(args)>0:
            raise AssertionError("args is invalid!")

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        conv_x = processing.convolve(gray, self.sobelX)
        self.post_process_conv_image(conv_x)

        conv_y = processing.convolve(gray, self.sobelY)
        self.post_process_conv_image(conv_y)

        conv_laplacian = processing.convolve(gray, self.laplacian)
        self.post_process_conv_image(conv_laplacian)

        # merger X and Y
        conv_x_y = conv_x.copy()
        conv_x_y = conv_x.__add__(conv_y)

        image_info = [{self.key_values[0]: image,          self.key_values[1]: "Original image",  self.key_values[2]: self.color_map_type["color"]},
                      {self.key_values[0]: gray,           self.key_values[1]: "grayscale image", self.key_values[2]: self.color_map_type["gray"]},
                      {self.key_values[0]: conv_x,         self.key_values[1]: "sobelX image",    self.key_values[2]: self.color_map_type["gray"]},
                      {self.key_values[0]: conv_y,         self.key_values[1]: "sobelY image",    self.key_values[2]: self.color_map_type["gray"]},
                      {self.key_values[0]: conv_x_y,       self.key_values[1]: "sobelX_Y image",  self.key_values[2]: self.color_map_type["gray"]},
                      {self.key_values[0]: conv_laplacian, self.key_values[1]: "laplacian image", self.key_values[2]: self.color_map_type["gray"]}
                      ]

        self.plot_image(image_info)

        if self.save_image:
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