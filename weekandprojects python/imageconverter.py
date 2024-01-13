#first we need to install pillow library
from PIL import Image
img_rgb = Image.open('sample1.jpg')#creating a file object
img_gray = img_rgb.convert('RGB')#changing color
img_gray.save('sample(rgb1).jpg')# saving file