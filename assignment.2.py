#QUESTION-1

employees = [("Vikram", 35, 8.75),("Neha", 30, 12.50),("Charlie", 50, 15.50),("Rahul", 20, 7.00)]
for j in employees:
    empl=j[0]
    salary=j[1]*j[2]
    print(f"{empl} has to be paid ${salary} for this week" )

#question-2

employees = [("Vikram", 35, 8.75),("Neha", 30, 12.50),("Charlie", 50, 15.50),("Rahul", 20, 7.00)]
a=0
for j in employees:
    wage=j[2]
    a=a+wage
avg=a/4
print(avg)
avg=avg
for k in employees:
    
    if k[2]>avg:
        print (f"{k[0]} earns more than the average")
    else: 
        print(f"{k[0]} earns less than the average")