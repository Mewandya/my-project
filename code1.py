total=0
count=0
number = input("Enter a number:")
while number !=0:
    total=total+number
    number=input("Enter a number:")
    count = count+1
print ("Sum: ",total)
print ("Count: ",(total/count))
