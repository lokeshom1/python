MAX = 18
print(end='  ')
for column in range(1,MAX+1):
     print(end=' %2i' % column)
print()
print(end='   +')
for column in range(1,MAX+1):
     print(end='---')
print()

# Print Tables in the contents

for row in range(1,MAX+1):
     print(end=' %2i |' % row)
     for column in range(1,MAX+1):
          product = row*column;
          print(end=' %4i ' % product)
     print()
