#numbers of students

numbers = [4, 8, 15, 16, 23, 42]
print (min(numbers), max(numbers), (f"{sum(numbers)/len(numbers)}"))

def grade(marks,passing=50):
    if marks > passing:
        return "Pass"
    else:
        return "Fail"
print(grade(55))
print(grade(55,passing=60))
        