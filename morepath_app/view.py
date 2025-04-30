from morepath import redirect
from morepath_app.app import App
from morepath_app.model import Document, Root, AddDocument, DeleteDocument, SearchDocument, UpdateDocument
from utils import *


@App.json(model=Root)
def root_default(self, request):
    return redirect("/documents")


@App.json(model=SearchDocument)
def document_default(self, request):
    id = get_required_param(request, 'id')
    doc_to_select = self.get_by_id(id)
    if not doc_to_select:
        return {"error": f"Document with id {id} not found"}
    else:
        return {
            "id": doc_to_select.id,
            "title": doc_to_select.title,
            "content": doc_to_select.content,
        }


@App.json(model=AddDocument)
def add_document_view(self, request):
    title = get_required_param(request,'title')
    content = get_required_param(request,'content')
    new_document=self.create(title=title,content=content)
    return {
        "message": "Document added successfully",
        "id": new_document.id,
        "title": new_document.title,
        "content": new_document.content
    }


@App.json(model=DeleteDocument)
def delete_document_view(self, request):
    id = get_required_param(request,'id')
    doc_to_delete= self.delete(id)
    if not doc_to_delete:
        return {"error": f"Document with id {id} not found"}
    return {
        "message": f"Document with id {id} deleted successfully"
    }


@App.json(model=UpdateDocument)
def add_document_view(self, request):
    id= get_required_param(request,'id')
    title = get_required_param(request,'title')
    content = get_required_param(request,'content')
    doc_to_select = self.get_by_id(id)
    if not doc_to_select:
        return {"error": f"Document with id {id} not found"}
    new_document=self.create(title=title,content=content)
    return {
        "message": "Document added successfully",
        "id": new_document.id,
        "title": new_document.title,
        "content": new_document.content
    }