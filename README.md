# Nova Student AI Assistant

An AI-powered learning assistant that helps students study smarter by generating study plans, solving homework problems, assisting with coding, and providing research support using Amazon Nova.

## Inspiration

Students often struggle to manage multiple academic tasks such as studying, solving assignments, and researching topics. This project was created to build a single intelligent assistant that helps students learn more efficiently and stay organized.

## What It Does

Nova Student AI Assistant provides several learning tools in one platform:

* Personalized study plan generator
* Homework and problem-solving assistance
* Coding help and debugging support
* Debate and critical thinking assistance
* Research insights and project idea generation

The goal is to provide a smart learning companion for students.

## How It Was Built

The application was developed using Python and Streamlit for the interface.
User prompts are sent to Amazon Nova through Amazon Bedrock, which generates intelligent responses that are displayed in the app.

## Technologies Used

* Python
* Streamlit
* Amazon Web Services (AWS)
* Amazon Bedrock
* Amazon Nova
* Boto3

## Challenges Faced

* Configuring AWS credentials and access to Amazon Nova
* Understanding the Bedrock API response structure
* Designing a simple but effective user interface for students

## What I Learned

Through this project I learned how to integrate Amazon Nova models using Amazon Bedrock and build AI-powered applications with Python and Streamlit.

## Future Improvements

* Voice-based AI study assistant
* PDF and lecture note analysis
* Student progress analytics
* Personalized AI tutoring system

## Getting Started

### Install dependencies

pip install -r requirements.txt

### Run the application

streamlit run app.py

## Project for

Amazon Nova AI Challenge
