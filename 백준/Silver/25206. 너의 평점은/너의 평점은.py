dic_grade = {"A+" : 4.5,
             "A0" : 4.0,
             "B+" : 3.5,
             "B0" : 3.0,
             "C+" : 2.5,
             "C0" : 2.0,
             "D+" : 1.5,
             "D0" : 1.0,
             "F"  : 0.0
            }

sum_credit = 0
mul_grade = 0

for i in range (20) :
    sub, credit, grade = map(str, input().split())
    credit = float(credit)

    if grade == "P" :
        continue
        
    sum_credit += credit
    mul_grade += credit * dic_grade[grade]

print(mul_grade / sum_credit)