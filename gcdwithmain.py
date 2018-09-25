# Computes the greatest common divisor of m and n
def gcd(m,n):
     # Determine the smaller of m and n
     min = m if m < n else n
     largestFactor =1
     for i in range(1,min+1):
          if m % i == 0 and n % i == 0:
               largestFactor = i
     return largestFactor
#Get an integer from the user
def get_int():
     return int(input("Please enter an integer:"))

#Main Code to execute

def main():
     n1=get_int()
     n2=get_int()
     print("gcd(",n1,",",n2,") = ", gcd(n1,n2))
#Run the Program
main()
