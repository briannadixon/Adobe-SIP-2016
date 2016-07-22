import PIL
from PIL import Image
im = Image.open("puppy.jpg")
im.rotate(45).show()
#new_image.save("output.jpg","jpeg")

pixels = im.load()
#print (im.size)

all_pixels =[]


for x in range(1920):
    for y in range (1080):
        r= pixels[x,y][0]
        g=pixels[x,y][1]
        b=pixels[x,y][2]
        pixel_value=r+g+b
        #print(pixel_value)


for x in range(1920):
    for y in range (1080):
        if pixel_value<=182:
            all_pixels.append((0,51,76))
            
        if pixel_value>182 and pixel_value <=364:
            all_pixels.append((217,26,33))
            
        if pixel_value>364 and pixel_value <=546:
            all_pixels.append((112,150,158))
            
        if pixel_value>546:
           all_pixels.append((252,227,166))
            
            
im.putdata(all_pixels)
im.show()
