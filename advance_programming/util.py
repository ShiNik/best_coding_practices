from configuration import ManipulationConfig as config
import processing

import cv2
import matplotlib.pyplot as plt
import numpy as np

def get_full_output_path(file_name):
    full_path = config.get_full_output_path(config, file_name)
    return full_path

def get_full_input_path(file_name):
    full_path = config.get_full_input_path(config, file_name)
    return full_path

def get_plot_configs():
    return config.get_plot_configs(config)
def get_plot_size(num_items):
    num_col = 2
    num_row = int(np.ceil(num_items/num_col))
    return {"row_size": num_row, "col_size": num_col}

def plot_image(plot_size, plot_title, image_info, key_values):
    # Error handeling
    if not isinstance(key_values, list):
        raise AssertionError("key_values should be provided as a list")
    if not isinstance(image_info, list):
        raise AssertionError("image_info should be provided as a list")
    if len(key_values)!= 3:
        raise AssertionError("invalid key_values!")
    if len(image_info)== 0:
        raise AssertionError("image_info is empty!")

    images = []
    titles = []
    color_map_type = []
    for info in image_info:
        # Error handeling
        if not isinstance(info, dict):
            raise AssertionError("image information should be provided as a dict!")
        for key_value in key_values:
            if key_value not in info:
                raise AssertionError("image information missing '" +  key_value +"' field!")

        images.append(info[key_values[0]])
        titles.append(info[key_values[1]])
        color_map_type.append(info[key_values[2]])
    fig, axs = plt.subplots(plot_size["row_size"], plot_size["col_size"], figsize=(10, 10), gridspec_kw = {'wspace':0.2, 'hspace':0.15})
    fig.suptitle(plot_title, fontsize=15)
    axs = axs.flatten()
    for img, title, type, ax in zip(images, titles, color_map_type, axs):
        image_to_display = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) if len(img.shape) == 3 else img
        ax.imshow(image_to_display, cmap = plt.get_cmap(type))
        ax.set_title(title, size=10)
    plt.show()

def print_image_properties(image):
    print("image size: ",processing.get_image_size(image))
    print("image width: ",processing.get_image_width(image))
    print("image height: ",processing.get_image_heigh(image))




