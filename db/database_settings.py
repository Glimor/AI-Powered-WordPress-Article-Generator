from sqlalchemy import create_engine, Column, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()

# ORM tablosu tanımlamaları
class Setting(Base):
    __tablename__ = 'settings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    api_key = Column(String)
    wp_api_url = Column(String)
    wp_username = Column(String)
    wp_password = Column(String)
    sleep_time = Column(String)
    max_length = Column(String)
    ai_model = Column(String)
    max_articles = Column(String)

class Suggestion(Base):
    __tablename__ = 'suggestions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    suggestion = Column(String)
    keyword = Column(String)

class Keyword(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True, autoincrement=True)
    keyword = Column(String)


class DatabaseSettings:
    def __init__(self):
        self.engine = create_engine('sqlite:///settings.db')
        self.session_factory = sessionmaker(bind=self.engine)
        self.Session = scoped_session(self.session_factory)
        Base.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()

    def get_api_key(self):
        session = self.get_session()
        try:
            result = session.query(Setting).filter_by(id=1).first()
            return result.api_key if result else None
        finally:
            session.close()

    def insert_one(self, api_key, wp_api_url, wp_username, wp_password, sleep_time, max_length, ai_model, max_articles):
        session = self.get_session()
        try:
            setting = Setting(api_key=api_key, wp_api_url=wp_api_url, wp_username=wp_username,
                              wp_password=wp_password, sleep_time=sleep_time, max_length=max_length, ai_model=ai_model, max_articles=max_articles)
            session.add(setting)
            session.commit()
        finally:
            session.close()

    def update_one(self, api_key, wp_api_url, wp_username, wp_password, sleep_time, max_length, ai_model, max_articles):
        session = self.get_session()
        try:
            setting = session.query(Setting).filter_by(id=1).first()
            if setting:
                setting.api_key = api_key
                setting.wp_api_url = wp_api_url
                setting.wp_username = wp_username
                setting.wp_password = wp_password
                setting.sleep_time = sleep_time
                setting.max_length = max_length
                setting.ai_model = ai_model
                setting.max_articles = max_articles
                session.commit()
        finally:
            session.close()

    def insert_suggestion(self, suggestion, keyword):
        session = self.get_session()
        try:
            suggestion_entry = Suggestion(suggestion=suggestion, keyword=keyword)
            session.add(suggestion_entry)
            session.commit()
        finally:
            session.close()

    def delete_one_suggestion(self, suggestion):
        session = self.get_session()
        try:
            session.query(Suggestion).filter_by(suggestion=suggestion).delete()
            session.commit()
        finally:
            session.close()

    def delete_one_keyword(self, keyword):
        session = self.get_session()
        try:
            session.query(Keyword).filter_by(keyword=keyword).delete()
            session.commit()
        finally:
            session.close()
            
    def insert_keywords(self, keywords):
        session = self.get_session()
        try:
            for keyword in keywords:
                keyword_entry = Keyword(keyword=keyword)
                session.add(keyword_entry)
            session.commit()
        finally:
            session.close()

    def get_all_data(self, table_name):
        session = self.get_session()
        try:
            table_class = {
                'settings': Setting,
                'suggestions': Suggestion,
                'keywords': Keyword
            }.get(table_name)
            if table_class:
                return session.query(table_class).all()
            else:
                raise ValueError("Table name not recognized.")
        finally:
            session.close()
