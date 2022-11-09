import binascii

in_file = open("bmp_24.bmp", "rb") # opening for [r]eading as [b]inary
data = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()



out_file = open("out.bin", "wb") # open for [w]riting as [b]inary
out_file.write(data)
out_file.close()