value = eval(input("Please enter an integer in the range 0...5 \n"))
if value < 0 :
     print("Value is too small")
else:
     if value ==0:
          print("zero")
     else:
          if value == 1:
               print("one")
          else:
               if value == 2:
                    print('Two')
               else:
                    if value == 3:
                         print('Three')
                    else:
                         if value == 4:
                              print("Four")
                         else:
                              if value == 5:
                                   print("Five")
                              else:
                                   print("Value is too Large")
print("Done")
