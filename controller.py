from commands import *
# from model import Model

def printDocument(function):

    def proxy(*argv, **kwargs):
        result = function(*argv, **kwargs)
        print(argv[0].document)
        return result
    return proxy

class Controller:
    def __init__(self, document):
        self.document = document
        self.history_list = []
        self.history_list_counter = -1

    @printDocument
    def insert(self, string_to_add, position):
        command = Insert(string_to_add, position)
        self.document = command.doIt(self.document)
        self.history_list[self.history_list_counter + 1:] = []
        self.history_list.append(command)
        self.history_list_counter = len(self.history_list) - 1

    @printDocument
    def delete(self, start_position, end_position):
        command = Delete(start_position, end_position)
        self.document = command.doIt(self.document)
        self.history_list[self.history_list_counter + 1:] = []
        self.history_list.append(command)
        # self.history_list_counter += 1
        self.history_list_counter = len(self.history_list) - 1

    @printDocument
    def undo(self):
        if self.history_list_counter == -1: return
        self.document = self.history_list[self.history_list_counter].undoIt(self.document)
        # self.document = self.history_list[self.history_list_counter].undoIt(self.document)
        self.history_list_counter -= 1

    @printDocument
    def redo(self):
        if self.history_list_counter == len(self.history_list) - 1: return
        self.history_list_counter += 1
        self.document = self.history_list[self.history_list_counter].doIt(self.document)

    def save_document(self, new_document):
        self.document = new_document
