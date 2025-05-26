import sys
from PIL import Image

if len(sys.argv) > 1:
    img = Image.open(sys.argv[1])
else:
    print("Usage: python main.py <image>")
    exit(1)

width, height = img.size

img = img.resize((80, int(height * (80 / width))))
width, height = img.size

pixels = []

characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"

for x in range(width):
    temp = []
    for y in range(height):
        temp.append(img.getpixel((x, y)))
    pixels.append(temp)

for y in range(height):
    for x in range(width):
        r, g, b, a = pixels[x][y]
        average = (r + g + b) / 3
        c = characters[int((average / 255) * (len(characters)) - 1)]
        print(c + c, end="")
    print()