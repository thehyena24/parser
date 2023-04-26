def GetID(file):
    with open(file) as f:
        flat_list=[word for line in f for word in line.split()]
        return int(flat_list[8])

def GetMonth(file):
    with open(file) as f:
        flat_list=[word for line in f for word in line.split()]
        date = flat_list[11]
        dateList = date.split("-")
        return int(dateList[0])


class Reader:
    
    def __init__(self, file, flat_list):
        self.file = file
        with open(file) as f:
            self.flat_list = [word for line in f for word in line.split()]


    
    

    def data1(self):
            return int(self.flat_list[35])
            
    def data2(self):
            return int(self.flat_list[43])
   


            




    

    def data3(self):
            return int(self.flat_list[161])

    def data4(self):
            return int(self.flat_list[170])
    





            

    

    def data5(self):
            return int(self.flat_list[199])

    def data6(self):
            return int(self.flat_list[207])

    def data7(self):
            return int(self.flat_list[215])

    def data8(self):
            return int(self.flat_list[223])

    def data9(self):
            return int(self.flat_list[231])

    def data10(self):
            return int(self.flat_list[239])

    def data11(self):
            return int(self.flat_list[247])

    def data12(self):
            return int(self.flat_list[256])
    


            


    

    def data13(self):
            return int(self.flat_list[268])

    def data14(self):
            return int(self.flat_list[276])

    def data15(self):
            return int(self.flat_list[283])

    def data16(self):
            return int(self.flat_list[291])

    def data17(self):
            return int(self.flat_list[300])

    def data18(self):
            return int(self.flat_list[310])

    def data19(self):
            return int(self.flat_list[321])

    def data20(self):
            return int(self.flat_list[329])

    def data21(self):
            return int(self.flat_list[338])

    def data22(self):
            return int(self.flat_list[349])

    def data23(self):
            return int(self.flat_list[359])

    def data24(self):
            return int(self.flat_list[369])
   
