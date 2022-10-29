from jpeg_file_carver import JPEG_FileCarver
#### open file here#####
pointer = open("res_image", "rb")  #pointer


carver=JPEG_FileCarver(pointer)
print(carver.carve())


##### close file here ####
pointer.close()