# auth.py
import streamlit as st

# Simulating a simple dictionary for demo purposes (replace with a database in production)
user_data = {}

def login():
    st.title('Login Page')

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in user_data and user_data[username] == password:
            st.success("Login successful!")
            return username  # Return the username when login is successful
        else:
            st.error("Invalid credentials. Please try again.")
    return None

def signup():
    st.title('Signup Page')

    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")

    if st.button("Sign Up"):
        if new_username in user_data:
            st.error("Username already exists. Please choose a different username.")
        elif new_password != confirm_password:
            st.error("Passwords do not match.")
        else:
            user_data[new_username] = new_password
            st.success(f"Account created for {new_username}! Please login to proceed.")

