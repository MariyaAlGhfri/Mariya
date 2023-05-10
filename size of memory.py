
#size of memory


memory =int(input("enter memory : "))
number_of_file=int(input("enter number of file: "))
file_size=int(input("enter file size: "))

size=number_of_file*file_size

if (size> memory):
  print("NO")

else:
  print("yes")