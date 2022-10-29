import binascii
#byte matching function
def match(byte_data,one_byte_hex_string): #passing a byte data to the function
    string_data=str(binascii.hexlify(bytearray(byte_data)))[2:-1]  #will return two hex characters(like ff) in string format
    # b'xff'=>ff (while printing)
    
    if string_data==one_byte_hex_string: #checks if the scanned byte is equal to the target byte
        return True
    else:
        return False

