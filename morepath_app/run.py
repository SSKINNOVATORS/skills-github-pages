import sqlalchemy
import morepath
from morepath_app.app import App, Session
from morepath_app.model import Base
import morepath_app.path
import morepath_app.view


if __name__ == '__main__':
    engine = sqlalchemy.create_engine("sqlite:///morepath_sqlalchemy.db")
    Session.configure(bind=engine)
    Base.metadata.create_all(engine)
    #morepath.autoscan('morepath_app')
    morepath.run(App())