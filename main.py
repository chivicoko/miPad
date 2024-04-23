from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)

        self.actionNew.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionSave_As.triggered.connect(self.saveFileAs)
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)
        self.actionCopy.triggered.connect(self.copy)
        self.actionCUt.triggered.connect(self.cut)
        self.actionPaste.triggered.connect(self.paste)
        self.actionDark_Mode.triggered.connect(self.darkMode)
        self.actionLight_Mode.triggered.connect(self.lightMode)
        self.actionChange_FontSize.triggered.connect(self.changeFontSize)

    def newFile(self):
        self.textEdit.clear()
        self.setWindowTitle("Untitled")

    def openFile(self):
        # fname = QFileDialog.getOpenFileName(self, "Open File", "C:\\Users\\USER\\Desktop\\dev\\personal\\text_editor", "Text files (*.txt)")
        fname = QFileDialog.getOpenFileName(self, "Open File", filter="Text files (*.txt)")  # default files path
        self.setWindowTitle(fname[0])
        with open(fname[0], "r") as f:
            text = f.read()
            self.textEdit.setText(text)

    def saveFile(self):
        print("Saved file")

    def saveFileAs(self):
        print("Saved file as")

    def undo(self):
        self.textEdit.undo()

    def redo(self):
        self.textEdit.redo()

    def copy(self):
        self.textEdit.copy()

    def cut(self):
        self.textEdit.cut()

    def paste(self):
        self.textEdit.paste()

    def darkMode(self):
        print("Dark Mode activated")

    def lightMode(self):
        print("Light Mode activated")

    def changeFontSize(self):
        print("Changed text's font size")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    app.exec_()