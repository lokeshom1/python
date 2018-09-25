print('###First exercise in Boolean condiitonal chapter ###')
integer=eval(input('Enter the range of the value:'))
if integer > 0 and integer < 100:
     print("OK")
else:
     print('')


print('###Second Exercise in the Boolean conditional ###')
integer=eval(input('Enter the range of the value:'))
if integer > 0 and integer < 100:
     print("OK")
else:
     print('Out Of Range')

print('###Third Exercise in the Boolean conditional ###')
day = eval(input('Enter the days in integer 0..6'))
if day == 0:
     print('Day is Sunday')
if day ==1:
     print('Day is Monday')
if day == 2:
     print('Day is Tuesday')
if day == 3:
     print('Day is Wednesday')
if day ==4:
     print('Day is Thursday')
if day == 5:
     print('Day is Friday')
if day ==6:
     print('Day is Saturday')
if day > 6:
     print('The Entered Day doesnot exists')
print('Done')

print('Same Boolean Conditional for days using ifelse')
day=eval(input('Enter the day in the integer b/w [0..6]: '))
if day == 0:
     print('Day is Sunday')
elif day ==1:
     print('Day is Monday')
elif day == 2:
     print('Day is Tuesday')
elif day == 3:
     print('Day is Wednesday')
elif day ==4:
     print('Day is Thursday')
elif day == 5:
     print('Day is Friday')
elif day ==6:
     print('Day is Saturday')
else:
     print('The Entered Day doesnot exists')
print('Done')
