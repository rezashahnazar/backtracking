# Doctor shifts
A python project using backtracking and recursion.

In this repository, there are several small projects, resembling basic structures of the final Shift Scheduler Project.

"DoctorShifts.py" is the main project.
It starts with an empty table of a 30 day month. Each day has 3 positions which should be filled. We should fill each cell with one of the 18 docors. in a way that:

1. No one should be placed in two positions in the same day. 
2. No one should have shifts for more than 24 hours consequently. 
3. No one should be placed in a shift position (the same column) more than 2 times in the month.
4. Each doctor (of 18) should have a total of 5 shifts in the 30 days of the month (18 times 5 = 30 times 3 = 90).
5. Shifts for each doctor should be evenly distributed throughout the month.

Tkinter library is used to make a GUI for showing the final schedule in a formatted table. "GUI.py" loads "DoctorShifts.py" at first, then handles Tkinter codes to produce the GUI.