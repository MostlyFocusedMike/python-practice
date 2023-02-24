import numpy as np
from PIL import Image
from sklearn.datasets import load_sample_images

china = load_sample_images().images[0]
flower = load_sample_images().images[1]

# we see that these are 3d arrays, meaning they are rgb images
# 427x640 px, with 3 color channels (RGB)
# remember, the shape shows the number of items in the array
# 427 arrays at the top, each one of thsoe arrays has 640 items, and each of those 3
# so columns, then each row in the column, then the color data for that point

print(china.shape, china.dtype)
# (427, 640, 3), dtype('uint8')
print(flower.shape, flower.dtype)
# (427, 640, 3), dtype('uint8')

# Then we need to take these matrices and convert them to PIL Images
im_china = Image.fromarray(china) # The argument is assumed to be a numpy array of uint8
im_flower = Image.fromarray(flower)

# We can then save the PIL Images as actual files
im_china.save("china.png")
im_flower.save("flower.png")

# and open them
im = Image.open('china.png')
im.show()


# To convert back the other way, from PIL Image to numpy array
im = Image.open('china.png')
img = np.array(im)
print(img.shape, img.dtype)
# (427, 640, 3), dtype('uint8')

# We can also cast an image to grayscale by converting to "luminance"
gray = im.convert('L')
gray.show()

g = np.array(gray)
print(g.shape, g.dtype)
# (427, 640), dtype('uint8')
# Notice now how there is only 2 dimensions, since the color data can be a single number between white and black



