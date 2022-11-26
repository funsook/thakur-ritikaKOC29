number=int(input("Enter the number: "))
if number==0 or number==1:
  print(number,"=>neither prime nor composite")
else:
  for i in range(2,number):
    if(number%i==0):
      print(number,"=>composite number")
      break
    else:
      print(number,"prime number")