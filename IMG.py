from PIL import Image, ImageDraw
import numpy as np
import random

# Image dimensions
width, height = 800, 800

# Create a new blank image with white background
image = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(image)

# Function to generate random colors
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Generate patterns of circles and rectangles
for _ in range(100):  # Adjust the number of shapes
    shape_type = random.choice(["circle", "rectangle"])
    color = random_color()
    x0 = random.randint(0, width)
    y0 = random.randint(0, height)
    x1 = x0 + random.randint(20, 100)
    y1 = y0 + random.randint(20, 100)
    
    if shape_type == "circle":
        draw.ellipse([x0, y0, x1, y1], fill=color, outline=random_color())
    else:
        draw.rectangle([x0, y0, x1, y1], fill=color, outline=random_color())

# Apply a random gradient effect using NumPy
data = np.array(image)
for i in range(width):
    for j in range(height):
        r, g, b = data[j, i]
        data[j, i] = (r // (i % 50 + 1), g // (j % 50 + 1), b // ((i + j) % 50 + 1))

# Convert back to an image and save
final_image = Image.fromarray(data)
final_image.show()
final_image.save("generated_artistic_image.png")
