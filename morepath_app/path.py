from morepath_app.app import App
from morepath_app.model import Document, Root,AddDocument,DeleteDocument,SearchDocument,UpdateDocument


@App.path(model=Root, path="/")
def get_root():
    return Root()

#http://localhost:5000/documents/find/?id=2
@App.path(model=SearchDocument, path="documents/find")
def get_document(request):
    return SearchDocument(request.db_session,Document)

#http://localhost:5000/documents/add/?content=ddjddkdj&title=knfkajmgdd
@App.path(model=AddDocument,path="documents/add")
def add_document(request):
    return AddDocument(request.db_session,Document)

#http://localhost:5000/documents/delete/?id=2
@App.path(model=DeleteDocument,path="documents/delete")
def delete_document(request):
    return DeleteDocument(request.db_session,Document)

#http://localhost:5000/documents/update/?id=2&?content=ddjddkdj&title=knfkajmgdd
@App.path(model=UpdateDocument,path="documents/update")
def update_document(request):
    return UpdateDocument(request.db_session,Document)
