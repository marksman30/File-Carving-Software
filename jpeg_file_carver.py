from naive_match import*

class JPEG_FileCarver:
    def __init__(self,pointer): #constructor take a pointer passed externally
        self.pointer=pointer #initializing it as a attribute of the object

    
    def carve(self,n=10): # n is the number of iterations to be run
        stage=0 # shows which stage the string match is on
        image_count=0 #stores number of images found from the dump
        image_start_sig=0 #tells wether the footer has been scanned or not
        image_data=None
        extracted_files = {} #stores the extracted jpg files
        while True:
            
            data=self.pointer.read(1) #reads a byte of data
            if not data: #end the loop if no other bytes left to search
                break
            if image_start_sig==0: #footer is yet to be found need to pass through 3 stages
                if stage==0:
                    if match(data,'ff'):
                        stage=1 #first header byte found move on to stage 1
                        image_data=data

                elif stage==1:
                    if match(data,'d8'): #second header byte found move on to stage 2
                        stage=2 
                        image_data+=data
                    else:
                        stage=0 #if required byte not found move to initial stage (stage 0)
                        image_data=None
                elif stage==2:
                    if match(data,'ff'): #third header byte found change image_start signal
                        image_start_sig=1
                        stage=0 
                        image_data+=data
                        
                    else:
                        stage=0
                        image_data=None
            else: #2 stage process
                image_data+=data
                if stage==0:
                    if match(data,'ff'): #first footer byte found
                        stage=1 #move on to next stage
                elif stage==1:
                    if match(data,'d9'): #second header byte found 
                        image_count+=1 #increment counter
                        image_start_sig=0
                        stage=0
                        out_file = open("./extracted/jpeg/out"+str(image_count)+".jpg", "wb")
                        out_file.write(image_data)
                        out_file.close()
                        extracted_files[image_count] = image_data
                        image_data=None
                    else:
                        stage=0#go back to initial stage

        return image_count,extracted_files

                
                    
            
        
