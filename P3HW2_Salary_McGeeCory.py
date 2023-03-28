 # CTI-110

   # P3HW2 - Salary

   # Cory McGee

   # Date 23 March 2023

   #
   
name = input ('Enter name of employee:')
hours = float (input( "Enter number of hours: "))
payrate = float(input("Enter employee's pay rate:" ))            
print('-'*38)
ovthrs= 0.0
ovtpay= 0.0
if hours > 40:
    regpay = payrate * 40
    ovthrs = hours -40
    ovtpay = payrate * ovthrs*1.5
    grosspay = ovtpay + regpay
else:
    grosspay = hours * payrate
print( 'Employee name: ',name)

print()
print("Hours Worked"+"  "*5+"Pay Rate"+"  "*5+"OverTime" +" "*5+"OverTime Pay"+"  "*5+"RegHour Pay"+" "*5 +"Gross Pay")
print('------------------------------------------------------------------------------------------------------------------')

print ( hours, '\t\t\t' ,payrate, '\t\t' ,ovthrs,'\t\t'+' $' + str(format(ovtpay, ',.2f'))+ '\t' +'   $' + str(format(regpay, ',.2f')) + '\t' +  '  $' + str(format(grosspay,',.2f')))
