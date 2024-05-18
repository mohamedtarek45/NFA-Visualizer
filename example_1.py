#x(x|y)*|z

def state_0(n):
    #if length of n become 0 
    #then print not accepted
    if(len(n)==0):
        return False
        
    else: 
        #if at zero index 
        #'X' found call
        #stateY function    
        if (n[0]=='X'):
            return state_1(n[1:])
        
   
        #if at zero index 
        #'Z' then print 
        #not accepted
        elif (n[0]=='Z'):
            return state_2(n[1:])
        else:
            return False 

def state_1(n):
    #if length of n become 0 
    #then print accepted
    if(len(n)==0):
        return True
        
    else:  
        #if at zero index 
        #'X' found call
        #stateZ function    
        if (n[0]=='X'):
            return state_1(n[1:]) 
            
        #if at zero index 
        #'Y' found call
        #stateZ function    
        elif (n[0]=='Y'):
            return state_1(n[1:])
        #if at zero index 
        #'Z' found call
        #stateZ function    
        else:
            return False       
       
def state_2(n):
    #if length of n become 0 
    #then print not accepted
    if(len(n)==0):
        return True
        
    else:  
        return False
            