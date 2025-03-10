import re
import streamlit as st

# Apply custom CSS for background and styling
st.markdown(
    """
    <style>

       .stApp > header {
    background-color: transparent;
}

        .stApp {
            background-color: #0d6471 !important;
            color: white !important;
            font-family: Arial, sans-serif;
        }
        /* Change label text color */
        label {
            color: white !important;
            font-size: 18px;
        }
        /* Change input text color */
        input {
            color: white !important;
            background-color: #216a74 !important;
            border-radius: 5px;
            padding: 8px;
            border: 1px solid white;
        }
        .password-box {
            font-size: 20px;
            font-weight: bold;
            background: #216a74;
            padding: 10px;
            border-radius: 5px;
            text-align: center;
            color: white;
        }
        .feedback {
            font-size: 16px;
            font-weight: bold;
            padding: 8px;
            border-radius: 5px;
            text-align: center;
            margin-top: 10px;
        }
        .strong {
            background-color: #28a745;
            color: white;
        }
        .moderate {
            background-color: #ffc107;
            color: black;
        }
        .weak {
            background-color: #dc3545;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def check_password_strength(password):
    score = 0
    feedback = []

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", "strong", feedback
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "moderate", feedback
    else:
        return "❌ Weak Password - Improve it using the suggestions below.", "weak", feedback

# Streamlit UI
st.title("🔒 Password Strength Checker")

password = st.text_input("Enter your password:", type="password")

if password:
    result, strength_class, feedback = check_password_strength(password)
    st.markdown(f"<div class='feedback {strength_class}'>{result}</div>", unsafe_allow_html=True)

    if feedback:
        for item in feedback:
            st.markdown(f"✅ {item}")

st.markdown("<br><small>Built with ❤ by <a href='https://github.com/safiaali926' style='color:white;'>Safia Ali</a></small>", unsafe_allow_html=True)
