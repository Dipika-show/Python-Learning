#write a python program to convert inch into cms
def inch_to_cms(inch):
    return inch*2.54

n=int(input("Enter your inch value: "))

print(f"the value in cms is {inch_to_cms(n)}")
