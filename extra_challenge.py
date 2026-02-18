# Ask the user to enter 5 numbers and store them in a list
# Print the list in reverse order
# Calculate the average of the numbers in the list
# Count how many numbers are greater than 10
# Create a function that checks if a number is prime
# Use the function to test every number in the list
# Create a dictionary where each number maps to its square
# Print the dictionary in a clean sentence format
# Use a loop to find the smallest number in the list
# Create a new list that only keeps even numbers
# Sort the new list from smallest to largest
# Write the results into a text file called results.txt
# Read the file and print its contents to the screen
# Handle errors if the file does not exist
# Create a menu that lets the user choose which task to run
numlist = []
print("i want five numbers! gimme.")
for i in range(5):
    num = int(input(f"num {i+1} of 5:\n"))
    numlist.append(num)
print(f"so you've chosen {numlist}.")
sum = numlist[0] + numlist[1] + numlist[2] + numlist[3] + numlist[4]
average = sum/5
#i am unsure how to check if a number is a prime as of yet, so i will substitute with the method to check whether a number
#is even or odd.
def evenodd():
    for i in range(len(numlist)):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd.")
    print(f"the average of this would be {average}")
ans = input(f"wanna check what's even or odd?")
if ans == "yes":
    evenodd()
else:
    print(f"ok well either you didnt put specifically 'yes' or you said no, so i guess not haha!")
#time has run out, this is far as i got. once more i did not need to look anything up- much of this could be done cleaner,
#but clean is not my style! -justin miller