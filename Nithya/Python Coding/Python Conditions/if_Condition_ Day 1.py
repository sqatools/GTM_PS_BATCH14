print("****************25-11-2025********************")
print("Simple if Condition")

Today="Sunday"
day1="Monday"
day2="Tuesday"
day3="Wednesday"

if Today==day1:
    print("Today is a Holiday")
else:
    print("Today is a working day")
##########################################
print("*"*20)
Today="Sunday"
day1="Sunday"
day2="Tuesday"
day3="Wednesday"

if Today==day1:
    print("Today is a Holiday")
else:
    print("Today is a working day")
#######################################
print("*" * 20)
Leave = "0"
sick_leave = "1"
Weekend = "2"
Festval = "5"

if Leave == sick_leave:
    print("Take care")
elif Leave== Weekend:
    print("Enjoy your Weekend")
elif Leave== Festval:
    print("Enjoy your Vacation")
else:
    print("Today is a working day")

#######################################
print("*" * 20)
Leave = "2"
sick_leave = "1"
Weekend = "2"
Festval = "5"

if Leave == sick_leave:
    print("Take care")
elif Leave== Weekend:
    print("Enjoy your Weekend")
elif Leave== Festval:
    print("Enjoy your Vacation")
else:
    print("Today is a working day")
#######################################
print("*" * 20)
Leave = "5"
sick_leave = "1"
Weekend = "2"
Festval = "5"

if Leave == sick_leave:
    print("Take care")
elif Leave== Weekend:
    print("Enjoy your Weekend")
elif Leave== Festval:
    print("Enjoy your Vacation")
else:
    print("Today is a working day")

#######################################
print("*" * 20)
Apple="A+ve"
Bravo="B+ve"
Charlie="O+ve"
Blood_group= "A+ve"

if Blood_group==Apple:
    print("Apple is not matching")
    if Blood_group==Bravo:
        print("Bravo your is matching")
    else:
        print("We still need a donor")
    if Blood_group==Charlie:
        print("Charlie your is matching")
    else:
        print("We are at risk")
else:
    print("Find more help")

