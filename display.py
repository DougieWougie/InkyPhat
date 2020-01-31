from inky import InkyPHAT
from PIL import Image, ImageFont, ImageDraw

inky_display = InkyPHAT("red")
inky_display.set_border(inky_display.WHITE)

# image = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
image = Image.open("bg.png")
draw = ImageDraw.Draw(image)

inky_display.set_image(image)
inky_display.show()
