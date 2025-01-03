from typing import Sequence

from sqlalchemy import select, String, ForeignKey, Table, Column
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship, joinedload
from schema import UserAdd, Quiz

engine = create_async_engine("sqlite+aiosqlite:///db//fastapi.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class UserOrm(Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    age: Mapped[int]
    phone: Mapped[str | None]
    quizzes = relationship('QuizOrm', back_populates='user')


quiz_question = Table('quiz_question', Model.metadata,
                      Column('quiz_id', ForeignKey('quiz.id'), primary_key=True),
                      Column('question_id', ForeignKey('question.id'), primary_key=True)
                      )


class QuizOrm(Model):
    __tablename__ = 'quiz'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    user: Mapped[int] = mapped_column(ForeignKey('user_id'))
    question = relationship("QuestionOrm", secondary="quiz_question", back_populates='quiz')


class QuestionOrm(Model):
    __tablename__ = 'question'
    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str] = mapped_column(String(500))
    answer: Mapped[str] = mapped_column(String(100))
    wrong1: Mapped[str] = mapped_column(String(100))
    wrong2: Mapped[str] = mapped_column(String(100))
    wrong3: Mapped[str] = mapped_column(String(100))
    quiz = relationship("QuizOrm", secondary="quiz_question", back_populates='question')


async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)


async def add_test_data():
    async with new_session as session:
        users = [
            UserOrm(name='user1', age=20),
            UserOrm(name='user2', age=30, phone='123456789'),
            UserOrm(name='user3', age=40),
        ]
        quizzes = [
            QuizOrm(name='quiz1', user=users[0]),
            QuizOrm(name='quiz2', user=users[1]),
            QuizOrm(name='quiz3', user=users[2])
        ]
        questions = [
            QuestionOrm(question='Сколько будeт 2+2*2', answer='6',
                        wrong1='8', wrong2='2', wrong3='0'),
            QuestionOrm(question='Сколько месяцев в году имеют 28 дней?', answer='Все',
                        wrong1='Один', wrong2='Ни одного', wrong3='Два'),
            QuestionOrm(question='Какой рукой лучше размешивать чай?', answer='Ложкой',
                        wrong1='Правой', wrong2='Левой', wrong3='Любой')
        ]
        quizzes[0].question.append(questions[0])
        quizzes[0].question.append(questions[1])
        quizzes[1].question.append(questions[1])
        quizzes[1].question.append(questions[2])
        quizzes[2].question.append(questions[0])
        quizzes[2].question.append(questions[2])

        session.add_all(quizzes)
        session.commit()


class UserRepository:

    @classmethod
    async def add_user(cls, user: UserAdd) -> int:
        async with new_session() as session:
            data = user.model_dump()
            user = UserOrm(**data)
            session.add(user)
            await session.flush()
            await session.commit()
            return user.id

    @classmethod
    async def get_users(cls) -> Sequence[UserOrm]:
        async with new_session() as session:
            query = select(UserOrm)
            res = await session.execute(query)
            users = res.scalars().all()
            return users

    @classmethod
    async def get_user(cls, id: int) -> UserOrm:
        async with new_session() as session:
            query = select(UserOrm).filter(UserOrm.id == id)
            res = await session.execute(query)
            user = res.scalars().first()
            return user


class QuizRepository:

    @classmethod
    async def add_quiz(cls, quiz: Quiz):
        async with new_session() as session:
            data = Quiz.model_dump()
            quiz = QuizOrm(**data)
            session.add(quiz)
            await session.flush()
            await session.commit()
            return quiz.id

    @classmethod
    async def get_quizzes(cls) -> list[QuizOrm]:
        async with new_session() as session:
            query = select(QuizOrm)
            res = await session.execute(query)
            quizzes = res.scalars.all()
            return quizzes

    @classmethod
    async def get_quiz(cls, id: int) -> QuizOrm:
        async with new_session() as session:
            query = select(QuizOrm).filter(QuizOrm.id == id)
            rez = await session.execute(query)
            quiz = rez.scalars().first()
            return quiz
            # quiz = session.query(QuizOrm). \
            #     options(joinedload(QuizOrm.question)).where(QuizOrm.id == id)
            # return quiz


