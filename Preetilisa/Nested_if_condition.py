round1 =  "pass"
round2 =  "pass"
round3 = "pass"

if round1 == "pass":
    print("congrats 1st round is cleared")
    if round2 == "pass":
        print("congrats 2nd round is cleared")
        if round3 == "pass":
            print("congrats 3rd round is cleared")
            print("Congrats all rounds are cleared")
        else:
            print("failed in 3rd round, try next time")
    else:
        print("failed in 2nd round, try next time")
