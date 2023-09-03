# Book Review System

## Overview

The Book Review System is a simple web application that allows users to add books along with their reviews. It's built using Flask, SQLite, and Vue.js, and styled with Bootstrap.

## Process Followed

1. **Setting up the Backend**:
    - Used Flask as the web framework.
    - SQLite was chosen for the database to store book details.
    - Created routes for the main page and adding books.

2. **Frontend**:
    - Used Vue.js for dynamic rendering of the book list.
    - Bootstrap was integrated for styling and responsiveness.
    - Custom CSS was added for additional styling.

3. **Docker Integration**:
    - Created a `Dockerfile` to containerize the application.
    - Used the `python:3.8-slim` image as the base.
    - Set up the working directory, copied the necessary files, and installed Flask.
    - Exposed port 5000 and set the command to run the Flask app.

## App Functionality

- **Add Books**: Users can add a book by providing its title, author, and an optional review.
- **View Books**: All added books are displayed in a list format with their respective reviews.

## Author

Roll Number: M21AIE250

---

## Setup and Run

To run the application:

1. Build the Docker image:
    ```bash
    docker build -t book-review-app .
    ```

2. Run the Docker container:
    ```bash
    docker run -p 5000:5000 book-review-app
    ```

3. Visit `http://localhost:5000` in your browser.

---

![Screenshot of my app](https://private-user-images.githubusercontent.com/111610085/265280940-d4eb75fb-90c5-48f9-b0d2-158f550e698d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTEiLCJleHAiOjE2OTM3NjQyOTMsIm5iZiI6MTY5Mzc2Mzk5MywicGF0aCI6Ii8xMTE2MTAwODUvMjY1MjgwOTQwLWQ0ZWI3NWZiLTkwYzUtNDhmOS1iMGQyLTE1OGY1NTBlNjk4ZC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBSVdOSllBWDRDU1ZFSDUzQSUyRjIwMjMwOTAzJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDIzMDkwM1QxNzU5NTNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lZDM1MWM3YzU3YWYyYWMyOWY1MzU3MWU5NmQ4YjZhYTFmZDI5YTdkZTdjYjgwMGNjM2JmM2Y4NDZkMjUwZWRhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.-gnKpIy2_G8POYU1VlNBmq3fMgxTbgnxYv4Rk33X6gI)




# M21AIE250
