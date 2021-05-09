from random import randint
class Generate:
    def __init__(self, capital, lower, number, character, length):
        self.capital = capital
        self.lower = lower
        self.number = number
        self.character = character
        self.length = length
        self.generation_funct()
        
    
    def generation_funct(self):
        numsarr = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0',]
        lowerarr = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        upperarr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S' ,'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        charsarr = ['£', '$', '%', '^', '&', '*', '(', ')', '@', '#', '~','?']
        genarr = []
        
        uppercase = False
        lowercase = False
        usenumbers = False
        usecharacters = False
        
        if self.capital == 1:
            uppercase = True
        if self.lower == 1:
            lowercase = True
        if self.number == 1:
            usenumbers = True
        if self.character == 1:
            usecharacters = True
        
        if uppercase == True:
            for i in range(len(upperarr)):
                tmp = upperarr[i]
                genarr.append(tmp)
        
        if lowercase == True:
            for i in range(len(lowerarr)):
                tmp1 = lowerarr[i]
                genarr.append(tmp1)
                
        if usenumbers == True:
            for i in range(len(numsarr)):
                tmp2 = numsarr[i]
                genarr.append(tmp2)
                
        if usecharacters == True:
            for i in range(len(charsarr)):
                tmp3 = charsarr[i]
                genarr.append(tmp3)
        
        
        genlength = len(genarr)
        password = ""
        
        for i in range(self.length):
            rand = randint(1, genlength)
            password += genarr[rand - 1]
               
        return password  

