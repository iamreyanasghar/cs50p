# run these commands in terminal before running the program

# wget https://cs50.harvard.edu/python/2022/psets/6/shirt/shirt.png
# wget https://cs50.harvard.edu/python/2022/psets/6/shirt/muppets.zip
# unzip muppets.zip

from PIL import Image, ImageOps
from pathlib import Path
import sys
import os

if len(sys.argv) != 3:
    sys.exit("Usage: python shirt.py input output")

input_file = sys.argv[1]
output_file = sys.argv[2]

inp_ext = Path(input_file).suffix.lower()
out_ext = Path(output_file).suffix.lower()

valid_ext = [".jpg", ".jpeg", ".png"]

if inp_ext not in valid_ext or out_ext not in valid_ext:
    sys.exit("Invalid Input")

if inp_ext != out_ext:
    sys.exit("Input and output have different extensions")

try:
    input_image = Image.open(input_file)

except FileNotFoundError:
    sys.exit("Input does not exist")


shirt = Image.open("shirt.png")

size = shirt.size
fitted = ImageOps.fit(input_image, size)

fitted.paste(shirt, shirt)

fitted.save(output_file)
