# 🌟 AI Challenge - Tech Sisters October 2024 🌟

## Introduction

Welcome to the AI Challenge repository for Tech Sisters! 🎉 This month, we focused on learning about **Large Language Models (LLMs)** and experimenting with the **Google Gemini API**. This project is designed to put your knowledge into practice. Even if you have never worked with **Streamlit**, you'll find it easy to get started! 😊

## Project Overview

In this repository, you'll find a simple chat application built using Streamlit and the Google Gemini API. Feel free to customize the prompts and user interface as you wish—be creative! ✨

## Getting Started

Follow these steps to set up your environment and run the Streamlit app:

### Prerequisites

Make sure you have the following installed:
- Python (version 3.7 or higher) 🐍
- pip (Python package installer) 📦

### Steps to Set Up

1. **Fork the Repository** 🍴
   - Click on the "Fork" button at the top right corner of this page to create a copy of this repository in your GitHub account.

2. **Clone the Forked Repository** 💻
   - Open your terminal (or command prompt) and run the following command:
     ```bash
     git clone https://github.com/YOUR_USERNAME/YOUR_FORKED_REPOSITORY.git
     ```
   - Replace `YOUR_USERNAME` with your GitHub username and `YOUR_FORKED_REPOSITORY` with the name of your forked repository.

3. **Create a Virtual Environment** 🌱
   - Navigate to the project directory:
     ```bash
     cd YOUR_FORKED_REPOSITORY
     ```
   - Create a virtual environment:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```

4. **Install Requirements** 📜
    - Before installing the necessary packages, make sure to navigate to the `/app` directory. You can do this by running the following command in your terminal:
        ```bash
        cd app
        ```
   - Install the necessary packages by running:
        ```bash
        pip install -r requirements.txt
        ```

### Running the Streamlit App 🚀

To run the Streamlit application, use the following command in your terminal:

```bash
streamlit run app.py
```

Once the app is running, you can access it in your web browser at http://localhost:8501. 🌐 Here, you'll find a user-friendly interface for the chat application, allowing you to interact with the Google Gemini API and ask questions about Tech Sisters.

Feel free to test it out, and don't hesitate to explore the functionalities. Your creativity can really shine here!

## Customization 🎨

You will find a chat application in the project. You're encouraged to customize the prompts and the user interface to make it your own. Here are a few ideas to get you started:

- **Modify Prompts:** Change the default prompts to suit your style or the type of conversations you want your app to handle. Experiment with different tones, topics, or formats to see how the responses vary! 🗣️

- **Update the UI:** Streamlit allows for easy customization of the user interface. Try changing colors, layouts, and text styles to create a unique look for your app. Don't forget to add your personal touch! 🎨

- **Add New Features:** Feel free to expand the functionality of the chat app. You can expirement with Retrieval Augmented Generation as seen in the course. The possibilities are endless! 🌟

Be creative and have fun with your project! Your ideas and innovations can make this app even better. 💖

## Deployment 🌍

Once you’ve customized your chat application and are ready to share it with others, here are some options for deploying your Streamlit app:

### Deploying on Streamlit Sharing

1. **Create a Streamlit Account:** If you don't have one yet, go to [Streamlit Sharing](https://streamlit.io/sharing) and sign up for an account.

2. **Push Your Changes to GitHub:** Make sure all your latest changes are pushed to your GitHub repository.

3. **Deploy Your App:**
   - Go to your Streamlit Sharing dashboard.
   - Click on "New App" and select your GitHub repository.
   - Choose the branch (usually `main`) and specify the file path to your `app.py`.
   - Click "Deploy," and your app will be live shortly! 🚀