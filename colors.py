# colors.py

# Basic Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

# Additional Colors
PINK = (255, 192, 203)
BROWN = (165, 42, 42)
NAVY = (0, 0, 128)
LIME = (0, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
SILVER = (192, 192, 192)
MAROON = (128, 0, 0)
OLIVE = (128, 128, 0)
TEAL = (0, 128, 128)
red_intensity_list = [(r, 0, 0) for r in range(255, 155, -1)]
orange_intensiti_list = [(255, r, 0) for r in range(255, 10, -1)]
yellow_intensity_list =[(r, 255, 0) for r in range(155, 255, +1)]
intensity_list =  yellow_intensity_list + orange_intensiti_list + red_intensity_list 

