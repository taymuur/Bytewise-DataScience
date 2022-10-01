# Image Converter Using Python

## Importing the libraries
```python
from PIL import Image
import glob
```

## PNG to JPEG Conversion
```python
for file in glob.glob("*.png"):
    image = Image.open(file)
    rgb_im = image.convert('RGB')
    rgb_im.save(file.replace("png", "jpg"), quality=100)
```

## JPG to PNG Conversion
```python
for file in glob.glob("*.jpg"):
    image = Image.open(file)
    rgb_im = image.convert('RGBA')
    rgb_im.save("conv_"+file.replace("jpg", "png"), quality=99)
```
