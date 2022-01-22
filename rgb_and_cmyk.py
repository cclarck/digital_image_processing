#!/usr/bin/env python3
#2021-11-10 10:07:35 CST
#title= RGB and CMYK
from PIL import Image, ImageDraw, ImageChops

img_w = 600
img_h = 268

# prepare a blank for a image
# using mode "L" 8-bit pixels, black and white
# size (img_w, img_h)
# color 255 -> CMYK
# color 0 -> RGB
img_blank_rgb = Image.new("L", (img_w, img_h), 0)
img_blank_cmyk = Image.new("L", (img_w, img_h), 255)
#img_result.show()
img_draw_rgb = ImageDraw.Draw(img_blank_rgb)
img_draw_cmyk = ImageDraw.Draw(img_blank_cmyk)

circle_x = 125
circle_y = 125
circle_radius = 75

# fill: 255 -> RGB; 0 -> CMYK
img_draw_rgb.ellipse(
    [(circle_x - circle_radius, circle_y - circle_radius), 
    (circle_x + circle_radius, circle_y + circle_radius)], fill=255
)

img_draw_cmyk.ellipse(
    [(circle_x * 2 - circle_radius, circle_y - circle_radius), 
    (circle_x * 2 + circle_radius, circle_y + circle_radius)], fill=0
)

circle_offset = 40
rgb_r = ImageChops.offset(img_blank_rgb, 0, -circle_offset)
rgb_g = ImageChops.offset(img_blank_rgb, -circle_offset, circle_offset)
rgb_b = ImageChops.offset(img_blank_rgb, circle_offset, circle_offset)

cmyk_r = ImageChops.offset(img_blank_cmyk, 0, -circle_offset)
cmyk_g = ImageChops.offset(img_blank_cmyk, -circle_offset, circle_offset)
cmyk_b = ImageChops.offset(img_blank_cmyk, circle_offset, circle_offset)

circle_rgb = Image.merge("RGB", (rgb_r, rgb_g, rgb_b))
circle_cmyk = Image.merge("RGB", (cmyk_r, cmyk_g, cmyk_b))

circle_rgb.show()
circle_cmyk.show()
