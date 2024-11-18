import os
from random import shuffle

from models import db, db_add_new_data, Quiz, Question, User
from flask import Flask, render_template, request, session, redirect, url_for

BASE_DIR = os.getcwd()

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz_db'
app.config['SECRET_KEY'] = 'dbsdj73hes!shjdn54445xcjhjhs!'

db.init_app(app)

html_config = {
    'admin': True,
    'debug': False
}

with app.app_context():
    db_add_new_data()

message = ''

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', html_config=html_config)


@app.route('/quiz/')
def quiz_list():
    quizzes = Quiz.query.order_by(Quiz.name).all()
    return render_template('quiz_list.html', quizzes=quizzes, html_config=html_config)


@app.route('/quiz/id', methods=['GET', 'POST'])
def quiz_view():
    if request.method == 'GET':
        return redirect(url_for('quiz_list'))
    session['quiz_id'] = request.form.get('quiz')
    session['question_num'] = 0
    session['question_id'] = 0
    session['right_answers'] = 0
    return redirect(url_for('question_view'))


@app.route('/question/', methods=['GET', 'POST'])
def question_view():
    if request.method == 'POST':
        question = Question.query.filter_by(id=session['question_id']).one()
        if question.answer == request.form.get('ans_text'):
            session['right_answers'] += 1
        session['question_num'] += 1
    quiz = Quiz.query.filter_by(id=session['quiz_id']).one()
    if int(session['question_num']) >= len(quiz.question):
        session['quiz_id'] = -1
        return redirect(url_for('result'))
    else:
        question = quiz.question[session['question_num']]
        session['question_id'] = question.id
        answers = [question.answer, question.wrong1, question.wrong2, question.wrong3]
        shuffle(answers)

        return render_template('question.html',
                               answers=answers,
                               question=question,
                               html_config=html_config)


@app.route('/result/')
def result():
    return render_template('result.html',
                    right=session['right_answers'],
                    total=session['question_num'],
                    html_config=html_config)


@app.route('/quiz_edit/', methods=['GET', 'POST'])
def quiz_edit():
    quizzes = Quiz.query.all()
    questions = Question.query.all()
    if request.method == 'POST':
    return render_template('quiz_edit', quizzes=quizzes, questions=questions)


@app.route('/quiz_add/', methods=['GET', 'POST'])
def quiz_add():
    try:
        if request.method == 'POST':
            name = request.form['name']
            user = User.query.first()
            quiz = Quiz(name, user)
            db.session.add(quiz)
            db.session.commit()
            global message
            message = 'Квиз успешно добавлен'
            return render_template('quiz_add', message=message)
        else:
            return redirect(url_for('index'))
    except:
        message = 'Квиз не был добавлен'
        return render_template('quiz_add', message=message)


@app.route('/question_add/', methods=['GET', 'POST'])
def question_add():
    try:
        if request.method == 'POST':
            quest = request.form['question']
            answer = request.form['answer']
            wrong1 = request.form['wrong1']
            wrong2 = request.form['wrong2']
            wrong3 = request.form['wrong3']
            question = Question(quest, answer, wrong1, wrong2, wrong3)
            db.session.add(question)
            db.session.commit()
            global message
            message = 'Вопрос успешно добавлен'
            return render_template('question_add', message=message)
        else:
            return redirect(url_for('index'))
    except:
        message = 'Вопрос не был добавлен'
        return render_template('question_add', message=message)


# @app.route('/quizzes_view/', methods=['POST', 'GET'])
# def view_quiz_edit():
#     if request.method == 'POST':
#         pass
#     quizzes = Quiz.query.all()
#     questions = Question.query.all()
#     return render_template('quizzes_view.html',
#                            html_config=html_config,
#                            quizzes=quizzes,
#                            questions=questions,
#                            len=len)


@app.errorhandler(404)
def page_not_found(e):
    return '<h1 style="color:red; text-align:center; margin-top:100px"> Упс..... </h1>'


if __name__ == "__main__":
    app.run(port=8000, debug=True)
