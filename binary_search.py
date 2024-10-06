numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

key = int(input("Enter the number you want searched: "))

found = False
start = 0
end = len(numbers) - 1

while start <= end:
    midpoint = (start+end)//2
    if numbers[midpoint] == key:
        print("Key Exists")
        found = True
        break
    elif numbers[midpoint] > key:
        end = midpoint - 1
    else:
        start = midpoint + 1    


if found == False:
    print("Key doesn't Exist")
  
