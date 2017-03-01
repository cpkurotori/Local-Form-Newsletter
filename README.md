#Local Form - Newsletter
This python program (using flask) is designed to gather information and store it locally in a csv file. This works nicely for Newsletter sign-ups, quick check-ins, or anything else you don't need a lot of security or logic for. This simply takes the information submitted in a form and appends a file (by default "maillist.csv") with the information. By deafult this is set up for a Newsletter sign up gathering First Name, Last Name, and email.

##newsletter.py
This contains the code that starts the flask application and sends the static index.html page to the browser. When the user submits their information, the program logs the information in "maillist.csv".

Please note: There are no logic tests to test for blank inputs, duplicates, nor are there logic to log the date.