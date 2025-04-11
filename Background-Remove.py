from rembg import remove
from PIL import Image



# Input and output file paths
input_path = 'image.jpg'
output_path = 'image.png'

# Open the input image
inp = Image.open(input_path)

# Remove the background
output = remove(inp)

# Save the output image
output.save(output_path)

# Open and show the saved image (optional)
Image.open(output_path).show()
