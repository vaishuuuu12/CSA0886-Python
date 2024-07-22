name=input("Enter the student's name:")
reg_no=input("Enter the student's register number:")
marks=[]
for i in range(1,6):
    marks.append(float(input(f"Enter mark for subject {i}:")))
total_marks=sum(marks)
print("\n Student Marks Sheet:")
print(f"Name:{name}")
print(f" Register number:{reg_no}")
print(f"Marks:{marks}")
print(f"Total marks:{total_marks}")

           
