import numpy as np
from PIL import Image, ImageDraw


def grayscale(image):
    array = np.array(image)
    r,g,b = array[:,:,0], array[:,:,1], array[:,:,2]

    gray  = 0.2126 * r + 0.7152 * g + 0.0722 * b
    gray  = Image.fromarray(gray)

    return gray

def _image_to_input(image):
    image = image.convert('RGB')
    arr   = np.array(image)
    r,g,b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    bw    = _to_grayscale(r, g, b)

    bw[bw <  128] = 0
    bw[bw >= 128] = 1
    bw    = bw.flatten()

    return bw