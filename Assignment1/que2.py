marks=[]
count1,c2=0,0
for i in range(1,11):
    mark = int(input(f"Enter marks for student {i}: ")) #user input
    marks.append(mark)
print("List of Marks:", marks)
Highest_marks = max(marks)
Lowest_marks = min(marks)
print("Highest Marks:", Highest_marks)
print("Lowest Marks:", Lowest_marks)
Average = 0
for i in marks:
    Average += i
Average = Average / len(marks)
print("Average Marks:", Average)
for i in marks:
    
    if i>45 :
        count1+=1
    else:
        c2+=1
print("Number of Students Passed:", count1)
print("Number of Students Failed:", c2,)