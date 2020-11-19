from project_Document_Management.category import Category
from project_Document_Management.document import Document
from project_Document_Management.topic import Topic


class Storage:

    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def cat_id(self, category_id: int):
        return [x for x in self.categories if x.id == category_id][0]

    def top_id(self, topic_id: int):
        return [x for x in self.topics if x.id == topic_id][0]

    def doc_id(self, document_id: int):
        return [x for x in self.documents if x.id == document_id][0]

    def edit_category(self, category_id: int, new_name: str):
        current = [x for x in self.categories if x.id == category_id][0]
        current.name = new_name

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.top_id(topic_id)
        topic.topic = new_topic
        topic.storage_folder = new_storage_folder

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.doc_id(document_id)
        document.file_name = new_file_name

    def delete_category(self, category_id):
        category = self.cat_id(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        current = [x for x in self.topics if x.id == topic_id][0]
        self.topics.remove(current)

    def delete_document(self, document_id):
        current = self.doc_id(document_id)
        self.documents.remove(current)

    def get_document(self, document_id):
        return self.doc_id(document_id)

    def __repr__(self):
        result = ''
        for document in self.documents:
            result += f'{document.__repr__()}\n'

        return result
