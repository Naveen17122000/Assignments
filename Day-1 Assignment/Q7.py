#Q7 Create a program that prints the multiplication table of a given number using a while loop.

number = int(input("Enter a number:"))

i = 1

while i<=10:
    print(f"{number} * {i} = {i*number}")

    i+=1
