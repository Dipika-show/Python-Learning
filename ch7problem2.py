'''write a program to greet all the person names stored in a list and starts with s
l=["dipika", "sneha","neha","sachin"]'''

l=["dipika", "sneha","neha","sachin"]

for name in l:
    if(name.startswith("s")):
        print(f"Hello {name}")
