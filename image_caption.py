from PIL import Image
import os

# Small dictionary of image filenames and their captions
captions = {
    "cat.jpg": "A cute cat is sitting calmly.",
    "dog.jpg": "A happy dog enjoying the outdoors.",
    "mountain.jpg": "Beautiful snow-covered mountains.",
    "beach.jpg": "Golden sand with blue ocean waves."
}

def generate_caption(image_path):
    filename = os.path.basename(image_path)
    if filename in captions:
        return captions[filename]
    else:
        return "An image of something interesting."

# Load and show the image
image_path = input("Enter image filename (with extension): ")
try:
    img = Image.open(image_path)
    img.show()  # Opens the image in the default viewer
    caption = generate_caption(image_path)
    print("\nGenerated Caption:", caption)
except FileNotFoundError:
    print("Image file not found. Please check the path.")