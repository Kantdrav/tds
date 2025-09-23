import base64

# Read and encode the image
with open('image.png', 'rb') as f:
    binary_data = f.read()
    image_b64_encoding = base64.b64encode(binary_data).decode('utf-8')  # Encode and decode to string

print(image_b64_encoding)  # This is the base64 string

# Decode and write back to a new image
with open('texttoimage.png', 'wb') as f:
    dbd = base64.b64decode(image_b64_encoding)  # Decode the base64 string
    f.write(dbd)
