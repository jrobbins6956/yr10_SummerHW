#paste code here
name = input("What is your name >>>") #asking user for name and assigning it to 'name'

print("Do you know your times table?")
print()

number = int(input("Please enter a number >>>")) #asking user for a number and assigning it to 'number'
stop = int(input("Please enter the amount of times table you want displayed as an integer >>>")) #asking user for a number and assigning it to 'stop' 
print()


for table in range(stop+1): #repeat same number of times as repeats requested add one
    print("{0} times {1} = {2}".format(table,number,table*number)) #printing text with times table calculation

print("Now you know your times table {0}".format(name))#message to user  
