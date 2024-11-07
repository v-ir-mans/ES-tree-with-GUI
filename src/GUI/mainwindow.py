# This Python file uses the following encoding: utf-8
import sys
import random

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from PySide6.QtGui import QImage, QIcon

from functions import buttons as bf
from Tree import treefunc as treef

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
        self.ui.excelButton.clicked.connect(self.openExcel)

        self.ui.mermaidButton.clicked.connect(self.marmaidToClipboard)
        self.ui.saveptlButton.clicked.connect(self.savePTL)
        self.ui.savevisButton.clicked.connect(self.saveVisualization)
        self.ui.savevisSVGButton.clicked.connect(self.saveVisualizationSVG)



        self.tree=treef.Tree()
    
    def marmaidToClipboard(self):
        if self.tree.is_trained:
            pyperclip.copy(self.tree.mermaid())
            self.status(f"Mermaid copied")
    
    def open_file_and_initialize_tree(self, path):
        if path:
            # Enable UI elements
            self.ui.optionbox.setEnabled(True)
            self.ui.dataTableScroll.setEnabled(True)

            # Initialize the tree, create data table, and train
            self.createDataTable()
            self.tree.train()

            # Update UI based on training status
            if self.tree.is_trained:
                self.ui.buttonBottomFrame.setEnabled(True)
                self.ui.logicText.setText(self.tree.logic_text)
                self.ui.likumuText.setText(self.tree.getLaws())


        else:
            # Disable UI elements if no path is provided
            self.ui.optionbox.setEnabled(False)
            self.ui.dataTableScroll.setEnabled(False)

    def openCSV(self):
        path = bf.open_file_dialog(self)
        if path:
            entries = treef.read_csv_to_entries(path)
            self.tree = treef.Tree(entries)
            self.open_file_and_initialize_tree(path)

    def openPTL(self):
        path = bf.open_file_dialog(self, "Pickle Files (*.ptl);;All Files (*)")
        if path:
            self.tree = treef.Tree.load_from_pickle(path)
            self.open_file_and_initialize_tree(path)

    def openExcel(self):
        path = bf.open_file_dialog(self, "Excel Files (*.xls *.xlsx *.xlsm *.xlsb *.odf *.ods *.odt);;All Files (*)")
        if path:
            entries = treef.read_excel_to_entries(path)
            self.tree = treef.Tree(entries)
            self.open_file_and_initialize_tree(path)




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

    def saveVisualizationSVG(self):
        save_path = bf.save_file_dialog(self, "svg", "SVG Files (*.svg);;All Files (*)", "koks")

        if save_path:
            svg = self.tree.visualizeSVG()

            svg.saveas(save_path, True)

            self.status(f"SVG saved in {save_path}")

    def status(self, messege):
        self.statusBar().showMessage(messege, timeout=5000) 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('icon.ico'))

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
