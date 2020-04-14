# LAD - Light Angle Detector
## Brightness Mean Algorithm
- Normal Image :          
![normal Image](readmeAssets/normal.png)
- Converted into black and white image
- Image with only bright pixels (white mask) :           
![white mask](readmeAssets/whitemask.png)
- Image with only dark pixels (black mask) :          
![black mask](readmeAssets/blackmask.png)
- In both images, the average pixel is calculated
- Output Image :           
![output image](readmeAssets/output.png)
- In above image the Green dot indicates the white mask average pixel and the Blue dot indicates average pixel of the black mask    
#### Warning : This algorithm doesn't work 100% of the time and sometime gives wrong angle and vector. You can calculate the angle by the slope of the vector made by two points(green and blue)
