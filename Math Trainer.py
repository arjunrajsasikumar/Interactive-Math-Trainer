import random
import csv
import math

#Variables

score = 0
streak = 0
best_streak = 0
oneadds = 0
oneaddm = 0
twoadds = 0
twoaddm = 0
threeadds = 0
threeaddm = 0
onesubs = 0
onesubm = 0
twosubs = 0
twosubm = 0
threesubs = 0
threesubm = 0
onemultis = 0
onemultim = 0
twomultis = 0
twomultim = 0
threemultis = 0
threemultim = 0
onedivis = 0
onedivim =0
twodivis = 0
twodivim = 0
threedivis = 0
threedivim = 0
onesqrroots = 0
onesqrrootm = 0
twosqrroots = 0
twosqrrootm = 0
threesqrroots = 0
threesqrrootm = 0
onepows = 0
onepowm = 0
addlst = ["Add","add"]
sublst = ["Sub","sub"]
multilst = ["Multi","multi"]
divilst = ["Divi","divi"]
sqrrootlst = ["Sqrroot","sqrroot"]
powlst = ["Pow","pow"]

# Defining the Functions

def onemulti():
    global score
    global streak
    global best_streak
    global onemultis
    global onemultim
    fnum = random.randint(1, 9)
    snum = random.randint(1, 9)
    print(fnum, "*", snum, "=?")
    usr_ans = int(input("Enter the answer:"))
    if usr_ans == fnum * snum:
        print("Congratulation You Got The Correct Answer")
        score += 1
        onemultis += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", fnum * snum)
        streak *= 0
        onemultim += 1


def twomulti():
    global score
    global streak
    global best_streak
    global twomultis
    global twomultim
    fnum = random.randint(10, 99)
    snum = random.randint(10, 99)
    print(fnum, "*", snum, "=?")
    usr_ans = int(input("Enter the answer:"))
    if usr_ans == fnum * snum:
        print("Congratulation You Got The Correct Answer")
        score += 1
        twomultis += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", fnum * snum)
        streak *= 0
        twomultim += 1



def threemulti():
    global score
    global streak
    global best_streak
    global threemultis
    global threemultim
    fnum = random.randint(100, 999)
    snum = random.randint(100, 999)
    print(fnum, "*", snum, "=?")
    usr_ans = int(input("Enter the answer:"))
    if usr_ans == fnum * snum:
        print("Congratulation You Got The Correct Answer")
        score += 1
        threemultis += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", fnum * snum)
        streak *= 0
        threemultim += 1


def oneadd():
    global score
    global streak
    global best_streak
    global oneadds
    global oneaddm
    fnum = random.randint(1, 9)
    snum = random.randint(1, 9)
    print(fnum, "+", snum, "=?")
    usr_ans = int(input("Enter the answer:"))
    if usr_ans == fnum + snum:
        print("Congratulation You Got The Correct Answer")
        score += 1
        oneadds += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", fnum + snum)
        streak *= 0
        oneaddm += 1


def threeadd():
    global score
    global streak
    global best_streak
    global threeadds
    global threeaddm
    fnum = random.randint(100, 999)
    snum = random.randint(100, 999)
    print(fnum, "+", snum, "=?")
    usr_ans = int(input("Enter the answer:"))
    if usr_ans == fnum + snum:
        print("Congratulation You Got The Correct Answer")
        score += 1
        threeadds += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", fnum + snum)
        streak *= 0
        threeaddm += 1


def twoadd():
    global score
    global streak
    global best_streak
    global twoadds
    global twoaddm
    fnum = random.randint(10, 99)
    snum = random.randint(10, 99)
    print(fnum, "+", snum, "=?")
    usr_ans = int(input("Enter the answer:"))
    if usr_ans == fnum + snum:
        print("Congratulation You Got The Correct Answer")
        score += 1
        twoadds += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", fnum + snum)
        streak *= 0
        twoaddm += 1


def onesub():
    global score
    global streak
    global best_streak
    global onesubs
    global onesubm
    fnum = random.randint(1, 9)
    snum = random.randint(1, 9)
    print(fnum, "-", snum, "=?")
    usr_ans = int(input("Enter the answer:"))
    if usr_ans == fnum - snum:
        print("Congratulation You Got The Correct Answer")
        score += 1
        onesubs += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", fnum - snum)
        streak *= 0
        onesubm += 1


def twosub():
    global score
    global streak
    global best_streak
    global twosubs
    global twosubm
    fnum = random.randint(10, 99)
    snum = random.randint(10, 99)
    print(fnum, "-", snum, "=?")
    usr_ans = int(input("Enter the answer:"))
    if usr_ans == fnum - snum:
        print("Congratulation You Got The Correct Answer")
        score += 1
        twosubs += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", fnum - snum)
        streak *= 0
        twosubm += 1


def threesub():
    global score
    global streak
    global best_streak
    global threesubs
    global threesubm
    fnum = random.randint(100, 999)
    snum = random.randint(100, 999)
    print(fnum, "-", snum, "=?")
    usr_ans = int(input("Enter the answer:"))
    if usr_ans == fnum - snum:
        print("Congratulation You Got The Correct Answer")
        score += 1
        threesubs += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", fnum - snum)
        streak *= 0
        threesubm += 1

def onepow():
    global score
    global streak
    global best_streak
    global onepows
    global onepowm
    fnum = random.randint(1, 9)
    snum = random.randint(1, 9)
    print(fnum, "^", snum, "=?")
    usr_ans = int(input("Enter the answer:"))
    if usr_ans == fnum**snum:
        print("Congratulation You Got The Correct Answer")
        score += 1
        onepows += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", fnum**snum)
        streak *= 0
        onepowm += 1






def onesqrroot():
    global score
    global streak
    global best_streak
    global onesqrroots
    global onesqrrootm
    fnum = random.randint(1, 9)
    print("Square root of ",fnum, "=?")
    usr_ans = float(input("Enter the answer:"))
    if usr_ans == round(math.sqrt(fnum),2):
        print("Congratulation You Got The Correct Answer")
        score += 1
        onesqrroots += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", round(math.sqrt(fnum),2))
        streak *= 0
        onesqrrootm += 1



def twosqrroot():
    global score
    global streak
    global best_streak
    global twosqrroots
    global twosqrrootm
    fnum = random.randint(10, 99)
    print("Square root of ",fnum, "=?")
    usr_ans = float(input("Enter the answer:"))
    if usr_ans == round(math.sqrt(fnum),2):
        print("Congratulation You Got The Correct Answer")
        score += 1
        twosqrroots += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", round(math.sqrt(fnum),2))
        streak *= 0
        twosqrrootm += 1



def threesqrroot():
    global score
    global streak
    global best_streak
    global threesqrroots
    global threesqrrootm
    fnum = random.randint(100, 999)
    print("Square root of ",fnum, "=?")
    usr_ans = float(input("Enter the answer:"))
    if usr_ans == round(math.sqrt(fnum),2):
        print("Congratulation You Got The Correct Answer")
        score += 1
        threesqrroots += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", round(math.sqrt(fnum),2))
        streak *= 0
        threesqrrootm += 1


def onedivi():
    global score
    global streak
    global best_streak
    global onedivis
    global onedivim
    fnum = random.randint(1, 9)
    snum = random.randint(1, 9)
    print(fnum, "/", snum, "=?")
    usr_ans = float(input("Enter the answer:"))
    if usr_ans == round(fnum/snum,2):
        print("Congratulation You Got The Correct Answer")
        score += 1
        onedivis += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", round(fnum/snum,2))
        streak *= 0
        onedivim += 1

def twodivi():
    global score
    global streak
    global best_streak
    global twodivis
    global twodivim
    fnum = random.randint(10, 99)
    snum = random.randint(10, 99)
    print(fnum, "/", snum, "=?")
    usr_ans = float(input("Enter the answer:"))
    if usr_ans == round(fnum/snum,2):
        print("Congratulation You Got The Correct Answer")
        score += 1
        twodivis += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", round(fnum/snum,2))
        streak *= 0
        twodivim += 1

def threedivi():
    global score
    global streak
    global best_streak
    global threedivis
    global threedivim
    fnum = random.randint(100, 999)
    snum = random.randint(10, 999)
    print(fnum, "/", snum, "=?")
    usr_ans = float(input("Enter the answer:"))
    if usr_ans == round(fnum/snum,2):
        print("Congratulation You Got The Correct Answer")
        score += 1
        threeivis += 1
        streak += 1
        if streak >= best_streak:
            best_streak = streak
    else:
        print("Hard luck, the correct answer is", round(fnum/snum,2))
        streak *= 0
        threedivim += 1


# Starting of the Program

print(
    "-----------------------------------------------------------------------------------------------------------------")
print(
    "                                                      WELCOME                                                    ")
print(
    "-----------------------------------------------------------------------------------------------------------------")
print("Type Multi to practice Multiplication,Type Add for Addition, Sub for Subtraction, Pow for Power, Sqrroot for Square Root")
Continue = "Yes"
while Continue=="Yes" or Continue=="yes":
    print(
        "-----------------------------------------------------------------------------------------------------------------")
    print(
        "                                                      CHOICE                                                     ")
    print(
        "-----------------------------------------------------------------------------------------------------------------")
    print("Type Multi to practice Multiplication,Type Add for Addition, Sub for Subtraction,Pow for Power, Sqrroot for Square Root , Divi for Division")
    choice = input("Enter your choice: ")
    while choice == "Add" or choice == "add":
        print(
            "-------------------------------------------------------------------------------------------------------------")
        print(
            "                                                  ADDITION                                                   ")
        print(
            "-------------------------------------------------------------------------------------------------------------")
        usr_cho = int(input("Type 1 to practice one digit Addition, 2 for two digit and 3 for three digit: "))
        if usr_cho == 1:
            oneadd()
            choice = input("Do you want to continue doing Addition? Type Add to continue or No to stop:")
        elif usr_cho == 2:
            twoadd()
            choice = input("Do you want to continue doing Addition? Type Add to continue or No to stop:")
        elif usr_cho == 3:
            threeadd()
            choice = input("Do you want to continue doing Addition? Type Add to continue or No to stop:")
        else:
            print("Invalid")
        if choice not in addlst:
            Continue=input("Do you want to practice other operations? Type Yes to Continue or Type No to stop:")
    while choice == "Multi" or choice == "multi":
        print(
            "-------------------------------------------------------------------------------------------------------------")
        print(
            "                                                  MULTIPLICATION                                             ")
        print(
            "-------------------------------------------------------------------------------------------------------------")
        usr_cho = int(input("Type 1 to practice one digit multiplication, 2 for two digit and 3 for three digit: "))
        if usr_cho == 1:
            onemulti()
            choice = input("Do you want to continue doing Multiplication? Type Multi to continue or No to stop:")
        elif usr_cho == 2:
            twomulti()
            choice = input("Do you want to continue doing Multiplication? Type Multi to continue or No to stop:")
        elif usr_cho == 3:
            threemulti()
            choice = input("Do you want to continue doing Multiplication? Type Multi to continue or No to stop:")
        else:
            print("Invalid")
        if choice not in multilst:
            Continue=input("Do you want to practice other operations? Type Yes to Continue or Type No to stop:")
        
    while choice == "Sub" or choice == "sub":
        print(
            "-------------------------------------------------------------------------------------------------------------")
        print(
            "                                                  SUBTRACTION                                                ")
        print(
            "-------------------------------------------------------------------------------------------------------------")
        usr_cho = int(input("Type 1 to practice one digit Subtraction, 2 for two digit and 3 for three digit: "))
        if usr_cho == 1:
            onesub()
            choice = input("Do you want to continue doing subtraction? Type Sub to continue or No to stop:")
        elif usr_cho == 2:
            twosub()
            choice = input("Do you want to continue doing subtraction? Type Sub to continue or No to stop:")
        elif usr_cho == 3:
            threesub()
            choice = input("Do you want to continue doing subtraction? Type Sub to continue or No to stop:")
        else:
            print("Invalid")
        if choice not in sublst:
            Continue=input("Do you want to practice other operations? Type Yes to Continue or Type No to stop:")
    
    while choice == "Pow" or choice == "pow":
        print(
            "-------------------------------------------------------------------------------------------------------------")
        print(
            "                                                  POWER                                                   ")
        print(
            "-------------------------------------------------------------------------------------------------------------")
        onepow()
        choice = input("Do you want to continue doing Power? Type Pow to continue or No to stop:")
        if choice not in powlst:
            Continue=input("Do you want to practice other operations? Type Yes to Continue or Type No to stop:")
    
    while choice == "Sqrroot" or choice == "sqrroot":
        print(
            "-------------------------------------------------------------------------------------------------------------")
        print(
            "                                                  SQUARE ROOT                                                   ")
        print(
            "-------------------------------------------------------------------------------------------------------------")
        print("                                Round off to the first two decimal places                                  ")
        usr_cho = int(input("Type 1 to practice one digit Square root, 2 for two digit and 3 for three digit: "))
        if usr_cho == 1:
            onesqrroot()
            choice = input("Do you want to continue doing Square Root? Type Sqrroot to continue or No to stop:")
        elif usr_cho == 2:
            twosqrroot()
            choice = input("Do you want to continue doing Square Root? Type Sqrroot to continue or No to stop:")
        elif usr_cho == 3:
            threesqrroot()
            choice = input("Do you want to continue doing Square Root? Type Sqrroot to continue or No to stop:")
        else:
            print("Invalid")
        if choice not in sqrrootlst:
            Continue=input("Do you want to practice other operations? Type Yes to Continue or Type No to stop:")
        
    while choice == "Divi" or choice == "divi":
        print(
            "-------------------------------------------------------------------------------------------------------------")
        print(
            "                                                  DIVISION                                                   ")
        print(
            "-------------------------------------------------------------------------------------------------------------")
        print("                                   Round off to the first two decimal places                               ")
        usr_cho = int(input("Type 1 to practice one digit Division, 2 for two digit and 3 for three digit: "))
        if usr_cho == 1:
            onedivi()
            choice = input("Do you want to continue doing Division? Type Divi to continue or No to stop:")
        elif usr_cho == 2:
            twodivi()
            choice = input("Do you want to continue doing Division? Type Divi to continue or No to stop:")
        elif usr_cho == 3:
            threedivi()
            choice = input("Do you want to continue doing Division? Type Divi to continue or No to stop:")
        else:
            print("Invalid")
        if choice not in divilst:
            Continue=input("Do you want to practice other operations? Type Yes to Continue or Type No to stop:")
print(
    "-----------------------------------------------------------------------------------------------------------------")
print(
    "                                                      SCORE                                                      ")
print(
    "-----------------------------------------------------------------------------------------------------------------")
print("Your final score is:", score)
print("Your best streak was:", best_streak)
print(
    "-----------------------------------------------------------------------------------------------------------------")
print(
    "                                                THANK YOU FOR PLAYING!                                           ")
print(
    "-----------------------------------------------------------------------------------------------------------------")

#Totals

oneaddtotal = oneadds+oneaddm
twoaddtotal = twoadds+twoaddm
threeaddtotal = threeadds+threeaddm
onesubtotal = onesubs+onesubm
twosubtotal = twosubs+twosubm
threesubtotal = threesubs+threesubm
onemultitotal = onemultis+onemultim
twomultitotal = twomultis+twomultim
threemultitotal = threemultis+threemultim
onedivitotal = onedivis+onedivim
twodivitotal = twodivis+twodivim
threedivitotal = threedivis+threedivim
onepowtotal = onepows+onepowm
onesqrroottotal = onesqrroots+onesqrrootm
twosqrroottotal = twosqrroots+twosqrrootm
threesqrroottotal = threesqrroots+threesqrrootm

#Importing to CSV

file = open("Math Statistics.csv", "w", newline='')
cw = csv.writer(file)
addfields = ["No. of Single digit addition attempted","Correct","Wrong","No. of Double digit addition attempted","Correct","Wrong","No. of Triple digit addition attempted","Correct","Wrong"]
cw.writerow(addfields)
addrows = [oneaddtotal,oneadds,oneaddm,twoaddtotal,twoadds,twoaddm,threeaddtotal,threeadds,threeaddm]
cw.writerow(addrows)
subfields = ["No. of Single digit subtraction attempted","Correct","Wrong","No. of Double digit subtraction attempted","Correct","Wrong","No. of Triple digit subtraction attempted","Correct","Wrong"]
cw.writerow(subfields)
subrows = [onesubtotal,onesubs,onesubm,twosubtotal,twosubs,twosubm,threesubtotal,threesubs,threesubm]
cw.writerow(subrows)
multifields = ["No. of Single digit multiplication attempted","Correct","Wrong","No. of Double digit multiplication attempted","Correct","Wrong","No. of Triple digit multipication attempted","Correct","Wrong"]
cw.writerow(multifields)
multirows = [onemultitotal,onemultis,onemultim,twomultitotal,twomultis,twomultim,threemultitotal,threemultis,threemultim]
cw.writerow(multirows)
divifields = ["No. of Single digit division attempted","Correct","Wrong","No. of Double digit division attempted","Correct","Wrong","No. of Triple digit division attempted","Correct","Wrong"]
cw.writerow(divifields)
divirows = [onedivitotal,onedivis,onedivim,twodivitotal,twodivis,twodivim,threedivitotal,threedivis,threedivim]
cw.writerow(divirows)
powfields = ["No. of Single digit power attempted","Correct","Wrong"]
cw.writerow(powfields)
powrows = [onepowtotal,onepows,onepowm]
cw.writerow(powrows)
sqrrootfields = ["No. of Single digit square root attempted","Correct","Wrong","No. of Double digit square root attempted","Correct","Wrong","No. of Triple digit square root attempted","Correct","Wrong"]
cw.writerow(sqrrootfields)
sqrrootrows = [onesqrroottotal,onesqrroots,onesqrrootm,twosqrroottotal,twosqrroots,twosqrrootm,threesqrroottotal,threesqrroots,threesqrrootm]
cw.writerow(sqrrootrows)
streak_score_fields = ["Score","Best Streak"]
cw.writerow(streak_score_fields)
streak_score_rows = [score, best_streak]
cw.writerow(streak_score_rows)
file.close()



