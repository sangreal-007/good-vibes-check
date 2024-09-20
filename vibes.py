# Write your code below this line 👇
print("Welcome to the Good Vibes Check!"+" "+"✨")
print ("I am here to check in on you and send some positive vibes your way.")
input("Press [Enter] to begin...")

# First Question
feeling = input("Do you feel good today? (yes/no/idk): ").lower()

if feeling == "yes":
    print("That´s awesome! Keep spreading those good vibes! 🌟")
    print("Remember, every day is an opportunity to do something great. 🚀")
    print("-"* 40) # Line Separator
elif feeling =="no":
    print("That´s okay. Not every day has to be perfect. 🌱")
    print("Take a deep breath, and remember, things will get better. You´ve got this! 💪")
    print("-"* 40) # Line Separator
elif feeling =="idk":
    print("It´s okay not to know how you feel sometimes. 💕")
    print("Take your time, reflect, and just be kind to yourself today. 💭")
    print("-"* 40) # Line Separator
else:
    print("Hmm, i didn't understand that, but i hope you feel good today! 🫶")
    print("-"* 40) # Line Separator

# Second Question
ambition = input("Do you have something you´re excited to work on today? (yes/no/maybe): ").lower()

if feeling == "yes":
    print("Fantastic! Go after it with everything you´ve got! 🌟")
    print("Progress, no matter how small, is still progress. Keep pushing forward! 🧨")
    print("-"* 40) # Line Separator
elif feeling == "no":
    print("That´s okay. Rest is important too! 🌷")
    print("Use today to recharge, and tomorrow you´ll be ready to tackle new goals! 🏅")
    print("-"* 40) # Line Separator
elif feeling == "maybe":
    print("That´s the spirit! Even a little bit of excitement can lead to great things! ✨")
    print("Take a small step, and see where it leads! Sometimes the smallest action sparks the biggest results. 🔥")
    print("-"* 40) # Line Separator
else:
    print("No worries! Just take it easy and focus on what makes you feel good. 🫂")
    print("-"* 40) # Line Separator

# Final Question
reflection = input("What´s something you´re grateful for today? (type anything): ").lower()
print(f"That´s wonderful! Being grateful for {reflection} is a beautiful way to stay positive. ✨")
print("Gratitude can turn ordinary moments into extraordinary blessings! 💌")
print("-" * 40)  # Line Separator
print("-" * 40)  # Line Separator
print("Thank you for joining the Good Vibes Check today. I believe in you, and hope, you have an amazing rest of the day! 🥰")
