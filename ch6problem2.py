#write a program to find out whether a student has passed or failed if its require a total of 40% and at least 33% on each subjects to pass.Assume 3 subjects and take marks as input from the user

marks1=int(input("enter your marks1:"))
marks2=int(input("enter your marks2:"))
marks3=int(input("enter your marks3:"))

#check the total percentage

total_percentage= (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("you are passed",total_percentage)
else:
    print("you failed",total_percentage)


