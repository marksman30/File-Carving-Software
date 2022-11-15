from naive_match import*

class BMP_FileCarver:
    def __init__(self,pointer): #constructor take a pointer passed externally
        self.pointer=pointer #initializing it as a attribute of the object

        
    def carve(self,n=10): # n is the number of iterations to be run
        stage=0 # shows which stage the string match is on
        image_count=0 #stores number of images found from the dump
        image_start_sig=0 #tells wether the footer has been scanned or not
        image_data=None
        size_data=None
        size=None
        while True:
            
            data=self.pointer.read(1) #reads a byte of data
            if not data: #end the loop if no other bytes left to search
                break
            if image_start_sig==0: #footer is yet to be found need to pass through 3 stages
                if stage==0:
                    
                    if match(data,'42'):
                        # print("hello1")
                        stage=1 #first header byte found move on to stage 1
                        image_data=data
                        continue

                elif stage==1:
                     if match(data,'4d'): #second header byte found move on to stage 2
                        # print("hello2")
                        stage=0 
                        image_data+=data
                        image_start_sig=1
                        
                     else:
                        stage=0 #if required byte not found move to initial stage (stage 0)
                        image_data=None
                
            else: #2 stage process
                 if stage==0:
                    #  print("hello")
                     size_data=data
                     image_data+=data
                     stage=1
                 elif stage==1:
                      size_data=data+size_data
                      image_data+=data
                      stage=2 
                 elif stage==2:
                     size_data=data+size_data
                     image_data+=data
                     stage=3   
                 elif stage==3:
                    #  print("hello")
                   
                     size_data=data+size_data
                   
                     image_data+=data
                     stage=0
                     image_start_sig=0
                     print(size_data)
                     size= int.from_bytes(size_data, byteorder='big')- 6
                     print('xxx')
                     print(size)
                     
                     image_data= image_data + self.pointer.read(size) 
                     image_count=image_count+1 
                     out_file = open("./extracted/bmp/out"+str(image_count)+".bmp", "wb")
                     out_file.write(image_data)
                     out_file.close()
                     image_data=None
                     size_data=None

        return image_count