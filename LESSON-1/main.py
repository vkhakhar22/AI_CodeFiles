print("Hello I am AI")

name=input("Enter your name:Va")
print("nice to meet you",name,"!")
print("how are you feeling today?(good/bad)")
mood=input().lower()
if mood=="good":
    print("Glad to hear that")
elif mood=="bad":
    print("Sorry to hear that.Hope things get better soon")
else:
    print("I see")

print("It was nice chatting with you",name,"Goodbye!")
