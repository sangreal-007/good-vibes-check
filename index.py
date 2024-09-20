import streamlit as st

# Welcome message
st.title("Good Vibes Check! ✨")
st.write("We’re here to check in on you and send some positive vibes your way.")

# Start interaction
st.write("Lets start...")

# First Question
feeling = st.text_input("Do you feel good today? (yes/no/idk):").lower()

# Display response based on the user's input
if feeling:
    if feeling == "yes":
        st.success("That’s awesome! Keep spreading those good vibes! 🌟")
        st.write("Remember, every day is an opportunity to do something great. 🚀")
        st.write("-" * 40)  # Line Separator
    elif feeling == "no":
        st.warning("That’s okay. Not every day has to be perfect. 🌱")
        st.write("Take a deep breath, and remember, things will get better. You’ve got this! 💪")
        st.write("-" * 40)  # Line Separator
    elif feeling == "idk":
        st.info("It’s okay not to know how you feel sometimes. 💕")
        st.write("Take your time, reflect, and just be kind to yourself today. 💭")
        st.write("-" * 40)  # Line Separator
    else:
        st.write("Hmm, I didn't understand that, but I hope you feel good today! 🫶")
        st.write("-" * 40)  # Line Separator

    # Second Question only after first question is answered
    ambition = st.text_input("Do you have something you're excited to work on today? (yes/no/maybe):").lower()

    # Display response based on the user's second input
    if ambition:
        if ambition == "yes":
            st.success("Fantastic! Go after it with everything you’ve got! 🌟")
            st.write("Progress, no matter how small, is still progress. Keep pushing forward! 🧨")
            st.write("-" * 40)  # Line Separator
        elif ambition == "no":
            st.warning("That’s okay. Rest is important too! 🌷")
            st.write("Use today to recharge, and tomorrow you’ll be ready to tackle new goals! 🏅")
            st.write("-" * 40)  # Line Separator
        elif ambition == "maybe":
            st.info("That’s the spirit! Even a little bit of excitement can lead to great things! ✨")
            st.write("Take a small step, and see where it leads! Sometimes the smallest action sparks the biggest results. 🔥")
            st.write("-" * 40)  # Line Separator
        else:
            st.write("No worries! Just take it easy and focus on what makes you feel good. 🫂")
            st.write("-" * 40)  # Line Separator

        # Final Question only after second question is answered
        reflection = st.text_input("What’s something you’re grateful for today?")

        if reflection:
            st.success(f"That’s wonderful! Being grateful for {reflection} is a beautiful way to stay positive. ✨")
            st.write("Gratitude can turn ordinary moments into extraordinary blessings! 💌")
            st.write("-" * 40)  # Line Separator
            st.write("Thank you for joining the Good Vibes Check today. I believe in you, and I hope you have an amazing rest of the day! 🥰")
