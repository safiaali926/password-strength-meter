import re
import random
import string
import streamlit as st

# Apply custom CSS for background and styling
st.markdown(
    """
   <style>
    /* Remove Streamlit's default app header background */
    .stApp > header {
        background-color: transparent !important;
    }

    /* Apply background color and styling */
    .stApp {
        background-color: #f0ffe8 !important;
        font-family: Arial, sans-serif;
        color: black !important;
    }

    /* Ensure label and form elements are visible */
    label, .css-16huue1, .css-1wbqyge, .css-1l02zno {
        font-size: 18px !important;
        color: black !important;
    }

    /* Fix input fields */
    input {
        color: black !important;
        background-color: white !important;
        border-radius: 5px;
        padding: 8px;
        border: 1px solid black;
    }

    /* Mobile Fix: Force Text & Input Visibility */
    @media screen and (max-width: 768px) {
        .stApp {
            background-color: #f0ffe8 !important;
        }
        label, input {
            color: black !important;
            background-color: white !important;
        }
    }

    /* Feedback messages */
    .feedback {
        font-size: 16px;
        font-weight: bold;
        padding: 8px;
        border-radius: 5px;
        text-align: center;
        margin-top: 10px;
    }

    .strong { background-color: #28a745; color: white; }
    .moderate { background-color: #ffc107; color: black; }
    .weak { background-color: #dc3545; color: white; }

    /* Button styling */
    .generate-btn {
        background-color: #a0db83;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px;
        text-align: center;
        cursor: pointer;
        display: inline-block;
    }

    .generate-btn:hover {
        background-color: #87c970;
    }

    /* Fix generated password text visibility */
    .generated-password {
        font-size: 18px;
        font-weight: bold;
        background: #a0db83;
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        margin-top: 10px;
        color: black !important;
    }
</style>
    """,
    unsafe_allow_html=True
)

# Blacklist of common weak passwords
BLACKLISTED_PASSWORDS = {"password123", "123456", "qwerty", "letmein", "admin", "welcome"}

# Function to generate a strong password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits  # 0-9
    if use_special:
        characters += string.punctuation # (!,@,#,$,%,&)
    return ''.join(random.choice(characters) for _ in range(length))

# Function to check password strength with custom weights
def check_password_strength(password):
    score = 0
    feedback = []

    # Check blacklist
    if password.lower() in BLACKLISTED_PASSWORDS:
        return "❌ This password is too common and easily guessable.", "weak", ["Choose a unique password."]

    # Custom weight scoring
    if len(password) >= 12:  # Stronger weight for longer passwords
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 2  # More weight for mixed-case
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 2  # More weight for special characters
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score >= 6:
        return "✅ Strong Password!", "strong", feedback
    elif score >= 4:
        return "⚠️ Moderate Password - Consider adding more security features.", "moderate", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions below.", "weak", feedback

# Streamlit UI
st.title("🔒 Password Strength Checker")

# User input for password check
password = st.text_input("🔑 Enter your password:", type="password")

if password:
    result, strength_class, feedback = check_password_strength(password)
    st.markdown(f"<div class='feedback {strength_class}'>{result}</div>", unsafe_allow_html=True)

    if feedback:
        for item in feedback:
            st.markdown(f"✅ {item}")

# Password Generator Section
st.title("🔐 Password Generator")

length = st.slider("📏 Select Password Length", min_value=6, max_value=32, value=12)
use_digits = st.checkbox("🔢 Include Digits")
use_special = st.checkbox("✨ Include Special Characters")

if st.button("🚀 Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.markdown(f"<div class='generated-password'>🔑 Generated Password: `{password}`</div>", unsafe_allow_html=True)

st.markdown("<br><small>Built with ❤ by <a href='https://github.com/safiaali926'>Safia Ali</a></small>", unsafe_allow_html=True)
