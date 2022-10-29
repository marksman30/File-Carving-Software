from naive_match import*

class JPEG_FileCarver:
    def __init__(self,pointer): #constructor take a pointer passed externally
        self.pointer=pointer #initializing it as a attribute of the object
    def carve(self,n=10): # n is the number of iterations to be run
        for i in range(n):
            data=self.pointer.read(1)
            if not data:
                break
            print(data)
        print("comming out")
