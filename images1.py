# Image processing using pillow - Image class, ImageFilter class & convert images to different format
# Pillow is the friendly PIL fork by Alex Clark and Contributors.
# PIL is the Python Imaging Library by Fredrik Lundh and Contributors.

from PIL import Image, ImageFilter

img = Image.open('./Pokedox/pikachu.jpg')
# Use of Image class
print(img)
print(img.format)
print(img.size)
print(img.mode)
print(dir(img))

# Use of ImageFilter class
filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save('blur.png', 'png')  # convert jpg to png because png supports these image filters.

# Convert images to different format
filtered_img = img.convert('L')  # convert format to grey scale (black & white), Also we can convert to RGB
filtered_img.save('grey.png', 'png')  # convert jpg to png because png supports these image filters.
