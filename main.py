from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.uic import loadUi
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("main.ui", self)

        self.current_path = None
        self.setWindowTitle(f"VC Pad - Untitled*")

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
        self.setWindowTitle(f"VC Pad - Untitled*")
        self.current_path = None


    def openFile(self):
        # fname = QFileDialog.getOpenFileName(self, "Open File", "C:\\Users\\USER\\Desktop\\dev\\personal\\text_editor", "Text files (*.txt)")
        fname = QFileDialog.getOpenFileName(self, "Open File", filter="Text files (*.txt)")  # default files path
        
        pathname_list = fname[0].split('/')
        self.setWindowTitle(f"VC Pad - {pathname_list[-1]}")

        with open(fname[0], "r") as f:
            text = f.read()
            self.textEdit.setText(text)
        self.current_path = fname[0]


    def saveFile(self):
        if self.current_path is not None:
            filetext = self.textEdit.toPlainText()
            with open(self.current_path, "w") as f:
                f.write(filetext)
        else:
            self.saveFileAs()


    def saveFileAs(self):
        # fname = QFileDialog.getSaveFileName(self, "Save File", "C:\\Users\\USER\\Desktop\\dev\\personal\\text_editor", "Text files (*.txt)")
        fname = QFileDialog.getSaveFileName(self, "Save File", filter="Text files (*.txt)")  # default files path
        text = self.textEdit.toPlainText()
        with open(fname[0], "w") as f:
            f.write(text)
        self.current_path = fname[0]

        pathname_list = fname[0].split('/')
        self.setWindowTitle(f"VC Pad - {pathname_list[-1]}")


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
        self.setStyleSheet("""
                QWidget{
                background-color: rgb(33, 33, 33);
                color: #ffffff;
                }
                QTextEdit{
                background-color: rgb(46, 46, 46);
                }
                QMenuBar::item:selected{
                color: #000000;
                }
            """)


    def lightMode(self):
        self.setStyleSheet("")


    def changeFontSize(self):
        print("Changed text's font size")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    app.exec_()