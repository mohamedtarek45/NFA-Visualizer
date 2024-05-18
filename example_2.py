"""
(a | b) * abb

"""

def state_0(n):
    if len(n) == 0:  
        return False
    elif (len(n)==3):
        if(n[0]=='a'):
            return state_1(n[1:])
        else:
            return False 
    else:
        if(n[0]=='a'):
            return state_0(n[1:])
        elif(n[0]=='b'):
            return state_0(n[1:])
        else:
            return False  
 
def state_1(n):
    if len(n) == 0:  
        return False
    else:
        if(n[0]=='b'):
            return state_2(n[1:])
        else:
            return False
            
def state_2(n):
    if len(n) == 0:  
        return False
    else:
        if(n[0]=='b'):
            return True
        else:
            return False
           