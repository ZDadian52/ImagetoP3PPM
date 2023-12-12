from PIL import Image

# Open the JPG image
input_image = Image.open("map.png")

# Convert the image to RGB mode (if it's not already in RGB mode)
rgb_image = input_image.convert("RGB")

# Get image width and height
width, height = rgb_image.size

# Open a new PPM file in write mode
with open("map.ppm", "w") as ppm_file:
    # Write PPM header
    ppm_file.write("P3\n")
    ppm_file.write("# America, LETS GO\n")
    ppm_file.write(f"{width} {height}\n")
    ppm_file.write("255\n")  # Maximum color value

    # Iterate through each pixel and write RGB values to the PPM file
    for y in range(height):
        for x in range(width):
            r, g, b = rgb_image.getpixel((x, y))
            ppm_file.write(f"{r}\n{g}\n{b}\n")

# Print a message indicating the conversion is complete
print("Conversion from JPG to P3 PPM completed. Output file: map.ppm")
