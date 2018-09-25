###Better Prompt Function#####
def prompt():
     value=int(input(print("Please enter an integer value : ")))
     return value
     
print("This program adds together 2 integers.")
value1=prompt()
value2=prompt()
sum = value1+value2;
print(value1, "+" , value2 , '=',sum)



def gcd(num1,num2):
     min = num1 if num1 < num2 else num2
     largestFactor = 1
     for i in range(1,min+1):
          if num1 % i == 0 and num2 % i ==0:
               largestFactor =i
     return largestFactor
factor=gcd(36,24)
print(factor)
  
