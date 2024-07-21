#write a program using function to convert  fehrenheit to celsius 
def f_to_c(f):
    return 5*(f-32)/9

f=int(input("enter your fahrenheit degree: "))
c=f_to_c(f)
print(f"{round(c,2)} degree celsius")
