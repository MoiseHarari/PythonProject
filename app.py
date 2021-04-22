from flask import Flask
from flask import request
import random
# from mbta_helper import find_stop_near
from flask import render_template
from problems import check_answer, generate_problem, q_req, show_results
# need help with importing dictionary and generate_problem function from problems.py
from problems_and_answers import problem_dictionary

app = Flask(__name__)

global total_questions
global correct_answers_count
correct_answers_count = 0
global questions_count 
questions_count = 0

# startpage: 
@app.route('/')
def get_started():
    """returns index page"""
    return render_template('index.html')

# startpage data processing
@app.route('/', methods=["GET", "POST"])
def questions_requested():
    """processes user's desired number of questions and returns welcome page"""
    global total_questions
    if request.method == "POST":
        count = request.form.get('count')
        total_questions = q_req(count)
        return render_template('welcome.html', total_questions=total_questions)
        
# actual app:
@app.route('/questions')
def show_problem():
    """displays porblem on problem page during session, ends session when user answered desired amount of questions
    returns questions or end page"""
    global questions_count
    global correct_answers_count
    if questions_count < total_questions:
        problem_statement = generate_problem() 
        questions_count += 1
        return render_template('questions.html', problem_statement=problem_statement)
    else: 
        questions_count = 0
        result = show_results()
        return render_template('end.html', result=result)

# check answers:
@app.route('/questions', methods=["GET", "POST"])  
def reply():
    """checks user's answers and returns checkanswer page with reply
    and troubeshoots error if user does not put anything before clicking submit"""
    try:
        if request.method == "POST":
            answer = float(request.form['math_answer'])
            reply = check_answer(answer)     
        return render_template('checkanswer.html', reply=reply, questions_count=questions_count)
    except ValueError:
        return render_template("error.html")  
        
if __name__ == "__main__":
    app.run(debug=True)
