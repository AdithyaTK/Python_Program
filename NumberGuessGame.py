import random
x=random.randrange(1,100)
count=0;
while(count!=5):
    guess=int(input("Enter the number:"))
    if guess==x:
        print("right guess")
        break
    else:
        print("wrong guess")
        if guess>x:
            print("The entered value is greater")
        else:
            print("The entered value is smalled")
    count=count+1
if(count==5):
    print("you failed...the number was",x)