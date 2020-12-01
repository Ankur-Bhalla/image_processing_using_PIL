# Image Processing - Image lost its aspect ratio if we compressed the image.
# Image is squeezed off. How to resolve this?
# Python script which will retain aspect ratio of images if we compressed the image.


from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
print(img.size)
new_img = img.resize((400, 400))  # aspect ratio changed
new_img.save('thumbnail_old.jpg')

# To keep aspect ratio same as original one use thumbnail method. thumbnail works in place.
# img.thumbnail((400,200))
img.thumbnail((400, 400))
img.save('thumbnail.jpg')
print(img.size)
