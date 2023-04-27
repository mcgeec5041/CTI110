# CTI-110

   # P4HW2 - Salary Calculator

   # Cory McGee

   # Date 25 April 2023

   #
def main():
    overTimePay = 0
    numEmployees = 0
    totOverTimePay = 0
    totRegPay = 0
    totGrossPay = 0
    name = input("Enter employee's name or " + 'Done' + " to terminate:")
    while name != "Done":
        hours = float(input("How many hours did " + name + " work?"))
        payRate = float(input("What is " + name +"s pay rate:"))
        #calculate your pay and overtime pay then display



        if hours > 40:
            regPay = 40 * payRate
            overTime = hours - 40
            overTimePay = overtime * 1.5 * payRate
            grossPay = ovtpay + regPay
        else:
           regPay = hours * payRate
           grossPay = regPay
        print("Employee Name:" + name)
        print(hours)

        numEmployees = numEmployees + 1
        totOverTimePay = overTimePay + totOverTimePay
        totRegPay = totRegPay + regPay
        totGrossPay = totGrossPay + grossPay
        #print each employee
        print()
        name = input ("Enter employee's name or " + 'Done' + " to terminate:")
    print("Total number of employees entered:",numEmployees)

    print(totOverTimePay)
    print(totRegPay)
    print(totGrossPay)
    print()
    print("Program has terminated")
main()

