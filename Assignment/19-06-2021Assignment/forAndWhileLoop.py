numbers = [1,2,3,4,5]
Weekdays = ['Monday', 'Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
Num = ['222','100','85','500','300']
Num =list(map(int,Num))
count=sum1=sum2=0

print("Using for loop:")
for i in numbers:
    print(i)

print("Using while loop")
while count<len(numbers):
    print(numbers[count])
    count+=1

count=0
print("Using for loop:")
for i in Weekdays:
    print(i)

print("Using while loop")
while count < len(Weekdays):
    print(Weekdays[count])
    count += 1

count=0
for i in Num :
    sum1+=i
print("The sum from for loop:",sum1)

while count < len(Num):
    sum2+=Num[count]
    count += 1
print("The sum from while loop:",sum2)