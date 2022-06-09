# Third party modules
import numpy
from PIL import Image


def get_image(image_path): # https://stackoverflow.com/a/27960627
    """Get a numpy array of an image so that one can access values[x][y]."""
    image = Image.open(image_path, "r")
    width, height = image.size
    pixel_values = list(image.getdata())
    if image.mode == "RGB":
        channels = 3
    elif image.mode == "L":
        channels = 1
    else:
        print("Unknown mode: %s" % image.mode)
        return None
    pixel_values = numpy.array(pixel_values).reshape((width, height, channels))
    return pixel_values




def diffPixels(image):
	difference = 0
    
	base = get_image("Pride_Rollover_Base.jpg")
	diff = get_image(image)

	for i in range(1869):
		for j in range(1280):
			if numpy.sum(numpy.subtract(base[i][j], diff[i][j])) > 5 or numpy.sum(numpy.subtract(base[i][j], diff[i][j])) < -5:
				difference = difference + 1
				# print(numpy.sum(numpy.subtract(base[i][j], diff[i][j])))
	return difference
  
# print(difference)

import os
for filename in os.listdir(os.getcwd()):
	if filename.endswith(".jpg"):
		print(filename + " " + str(diffPixels(filename)))

# print(image[0])
# print(image.shape)