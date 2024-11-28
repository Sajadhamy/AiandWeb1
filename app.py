import streamlit as st
import pandas as pd
import numpy as np

#Generate the random number persistent across guesses.
if "true_number" not in st.session_state:
    st.session_state.true_number = np.random.randint(0, 50)

#initialize the number of attempts
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

#title and instructions
st.title("Number Guessing Game")
st.write("I have a number in mind between 0 and 50. Can you guess it in 5 attempts?")
st.write("I will tell you if you need to guess higher or lower. I will also tell you how many attempts you have made.")

#user input
guess = st.number_input("Enter a number", min_value=0, max_value=50, value=None)

#Button to check the guess
if st.button("Check"):
    if guess is not None:
        #increment attempts
        st.session_state.attempts += 1
        #The difference between the guess and the true number
        diff = abs(guess - st.session_state.true_number)

        #check the conditions
        if guess == st.session_state.true_number:
            st.success(f"Congratulations! You guessed the number in {st.session_state.attempts} attempts.")
            st.session_state.attempts = 5 #end the game
        elif st.session_state.attempts >= 5:
            st.error(f"Sorry! You have exhausted all your attempts. The number was {st.session_state.true_number}")
        else:
            if diff <= 10:
                if guess < st.session_state.true_number:
                    st.warning(f"Almost there! Guess higher. You have made {st.session_state.attempts} attempts.")
                else:
                    st.warning(f"Almost there! Guess lower. You have made {st.session_state.attempts} attempts.")
            else:
                if guess < st.session_state.true_number:
                    st.error(f"Too far from the number, Guess higher! You have made {st.session_state.attempts} attempts.")
                else:
                    st.error(f"Too far from the number, Guess lower! You have made {st.session_state.attempts} attempts.")
    else:
        st.error("Please enter a valid input.")

#Button to restart the game
if st.button("Restart"):
    st.session_state.true_number = np.random.randint(0, 50)
    st.session_state.attempts = 0
    st.success("Game restarted! Guess the new number.")