#Nested if condition
round1="pass"
round2="pass"
round3="pass"

if round1=="pass":
    print("You have cleared the 1st round")
    if round2=="pass":
        print("You have cleared the 2nd round")
        if round3=="pass":
            print("You have cleared the 3rd round")
        else:
            print("You have not cleared the 3rd round")
    else:
        print("You have not cleared the 2nd round")

else:
    print("You have not cleared the 1st round, try next time")

print("======"*50)
#===============================================================
#Number properties checker
num=10
if num>0:
    print("Number is +ve")

else:
    print("Number is -ve")
