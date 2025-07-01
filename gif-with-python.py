#Final Proyect #Create a GIF with Python #The Legend of Python! #@saiyexstech 

import imageio.v3 as iio

#All images must have the same height and width.
filenames = ['london1.jpg', 'london2.jpg', 'london3.jpg', 'london4.jpg'] 
images = []

for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('gif-generated.gif', images, duration = 500, loop = 0)

