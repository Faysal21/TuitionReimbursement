# TuitionReimbursement
## Project Description
A full-stack web application designed for a simulated tuition reimbursement management system.

## Technologies used
* Psycopg2 - version 2.9.3
* Flask - version 2.1.2
* Flask-Cors - version 3.0.10
* PostgreSQL - version 14

## Features
Ready-to-use:
* Fill out a request form with unique employee and event details
* Approve or deny an employee's request for reimbursement as a department head, supervisor, and/or Benefits Coordinator
* Login directly to a request form by giving the user's e-mail address, employee ID, and associated request ID

To be added:
* Send user to designated page after logging in (based on current status of request form)
* Add full functionality to "Submit Decision" buttons on approval pages
* Store employee-uploaded files or file paths on request form fillout and final grade/presentation upload pages

## Getting Started
1. If necessary, install Python 3 and any Python-friendly IDE
2. Clone this repo by running the following command in Git Bash or your OS command line: _git clone https://github.com/Faysal21/FlashpointApp.git_
3. Setup a local PostgreSQL database on your computer or create one via Amazon RDS to use over the cloud.
4. In your PostgreSQL database, make sure to add the corresponding tables with all the necessary columns (see classes.py).
5. After creating a Python project with files from this repository, add a database_conn.py file to connect to your database (not included here)
6. Install Flask, Flask-Cors, and Psycopg2 from the Python Package Index (PyPI) to your project.
7. Run the app.py file in the project and open the index.html page in a browser to begin navigating the pages.


## Usage
On the index page, you will fill out two sections of the form. The first section covers all the employee's personal information, while the second section is for the event in which the employee is participating to redeem his/her reimbursement. You are required to fill out every field except for uploading a file at the very end. Click ***"SUBMIT"*** when you are done.

Atop that page, there are also links for you to preview the different approval pages for the non-standard employee roles, an upload page to provide a file related to the final grade or presentation, and most importantly one to login directly to a particular request and pick up where one left off depending on how far along the request form is in the full approval process.

As mentioned above in features, you should be able to provide the e-mail and employee ID on the login page, then give the request ID corresponding to that employee who completed that form. If all is correct, you should receive a pop-up message informing you that the login process is ready.

The approval pages are prototypes at this moment; however, you can choose to either approve or deny. If you choose to deny, a text box below allows you to provide feedback explaining the reason why you did not approve and/or what can be done going forward. You can then hit ***"SUBMIT DECISION"*** when finished.

In the final grade/presentation upload page, another prototypical design, you would choose a file to upload for one last approval before being confirmed to guarantee reimbursement. Upload as many files as you want, click ***"UPLOAD FILE"*** after choosing each file, and click ***"FINISH"*** once you're done.

