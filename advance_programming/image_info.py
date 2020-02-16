import processing

class ImageInfo():

    @staticmethod
    def get_channel_id(channel_name):
        switcher = {
            'blue': 0,
            'green': 1,
            'red': 2,
        }
        id = switcher.get(channel_name.lower(), -1)

        if id == -1:
            raise AssertionError("channel_name is invalid!")

        return id

    @staticmethod
    def get_channels(image):
        id = ImageInfo.get_channel_id("blue")
        blue_channel = processing.get_channel_form_image_by_channel_Id(image, id)
        id = ImageInfo.get_channel_id("green")
        green_channel = processing.get_channel_form_image_by_channel_Id(image, id)
        id = ImageInfo.get_channel_id("red")
        red_channel = processing.get_channel_form_image_by_channel_Id(image, id)
        return blue_channel, green_channel, red_channel

    @staticmethod
    def get_image_channels(image):
        id = ImageInfo.get_channel_id("blue")
        blue_image = processing.get_color_channel_from_image_by_channel_Id(image, id)
        id = ImageInfo.get_channel_id("green")
        green_image = processing.get_color_channel_from_image_by_channel_Id(image, id)
        id = ImageInfo.get_channel_id("red")
        red_image = processing.get_color_channel_from_image_by_channel_Id(image, id)
        return blue_image, green_image, red_image