# Environmental-Event-Service
It was a part of our "Software as a Service" course, where we had to combine three services to build a new api that could provide a combination of services. Special attention to sustainability was given as it was one of the requirement.

The service provide summary of humanitarian crisis report from all over world which are published in the ReliefWeb website. 
The following Api's were user,
1. ReliefWeb API - To get reports on humanitarian crisis.
2. Aylien Machine Learning API - To summerize the reports.
3. Google country and places - To get the ilst of all countries in the world.

### Technologies Used
1. Python 3.6
2. Flask Microframework for Rest Service
3. HTML/CSS/Javascript

### How to run the service:
1. Download and Install Python 3.6 from https://www.python.org/downloads/
2. Use the command prompt to navigate to the directory of the project and run the command,

`pip install –r requirements.txt`

This installs the dependencies of the project.

3. To start the web server, run the command in the project directory,

`python app.py runserver`

4. The web service will be accessible on http://localhost:8888/
