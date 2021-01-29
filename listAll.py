# This script is about a simple list of 5 number
# It finds and returns "all" possible orders of given numbers 
# which meets our validation criteria

nums = [1,2,3,4,5] #list of possible numbers to be used
unums = [] #list of used numbers by our functions which would be completed stepwise automaticaly 

def isValid(used):
    if len(used) != 5:
        return True
    else:
        if (used[3]+used[4])==7: # Our validation criteria
            return True
        else:
            return False  

def xVal(ls, x):
    ls.append(x)
    if isValid(ls)== True:
        del ls[-1] 
        # deleting should be done before returning True or False, 
        # because that ends the function
        return True 
    else:
        del ls[-1]
        return False
    
log=[] # A list for logging each time a pattern is found
def solve(list,ulist,log):    
    if len(ulist)==5:
        print(ulist)
        log.append('1') # adding to the logger list each time a pattern is found
        # returning true is deleted to allow function to loop thoough all possible patterns
    
    for i in list:
        if i not in ulist:
            if xVal(ulist, i): 
                # validation should be done before appending, 
                # because as soon as the 5th appending is done for the first time,
                # function ends in the next recursion while it might be invalid!
                ulist.append(i)
                if solve(list,ulist,log):
                    return True
                del ulist[-1]
    return False # for situations if not any final answers is possible
    
   
solve(nums,unums,log)              
print("---------------")
print(len(log),"possible patterns found.")