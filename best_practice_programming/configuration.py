#Declare constants in a separate file called constant.py
class ManipulationConfig:
    def __init__(self):
        self.color_map_type   = {"color":'BrBG',"gray":'gray'}
        self.key_values = ["image", "title", "color_map_type"]
        self.output_path = ".\\images\output\\"
        self.input_path = ".\\images\input\\"

    def get_color_map_type(self):
        return self.color_map_type
    def get_key_values(self):
        return self.key_values

    @staticmethod
    def get_full_input_path(ManipulationConfig, file_name):
        return ManipulationConfig().input_path+ file_name

    @staticmethod
    def get_full_output_path(ManipulationConfig, file_name):
        return ManipulationConfig().output_path + file_name

    @staticmethod
    def get_plot_configs(ManipulationConfig):
        key_values = ManipulationConfig().get_key_values()
        color_map_type = ManipulationConfig().get_color_map_type()
        return key_values, color_map_type