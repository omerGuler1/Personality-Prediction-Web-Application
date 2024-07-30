# Personality Prediction Web Application

This project is a web application that predicts personality types using the K-Nearest Neighbors (KNN) algorithm. The application is built with FastAPI for the backend and Streamlit for the frontend, providing an interactive and user-friendly personality test.

## Project Description

The Personality Prediction Web Application allows users to take a personality test and receive predictions based on their responses. Users can choose between two test lengths: a comprehensive 60-question test or a shorter 20-question version. Both versions classify users into one of 16 personality types. While the 60-question test provides a more detailed analysis, the 20-question version offers a quicker way to get an overview of their personality type. Each personality type is described with specific characteristics to help users understand their results better.


### How To Run The Project

This project requires three terminals to run the backend and frontend services. Follow the steps below:

Terminal 1: Start MySQL and Create the Database
First of all, you need to configure the DB_URL variable from sql_app/database.py file with your own database credentials. Here is the format:

DB_URL = "mysql+pymysql://username:password@host:port/persons" (database named persons)

1. Start MySQL service:
   
$ brew services start mysql

2. Access MySQL with the root user:
   
$ mysql -u root -p

3. Create the persons database:

$ CREATE DATABASE persons;

$ EXIT;

Terminal 2: Start the FastAPI Application
1. Navigate to the project directory.
2. Start the FastAPI application using Uvicorn:

$ uvicorn app.main:app --reload  

Terminal 3: Start the Streamlit Frontend
1. Navigate to the project directory.
2. Start the Streamlit application:

$ streamlit run frontend/app.py 

#### Website:
<img width="1009" alt="Screenshot 2024-07-30 at 09 51 43" src="https://github.com/user-attachments/assets/dd589975-8d88-440a-9ad6-df9a0b00c1a6">

##### Prediction:
<img width="757" alt="Screenshot 2024-07-30 at 09 56 36" src="https://github.com/user-attachments/assets/2d8da1e3-467e-4558-88be-006d297f7a53">
