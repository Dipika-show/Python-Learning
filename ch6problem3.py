#a spam comment is defined as a text containing following keywords: "make a lot money", "buy now", "click this", "subscribe this". write a program to detect this spam
p1= "make a lot money"
p2= "buy now"
p3="click this"
p4="subscribe this"

comment=input("enter your comment:")
if((p1 in comment)or(p2 in comment)or(p3 in comment)
   or (p4 in comment)):
    print("this comment is a spam")
else:
    print("this comment is not a spam")
    