class Insert:
    def __init__(self, string_to_add, position):
        self.string_to_add = string_to_add
        self.position = position

    def doIt(self, document):
        new_document = document[:self.position] + self.string_to_add + document[self.position:]
        return new_document

    def redoIt(self, document):
        old_document = document[:self.position] + document[self.position + len(self.string_to_add):]
        return old_document

class Delete:
    def __init__(self, start_position, end_position):
        self.start_position = start_position
        self.end_position = end_position
        self.deleted_string = None

    def doIt(self, document):
        self.deleted_string = document[self.start_position:self.end_position + 1]
        new_document = document[:self.start_position] + document[self.end_position + 1:]
        return new_document

    def redoIt(self, document):
        old_document = document[:self.start_position] + self.deleted_string + document[self.start_position:]
        return old_document
