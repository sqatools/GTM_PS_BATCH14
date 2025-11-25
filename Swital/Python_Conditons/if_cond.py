print("#"*10, "Score Equality", "#"*10)
score_s1 = 40
score_s2 = 50

if score_s1 == score_s2:
    print("score are equal")
else:
    print("score are different")

print("#"*10, "Check Eligibility", "#"*10)
age = 27
experience = 3

if age >= 18 and experience >= 2:
    print("Eligible for the job")
elif age >= 18 and experience < 2:
    print("Need more experience")
else:
    print("Not eligible for the job")

print("#"*10, "Check Equal number", "#"*10)
s1 = 10
s2 = 20
s3 = 30
s4 = 10
if s1 == s2:
    print("s1 and s2 are equal")
elif s1 == s3:
    print("s1 and s3 are equal")
elif s1 == s4:
    print("s1 and s4 are equal")
else:
    print("All are different")

print("#"*10, "Marks which is equal and grade", "#"*10)
marks = 82

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")
