class Solution:
    def validIPAddress(self, IP: str) -> str:
        
        result="IPv4" #will start by assuming its IPv4
        count=0
        for x in IP.split('.'):
            try:
                if int(x) > 255 or int(x)<0: #check 1: must be 0-255
                    result="Neither"
                elif len(x)>3 or len(x)==0 or (int(x)<10 and len(x)!=1) or (100>int(x)>9  and len(x)!=2): #check 2: length of the number
                    result="Neither"
            except: #if its not convertable to int will make result Neither
                 result="Neither"
            count+=1
            
        if count!=4: 
            result="Neither"

        IP=IP.split(':') 
        if len(IP)!=8:
            return result #either IPv4 or Neither
        
        result="IPv6"  #else it check if its a valid ipv6
        
        for x in IP:
            try:
                d=int(x, 16) #so it goes in the except if error was raised and not a valid hex
                if x[0]=="-"  or len(x)>4 or len(x)==0:
                    return "Neither"
            except:
                return "Neither"
            
        return result    
            
            
