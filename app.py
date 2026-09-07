import streamlit as st
from google import genai

client = genai.Client()

st.title("AI Message Helper")
st.write("Turn a rough message into a clearer version with the tone you choose.")

message = st.text_area("Enter your message here:")

tone = st.selectbox("Select the tone of the message:", ["Formal", "Concise", "Friendly", "Professional"])

button_clicked = st.button("Improve Message")

if button_clicked:
    if message.strip() == "":
        st.warning("Please enter a message first.")
    else:

        prompt = f"""Rewrite the following message in a {tone} tone.

        Return only one improved version of the message.
        Do not provide explanations, options, or extra comments.

        Message:
        {message}"""

        try:
            response = client.models.generate_content(model="gemini-3.6-flash", contents=prompt)

            st.subheader("Improved Message:")
            st.write(response.text)
        except Exception:
            st.error("Something went wrong. Please try again.")
