import binascii

in_file = open("res_image", "rb") 
count=0
mem=0
print(f"{mem:#0{6}x}",end="    ")
while True:
    data=in_file.read(1)
    if not data:
        break
    str_data=str(binascii.hexlify(bytearray(data)))[2:-1]
    print(str_data,end=" ")
    count=count+1
    mem=mem+1
    if count==16:
        count=0
        print("")
        print(f"{mem:#0{6}x}",end="    ")
        
in_file.close()
