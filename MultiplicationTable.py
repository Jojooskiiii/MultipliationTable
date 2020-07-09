###Papa Kojo Oseku-Afful
###97242022

###Multiplication Timetable

def main():
##Take input for user
    
    number = int(input("Enter the number for multiplication table: "))
    
##Print out the multiple the number
    
    print("The Multiplication Table of", number)
##Iterate 10 times from i  from 1-10
    
    for i in range(1, 11):
        print(number,"X",i,"=",number * i)
main()
