import binascii

in_file = open("index.jpg", "rb") # opening for [r]eading as [b]inary
data1 = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

in_file = open("out2.jpg", "rb") # opening for [r]eading as [b]inary
data2 = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

in_file = open("pole.jpeg", "rb") # opening for [r]eading as [b]inary
data3 = in_file.read() # if you only wanted to read 512 bytes, do .read(512)
in_file.close()

data=data1+data2+data3
out_file = open("out.bin", "wb") # open for [w]riting as [b]inary
out_file.write(data)
out_file.close()