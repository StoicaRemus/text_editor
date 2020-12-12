from controller import Controller

document = "this is a simple string"

def main(document):

    controll = Controller(document)
    controll.insert('TEST', 10)
    print(f"1 :  {controll.document}")
    controll.insert('START', 0)
    print(f"2 :  {controll.document}")
    controll.delete(0, 4)
    print(f"3 :  {controll.document}")
    controll.insert('om', 5)
    print(f"4 :  {controll.document}")
    print(f"Counter is: {controll.history_list_counter}")
    controll.undo()
    print(f"5 undo : {controll.document}")
    controll.undo()
    print(f"6 undo : {controll.document}")
    controll.redo()
    print(f"7 redo: {controll.document}")
    controll.redo()
    print(f"8 redo: {controll.document}")

    return controll.document   ### return saved document
    # controll.undo()
    # controll.redo()


if __name__ == "__main__":
    document = main(document)

    print(f"\nFinal document : {document}")