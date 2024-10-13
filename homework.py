
def linear_search(letters_list, target_letter):

    for letter in letters_list:
     
        if letter == target_letter:
            return True
 
    return False


letters = ['a', 'b', 'c', 'd', 'e']
target = 'c'

# Call the linear search function
if linear_search(letters, target):
    print(f"The letter '{target}' is in the list.")
else:
    print(f"The letter '{target}' is not in the list.")
