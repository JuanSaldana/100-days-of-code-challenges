""" To extract the colors from an image, and export a list of rgbs"""
import colorgram

COLORS = []
colors = colorgram.extract("day-18/damien-hirst-bromobenzotrifluoride.jpg", 30)

for color in colors:
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b
    new_color_tuple = (red, green, blue)
    # if color is somewhere close to either white or black
    if 20 > red > 230 and 20 > green > 230 and 20 > blue > 230:
        # then ignore it
        continue
    COLORS.append(new_color_tuple)
