from commands import *
from model import Model
class Controller:
    def __init__(self, document):
        self.document = document
        self.history_list = []
        self.history_list_counter = -1

    def insert(self, string_to_add, position):
        command = Insert(string_to_add, position)
        self.document = command.doIt(self.document)
        self.history_list.append(command)
        self.history_list_counter += 1


    def delete(self, start_position, end_position):
        command = Delete(start_position, end_position)
        self.document = command.doIt(self.document)
        self.history_list.append(command)
        self.history_list_counter += 1

    def undo(self):
        self.document = self.history_list[self.history_list_counter].redoIt(self.document)
        self.history_list_counter -= 1

    def redo(self):
        self.document = self.history_list[self.history_list_counter + 1].doIt(self.document)
        self.history_list_counter += 1

    def save_document(self, new_document):
        self.document = new_document
