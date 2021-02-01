table = [
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
 
docs = {
    1:'A',
    2:'B',
    3:'C',
    4:'D',
    5:'E',
    6:'F',
    7:'G',
    8:'H',
    9:'I',
    10:'J',
    11:'K',
    12:'L',
    13:'M',
    14:'N',
    15:'O',
    16:'P',
    17:'Q',
    18:'R'
}

cNum={
    1:0,
    2:0,
    3:0,
    4:0,
    5:0,
    6:0,
    7:0,
    8:0,
    9:0,
    10:0,
    11:0,
    12:0,
    13:0,
    14:0,
    15:0,
    16:0,
    17:0,
    18:0
}

# the main function which fills the table
def solve(tb):
    find = find_empty(tb)
    if not find:
        return True
    else:
        row, col = find

    #finding the least used numbers respectively to use in loop
    countAll(tb)
    cnList=sorted(cNum, key=cNum.get, reverse=False)

    # in order to choose the least used number each time, insted of :
    # for i in range(1,19):
    #     if valid(tb, i, (row, col)):
    #         tb[row][col] = i
    #         if solve(tb):
    #             return True
    #         tb[row][col] = 0
    # return False
    
    for i in range(0,18):
        if valid(tb, cnList[i], (row, col)):
            tb[row][col] = cnList[i]
            if solve(tb):
                return True
            tb[row][col] = 0
    return False

# finding the next empty cell in the table
def find_empty(tb):
    for i in range(len(tb)):
        for j in range(len(tb[0])):
            if tb[i][j] == 0:
                return (i, j) # it returns row and collumn respectively
    return None


# the function which check all validation criterias before inserting a number
def valid(tb, num, pos):
    # check maximum shifts
    if counter(tb,num) > 4:
        return False  
            
    # Checking the same day to avoid repeating
    for i in range(len(tb[0])):
        if tb[pos[0]][i] == num: #and pos[1] != i:
            return False   
    
    # Check to avoid useing a number more than 2 times in a column
    if countCol(tb,num, pos) > 2:
        # print(pos[0],'---',pos[1],'---',tb[pos[0]],'---',num,'---',countCol(tb,num, pos))
        # print('--------')
        return False
    
    # check the day before and after to avoid 48hour shifts
    for i in range(len(tb[0])):
        if pos[0] != 0:  
            if tb[(pos[0])-1][i] == num:
                return False
        elif pos[0] < (len(tb)-1):
            if tb[(pos[0])+1][i] == num:
                return False
    
    return True



# printing the table in the desired pattern
def printTab(tb):
    for i in range(len(tb)):
        if i % 10 == 0 and i != 0:
             print("- - - - - - - - - - - - - ")
        for j in range(len(tb[0])):
            if j == 2:
                print(tb[i][j])
            else:
                print(str(tb[i][j]) + " ", end="")



# counting the number of times a specific person is placed in the table
def counter (tb, num):
    counter=0
    for i in range(0,len(tb)):
        counter += tb[i].count(num)
    return counter

# counting the number of times a person is placed in the same column
def countCol(tb, num, pos):
    counter=1
    for i in range(len(tb)):
        if tb[i][pos[1]] == num:
            counter += 1
    return counter

# counting how many times each number is used
# and putting the result in cNum dictionart
def countAll(tb):
    for i in range(1,19):
        cNum[i]=counter(tb,i)



printTab(table) #before solving
solve(table)
print("___________________")
printTab(table) #after solving

# translating doctor numbers of the solved table to their specified letters 
# as mentioned in the 'docs' dictionary
for i in range(len(table)):
    for j in range(len(table[0])):
        table[i][j]=str(docs[table[i][j]])

print("___________________")
printTab(table) # by letters 