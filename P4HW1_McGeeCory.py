# grade calculator
def main():

    grade = 0
    total = 0
    grade_list = []


    num= int(input("How many scores do you want to enter: "))

    for i in range(0, num) :
        grade = float(input("Enter score #" + str(i + 1) + ": "))
        while grade < 0 or grade >100:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            grade = int(input("Enter score #" + str(i + 1)+ ": "))
        grade_list.append(grade)
    lowest = min(grade_list)
    grade_list.remove(lowest)
    print("             Results           ")
    print("Lowest Score  :", format(lowest,',.1f'))
    print("Modified List :", grade_list)
    average = sum(grade_list)/ (num - 1)
    print("Scores Average:", format(average,',.2f'))
    if average > 90:
        grade = "A"
    elif average >= 80:
            grade = "B"
    elif average >= 70:
            grade = "C"
    elif average >= 60:
            grade = "D"
    else:
        grade = "F"
    print("Grade          : ", grade)


main()    
