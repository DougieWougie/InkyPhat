# InkyPhat
The Python code running on the Pimoroni InkyPhat sitting in front of my TV.

- [Pimoroni tutorial](https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat)
- [Inky Python Library](https://github.com/pimoroni/inky)

Pretty pointless - displays an image and tells you which bin to put out, probably add more later.

## How it works
The eInk screen really only does one thing, it displays and image. Images are built using the [Python Image Library](https://pypi.org/project/Pillow/)'s [ImageDraw module](https://pillow.readthedocs.io/en/stable/reference/ImageDraw.html). I have a red one BTW:
1. Import the library `from inky import InkyPhat`
2. Instantiate the class `inkyphat = InkyPHAT('red')`
3. Set the image `inkyphat.set_image(image)`
4. Set the border `inkyphat.set_border(inky.RED)`
5. Update the display `inkyphat.show()`

## More about the image
I'm using [Gimp](https://www.gimp.org) which is handy as Pimoroni provide a [palette](https://github.com/pimoroni/inky/blob/master/tools/inky-palette.gpl). Images are 212x104 PNG-8 format.

