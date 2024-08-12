# Simple ChatBot with Google Generative AI

This is a simple chatbot application built using Streamlit and powered by Google Generative AI. The chatbot takes user input and generates responses using a pre-trained AI model.

## Features

- **Interactive Chat Interface**: Users can interact with the chatbot through a simple and intuitive interface.
- **Session Management**: The chat history is maintained throughout the session.
- **Error Handling**: The application gracefully handles errors that may occur during the response generation process.

## Installation

To run this application, you need to have Python installed on your system. Follow the steps below to set up and run the application:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/simple-chatbot.git
    cd simple-chatbot
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    streamlit run chatbot.py
    ```

## Usage

1. Open your web browser and navigate to `http://localhost:0000`.
2. Enter your prompt in the text input field and click "Send".
3. The chatbot will generate a response based on your input and display it on the screen.
4. The chat history will be displayed below the input field.

## Code Overview

- **app.py**: The main application file that contains the Streamlit code for the chatbot interface.
- **getResponseFromModel(user_input)**: A function that takes user input and generates a response using a pre-trained AI model. It includes error handling to manage potential issues.


