def sequence(tup):
    # code here 
    diff = tup[1]-tup[0]
    last = tup[-1]
    next_terms =[last + diff*i for i in range(1,4)]
    return tup + tuple(next_terms)
    
    
    
    
    
