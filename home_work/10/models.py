from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), nullable=False)
    login = db.Column(db.String(25), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False, unique=True)
    quizzes = db.relationship('Quiz', backref='user', cascade='all, delete, delete-orphan')

    def __init__(self, name: str, login: str, password: str):
        super().__init__()
        self.name = name
        self.login = login
        self.password = password

    def __repr__(self):
        return f'Name:{self.name}, login:{self.login}'


quiz_question = db.Table('quiz_question',
                         db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.id'), primary_key=True),
                         db.Column('question_id', db.Integer, db.ForeignKey('question.id'), primary_key=True),
                         )


class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name: str, user: User):
        super().__init__()
        self.name = name
        self.user = user

    def __repr__(self):
        return f'Quize name:{self.name}, id:{self.id}'


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(300), nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    wrong1 = db.Column(db.String(100), nullable=False)
    wrong2 = db.Column(db.String(100), nullable=False)
    wrong3 = db.Column(db.String(100), nullable=False)
    quiz = db.relationship('Quiz', secondary=quiz_question, backref='question')

    def __init__(self, question: str, answer: str, wrong1: str, wrong2: str, wrong3: str):
        super().__init__()
        self.question = question
        self.answer = answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

    def __repr__(self):
        return f'Question:{self.question}, id:{self.id}'


def db_add_new_data():
    db.drop_all()
    db.create_all()

    user1 = User('user1', 'login1', 'password1')
    user2 = User('user2', 'login2', 'password2')
    user3 = User('user3', 'login3', 'password3')

    quizzes = [
        Quiz('quiz1', user1),
        Quiz('quiz2', user2),
        Quiz('quiz3', user3),
        Quiz('quiz4', user1),
        Quiz('quiz5', user2)
    ]

    questions = [
        Question('Сколько будут 2+2*2', '6', '8', '2', '0'),
        Question('Сколько месяцев в году имеют 28 дней?', 'Все', 'Один',
                 'Ни одного', 'Два'),
        Question('Каким станет зелёный утёс, если упадет в Красное море?', 'Мокрым?',
                 'Красным', 'Не изменится',
                 'Фиолетовым'),
        Question('Какой рукой лучше размешивать чай?', 'Ложкой', 'Правой',
                 'Левой', 'Любой'),
        Question('Что не имеет длины, глубины, ширины, высоты, а можно измерить?',
                 'Время', 'Глупость', 'Море',
                 'Воздух'),
        Question('Когда сетью можно вытянуть воду?', 'Когда вода замерзла', 'Когда нет рыбы',
                 'Когда уплыла золотая рыбка', 'Когда сеть порвалась'),
        Question('Что больше слона и ничего не весит?', 'Тень слона', 'Воздушный шар',
                 'Парашют', 'Облако'),
        Question('Что такое у меня в кармашке?', 'Кольцо', 'Кулак', 'Дырка',
                 'Бублик')
    ]

    quizzes[0].question.append(questions[0])
    quizzes[0].question.append(questions[2])
    quizzes[0].question.append(questions[5])

    quizzes[1].question.append(questions[1])
    quizzes[1].question.append(questions[3])
    quizzes[1].question.append(questions[6])

    quizzes[2].question.append(questions[4])
    quizzes[2].question.append(questions[7])
    quizzes[2].question.append(questions[6])

    quizzes[3].question.append(questions[0])
    quizzes[3].question.append(questions[3])
    quizzes[3].question.append(questions[4])
    quizzes[3].question.append(questions[7])

    quizzes[4].question.append(questions[1])
    quizzes[4].question.append(questions[2])
    quizzes[4].question.append(questions[5])
    quizzes[4].question.append(questions[6])

    db.session.add_all(quizzes)
    db.session.commit()
