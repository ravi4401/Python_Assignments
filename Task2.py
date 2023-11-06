#1_Question
employees = [
    ("Vikram", 35, 8.75),
    ("Neha", 30, 12.50),
    ("Charlie", 50, 15.50),
    ("Rahul", 20, 7.00)
]
for i in employees:
    wage = i[1]*i[2]
    name = i[0]
    print(f"{name} has to be paid ${wage} for this week")










#2_Question

employees = [
    ("Vikram", 35, 8.75),
    ("Neha", 30, 12.50),
    ("Charlie", 50, 15.50),
    ("Rahul", 20, 7.00)
]

sum_of_all_wages = 0

for s in employees:
    hourly_wage = s[2]
    sum_of_all_wages= sum_of_all_wages+hourly_wage

Avg_wages = sum_of_all_wages/4
print("Average hourly wage: $",Avg_wages)

for n in employees:
    name = n[0]
    
    if n[1] > Avg_wages :
        print(f"{name} earns more than average")
    else:
        print(f"{name} earns less than average")



