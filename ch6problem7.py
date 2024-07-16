#write a program to find out whether a given post is talking about "Dipika" or not

post =input("Enter your post:")
if("Dipika".lower() in post.lower()):
    print("this post is talking about dipika")
else:
    print("this post is not talking about dipika")

