#Q2. Create a program that takes user input to add multiple elements to an array, then prints the final array

array = []
user = int(input("How many elements do you want to add to the array?\n"))

for _ in range(user):
    element = input("Enter an element to add to the array:  ")
    array.append(element)
print("final array: 2",array)