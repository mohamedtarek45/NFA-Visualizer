# XY|Z*
def state0(n):
    if(len(n)==0):
        return True
        
    else:    
        if (n[0]=='x'):
            return state1(n[1:])
        elif (n[0]=='z'):
            return state2(n[1:])
        else:
            return False   

def state1(n):
    if(len(n)==0):
        return False
        
    else:  
        if (n[0]=='y'):
            return state3(n[1:])
        else:
            return False   
            
def state2(n):
    if(len(n)==0):
        return True
        
    else:   
        if (n[0]=='z'):
            return state2(n[1:])   
        else :
            return False


def state3(n):
        if(len(n)==0):
            return True
        else:
            return False