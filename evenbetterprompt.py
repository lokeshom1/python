def prompt(n):
     value = int(input("Please enter integer ", n , ":",sep=''))
     return value

print("This program adds together 2 integers")
value1= prompt(1)
value2 = prompt(2)
sum = value1 + value2
print(value1, "+", value2,"=" ,sum)
