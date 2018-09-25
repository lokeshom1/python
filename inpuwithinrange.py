def get_int_in_range(first,last):
     if first > last:
          first,last = last, first
     in_value = int(input("Please enter values in the range " \
                          + str(first) + "...."+ str(last) + ":"))
     while in_value < first or in_value > last:
          print(in_value, "is not in the range",first,"....",last)
          in_value=int(input("Please try again:"))
     return in_value;
def main():
     print(get_int_in_range(10, 20))
     print(get_int_in_range(20, 10))
     print(get_int_in_range(5,5))
     print(get_int_in_range(-100, 100))

main()
