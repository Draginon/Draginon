class Colors:
    dark_grey = (26, 31, 40)
    green = (40, 240, 20)
    red = (200, 30, 30)
    orange = (230, 150, 20)
    yellow = (237, 243, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    dark_green = (20, 80, 20)
    light_green = (44, 162, 30)

    @classmethod
    def get_cell_colors(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]
    