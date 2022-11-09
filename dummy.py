from jpeg_file_carver import JPEG_FileCarver
from bmp_file_carver import BMP_FileCarver
#### open file here#####
pointer = open("res_image", "rb")  #pointer


carver=BMP_FileCarver(pointer)
print(carver.carve())


##### close file here ####
pointer.close()