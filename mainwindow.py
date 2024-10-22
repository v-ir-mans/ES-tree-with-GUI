# This Python file uses the following encoding: utf-8
import sys
import random

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtGui import QPixmap, QImage

from functions import buttons as bf
from functions import treefunc as treef

import pyperclip

# ARMAND, NEAIZMIRSTI, KA FAILI TIEK ATV'ERTI NO HARDCODED MAPES

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        cur_emoji=random.choice(["😀", "😂", "😎", "😍", "🤔", "😜", "🥳", "😇"])
        self.ui.bigheading.setText(self.ui.bigheading.text()+cur_emoji)

        self.ui.csvButton.clicked.connect(self.openCSV)
        self.ui.ptlButton.clicked.connect(self.openPTL)

        self.ui.mermaidButton.clicked.connect(self.marmaidToClipboard)
        self.ui.saveptlButton.clicked.connect(self.savePTL)
        self.ui.savevisButton.clicked.connect(self.saveVisualization)



        self.tree=treef.Tree()
    
    def marmaidToClipboard(self):
        if self.tree.is_trained:
            pyperclip.copy(self.tree.mermaid())
    def openCSV(self):

        #path=bf.open_file_dialog(self)

        path=r"C:\Users\olive\Documents\2darbs\Backend\data\training\data.csv"
        
        if path:
            entries=treef.read_csv_to_entries(path)

            self.tree=treef.Tree(entries)

            self.ui.optionbox.setEnabled(True)
            self.ui.dataTableScroll.setEnabled(True)

            self.createDataTable()

            self.tree.train()

            if self.tree.is_trained:
                self.ui.buttonBottomFrame.setEnabled(True)

            '''
            pil_img=self.tree.visualize()
            q_image = self.pil_image_to_qt(pil_img)
            pixmap = QPixmap.fromImage(q_image)
            '''

        else:
            self.ui.optionbox.setEnabled(False)
            self.ui.dataTableScroll.setEnabled(False)
    
    def openPTL(self):

        path=bf.open_file_dialog(self, "Pickle Files (*.ptl);;All Files (*)")
        
        if path:

            self.tree=treef.Tree.load_from_pickle(path)

            self.ui.optionbox.setEnabled(True)
            self.ui.dataTableScroll.setEnabled(True)

            self.createDataTable()

            self.tree.train()

            if self.tree.is_trained:
                self.ui.buttonBottomFrame.setEnabled(True)

            '''
            pil_img=self.tree.visualize()
            q_image = self.pil_image_to_qt(pil_img)
            pixmap = QPixmap.fromImage(q_image)
            '''

        else:
            self.ui.optionbox.setEnabled(False)
            self.ui.dataTableScroll.setEnabled(False)

    def pil_image_to_qt(self, pil_image):
        # Convert PIL Image to a byte array
        data = pil_image.convert("RGBA").tobytes("raw", "RGBA")
        
        # Create a QImage from the byte data
        q_image = QImage(data, pil_image.width, pil_image.height, QImage.Format_RGBA8888)
        return q_image

    def createDataTable(self):
        table=self.ui.dataTable
        entries=self.tree.training_entries
        

        columns=entries.getAttrib()
        columns.append("Klase")
        print(columns)

        ylen=len(entries)
        xlen=len(columns)
        
        table.setRowCount(ylen)
    
        table.setColumnCount(xlen)

        table.setHorizontalHeaderLabels(columns)

        for y, e in enumerate(entries):
            for x, i in enumerate(e.attributes_dict.values()):
                table.setItem(y, x, QTableWidgetItem(str(i)))
            table.setItem(y, xlen-1, QTableWidgetItem(e.klase))

    def savePTL(self):
        save_path=bf.save_file_dialog(self, "ptl","Pickle Files (*.ptl);;All Files (*)")

        if save_path:
            self.tree.save_as_pickle(save_path)

    def saveVisualization(self):
        # Open file dialog with PNG filter
        save_path = bf.save_file_dialog(self, "png", "PNG Files (*.png);;All Files (*)", "koks")

        if save_path:
            # Convert PIL image to Qt and save as PNG
            pil_image = self.tree.visualize()
            qt_image = self.pil_image_to_qt(pil_image)
            qt_image.save(save_path, "PNG")

            self.status(f"Image saved in {save_path}")

    def status(self, messege):
        self.statusBar().showMessage(messege, timeout=5000) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
