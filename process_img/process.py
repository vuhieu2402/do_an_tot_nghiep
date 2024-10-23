from PIL import Image



img_file = 'page_01.jpg'

img = Image.open(img_file)

print(img)
img.show()