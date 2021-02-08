import DoctorShifts
from tkinter import *

class Table: 
      
    def __init__(self,root): 
          
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = Entry(root, width=10, fg='white', 
                               font=('Arial',16,'bold'), justify='center') 
                  
                self.e.grid(row=i, column=j) 
                self.e.insert(END, list[i][j])

list= [['ER1', 'ER2', 'CCU']] + DoctorShifts.table
for x in range(31):
    if x ==0 :
        list[x].insert(0,"Days")
    else:
        list[x].insert(0,x)
        


# find total number of rows and 
# columns in list 
total_rows = len(list) 
total_columns = len(list[0])

root = Tk()
t = Table(root)
root.mainloop()