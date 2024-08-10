Simple Streamlit app using LangChain and Google Generative AI to generate real-time responses based on user input. Easy setup, clean interface, and powered by state-of-the-art AI technology.

---


---

# LangChain-Streamlit-App 
## Overview

This project is a simple web application built using Streamlit and LangChain with the Google Generative AI API. The app allows users to input a question, which is then processed by Google's Generative AI model ("gemini-pro") through LangChain, and the generated response is displayed in real-time. This demo application serves as a straightforward example of integrating state-of-the-art AI models into a user-friendly web interface.

## Features

- **Real-Time Interaction**: Users can input any question, and the app will generate an answer using Google's Generative AI model.
- **Streamlit Interface**: The app uses Streamlit for a clean and responsive web interface, making it easy to deploy and share.
- **Environment Management**: Includes secure management of API keys using environment variables.
- **Error Handling**: Basic error handling is in place to manage API call issues.

## Installation

To run this application locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/langchain-streamlit-app.git
   cd langchain-streamlit-app
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.7 or higher. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up Google API Key**:
   Set your Google API key in your environment:
   ```bash
   export GOOGLE_API_KEY="your_google_api_key"
   ```

4. **Run the Application**:
   Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Input a Question**: Type your question in the provided text input field.
2. **Generate a Response**: Click the 'Generate' button to get an AI-generated answer.
3. **View the Response**: The generated answer will be displayed below the input field.

## Requirements

- **streamlit**: For building the web interface.
- **langchain-google-genai**: To interact with Google's Generative AI models.
- **google-cloud-aiplatform**: Required for Google API interaction.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.

---
