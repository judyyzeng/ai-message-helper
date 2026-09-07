# AI Message Helper

This is a small project I built to explore how AI can make everyday communication easier. It helps users turn a rough message into a clearer version based on the tone they choose.

## Features

- Enter a rough message
- Choose a tone such as Formal, Friendly, Concise, or Professional
- Use Gemini AI to rewrite the message
- Show a simple warning if no message is entered

## How it works

The app is built with Python and Streamlit. When the user enters a message and chooses a tone, the app sends a prompt to the Gemini API. The AI then returns one improved version of the message, which is shown on the page.

## What I learned

Through this project, I learned how to connect a simple web interface to an AI API and how to use prompts to control the style of the AI response. I also learned how to handle empty input and API errors so the app is easier to use.

## Technologies used

- Python
- Streamlit
- Google Gemini API
- Git and GitHub

## How to run

1. Clone or download this repository.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Set your Gemini API key as an environment variable.

On macOS or Linux:

```bash
export GEMINI_API_KEY="your_api_key_here"
```

4. Run the app:

```bash
streamlit run app.py
```

5. Open the local Streamlit page in your browser.
