#Marks of students 

marks = [88, 45, 92, 67, 30, 75]
#passed students

passed_students = [mark for mark in marks if mark > 50]
print("Passed students:", len(passed_students))

#Maximum and minimum marks
#jab ham aik hi line ma zayada entities perform karna chahte hain to hum f string ka use karte hain 
print(f"Highest: {max(marks)}, Lowest: {min(marks)}")

#Average marks
print(f"{sum(marks)/len(marks):.1f}")