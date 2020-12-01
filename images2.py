# Image Processing - Python script which show image in new window, rotate image, resize image and crop image

from PIL import Image, ImageFilter

img = Image.open('./Pokedox/pikachu.jpg')
filtered_img = img.convert('L')

# show image in new window
filtered_img.show()

# rotate image to specified angle
crooked = filtered_img.rotate(180)
crooked.save('grey_rotate.png', 'png')

# resize image needs tuple as a parameter
resize = filtered_img.resize((300, 300))
resize.save("grey_resize.png", "png")

# crop images
box = (100, 100, 400, 400)
region = filtered_img.crop(box)
region.save("grey_crop.png", 'png')
