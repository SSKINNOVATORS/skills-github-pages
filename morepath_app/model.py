from sqlalchemy import Column, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DocumentCollection:
    def __init__(self, db_session,model_class):
        self.db_session = db_session
        self.model_class = model_class

    def create(self, **kwargs):
        instance = self.model_class(**kwargs)
        self.db_session.add(instance)
        self.db_session.flush()
        return instance

    def get_by_id(self, id):
        return self.db_session.query(self.model_class).get(id)

    def update(self, id, **kwargs):
        instance = self.get_by_id(id)
        if not instance:
            return None
        for key, value in kwargs.items():
            if hasattr(instance, key):
                setattr(instance, key, value)
        self.db_session.flush()
        return instance

    def delete(self, id):
        instance = self.get_by_id(id)
        if not instance:
            return None
        self.db_session.delete(instance)
        self.db_session.flush()
        return instance

    # def query(self):
    #     return self.db_session.query(Document)
    #
    # def add(self, title, content):
    #     session = self.db_session
    #     document = Document(title=title, content=content)
    #     session.add(document)
    #     session.flush()
    #     return document

class Root:
    pass


class Document(Base):
    __tablename__ = "document"

    id = Column(Integer, primary_key=True)
    title = Column(Text)
    content = Column(Text)

class AddDocument(DocumentCollection):
    pass

class DeleteDocument(DocumentCollection):
    pass

class SearchDocument(DocumentCollection):
    pass
