def prompt():
     print("Please enter an integer value : ",end='')

print("This program adds together 2 integers.")
prompt()
value1=int(input())
prompt()
value2=int(input())
sum = value1+value2;
print(value1, "+" , value2 , '=',sum)


###Counting the numbers till 10 #####

print('Counting the numbers till 10')

def count_to_10():
     for i in range(1,11):
          print(i)
print("Going to count to ten")
count_to_10()
print("Going to count to ten again")
count_to_10()


###Counting the number till n ######

def count_to_n(n):
     for i in range(1,n+1):
          print(i)
print("Going to count to ten....")
count_to_n(10);
print("Going to count to five....")
count_to_n(5)

###Better Prompt Function#####
def prompt():
     value=int(input(print("Please enter an integer value : ")))
     return value
     
print("This program adds together 2 integers.")
value1=prompt()
value2=prompt()
sum = value1+value2;
print(value1, "+" , value2 , '=',sum)


