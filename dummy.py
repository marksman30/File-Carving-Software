from jpeg_file_carver import JPEG_FileCarver

in_file = open("out.bin", "rb")  #pointer
carver=JPEG_FileCarver(in_file)
carver.carve(10)
in_file.close()