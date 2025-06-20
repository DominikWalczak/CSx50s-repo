CapyTypeQuiz
#### Video Demo:  https://youtu.be/UdrTSJYSO5k
#### Description:
I created flask page using SQL, JavaScipt, CSS and JinJa.
Flask python(app.py) file has got written functions which allow user to login, register, switch pages.
I have added functions like SQL from cs50, Flask, redicrect, render_template, request, session from flask,
check_password_hash, generate_password_hash from werkzeug.security
Flask file uses functions from functions.py where I added functions like wrong, is_strong_password, login_required.
I also used bootstrap for css in html.
Whenever user tries to login into my site he gets checked by "/login" function which uses SQL date base where is users table containing all users, if there is no such a account user get's redirected to "wrong.html" which shows capybara image.
Whenever user tries to register on my site he gets checked by "/register" function which checks if there is user with such a account, if there is user, person gets redirected to "wrong.html" which shows capybara image but if there is no such a account user get's account created which allows him to log in and take a quiz!
When user get's logged in "/" is used then which shows "index.html" which is actually Main Page of my project.
On the navbar there are 3 href links which redirect to "quiz.html","history.html" and to "index.html", there is also log out function which uses "/logout" from flask which redirects to "login.html" and clears session["user_id"].
There is "login.html", "register.html" and "wrong.html" which allow user to see and use them without logging in.
On the navbar of "login.html", "register.html" and "wrong.html" are 3 href links "/login", "/register" and "/" but "/" requires user to be logged in so user gets redirected back to" login.html"
I got @login_required function which requires user to be logged in through session["user_id"] if they are not they are getting redirected to "login.html".
I used Jinja to fill every page with basic layout from "layout.html" and to add functionality and to connect it with flask file.
I used CSS to make backgrounds for the navbar and body as images, also I styled the navbars CapyWorld in 3 different green tones.
Page "index.html" is Main Page which explains the idea of the page.
Page "history.html" shows history of taken quizes by using SQL date base and afterwards uses Jinja to show to user date, time and capybara type he/she got.
JavaScript part is responsible for "quiz.html", there is 10 questions with 4 answers each in A, B, C, D order with 25 possible results!
Every time user answers one of var a, b, c, d with var sum gets +1, if sum is not 10 next question will be shown to user, at the end of quiz funtion in JavaScript "CapyType" gets it's final step activated which calculates the outcome based on answers.
For instance if user got 4 a's, 3 b's, 2 c's and 1 d he gets into "a" bracket then into "b" bracket and then the result is in "c" bracket because it's second smalles variable and gets the capybara type with id 1 which transfers it through flask to JinJa in answer.html.
When user is done with answearing the quiz's questions the results are transfered to flask where page "answer.html" is open afterwards with SQL history date base table which saves urls and capybara types.
Page "answer.html" with Jinja's help shows correct picture url and user's capibara type and saves outcome in SQL history table.

That was CapyType,
Dominik Walczak
