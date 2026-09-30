print("Hello! I am AI Bot. What's your name? : ")
name = input()
print(f"Nice to meet you, {name}")
print("How are you feeling today? (good/bad)")
mood = input().lower()

if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm so sorry to hear that. Hope things get better soon.")
else:
    print("I see. Sometimes it's hard to put feeling into words.")

print("What is your favourite colour?")
colour = input().lower()

if  colour == "red":
    print(f"I like {colour}")
elif colour == "blue":
    print(f"I love the colour {colour}")
else:
    print(f"{colour} is my favourite colour too!")

print(f"It was nice chatting with you {name}. Goodbye!")
