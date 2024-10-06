numbers = [1,2,3,4,5,6,7,8,9,10]
print(numbers)

number_search = int(input("Enter the number you want searched: "))

found = False

for i in numbers:
    if number_search == i:
        print("Key Exists")
        found = True
        break


if found == False:
    print("key doens't Exist")    
    


