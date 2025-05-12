from PIL import Image

image = Image.open("example.jpg")

image = image.convert("RGB")

red, green, blue = image.split()

shifting = 100
left_coordinates = (shifting, 0, image.width, image.height)
left_red = red.crop(left_coordinates)

right_coordinates = (0, 0, image.width-shifting, image.height)
right_blue = blue.crop(right_coordinates)

shifting = shifting//2
middle_coordinates = (shifting, 0, image.width-shifting, image.height)

middle_red = red.crop(middle_coordinates)
middle_blue = blue.crop(middle_coordinates)
middle_green = green.crop(middle_coordinates)

red_mix = Image.blend(left_red, middle_red, 0.5)
blue_mix = Image.blend(right_blue, middle_blue, 0.5)

final_image = Image.merge("RGB", (red_mix, middle_green, blue_mix))
final_image.thumbnail((80, 80)) 
final_image.save('final_image.jpg') 
