from controller import Controller

document = ""

def main(document):

    controll = Controller(document)
    controll.insert('TEST', 10)
    # print(f"1 :  {controll.document}")
    controll.insert('START', 0)
    # print(f"2 :  {controll.document}")
    controll.delete(0, 4)
    # print(f"3 :  {controll.document}")
    # controll.insert('om', 5)
    # print(f"4 :  {controll.document}")
    # print(f"Counter is: {controll.history_list_counter}")
    # controll.undo()
    # print(f"5 undo : {controll.document}")
    # controll.undo()
    # print(f"6 undo : {controll.document}")
    # controll.redo()
    # print(f"7 redo: {controll.document}")
    # controll.redo()
    # print(f"8 redo: {controll.document}")
    # controll.insert('1', 0)
    # controll.insert(' 2', 1)
    # controll.insert(' 3', 4)
    # controll.undo()
    # controll.undo()
    # controll.insert('6', 2)
    # controll.redo()
    # controll.redo()
    # controll.undo()
    # controll.undo()
    # controll.redo()
    #


    return controll.document   ### return saved document
    # controll.undo()
    # controll.redo()


if __name__ == "__main__":
    document = main(document)
