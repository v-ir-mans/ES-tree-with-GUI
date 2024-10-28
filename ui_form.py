# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QStatusBar, QTableWidget, QTableWidgetItem,
    QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1384, 591)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setEnabled(True)
        self.bigheading = QLabel(self.centralwidget)
        self.bigheading.setObjectName(u"bigheading")
        self.bigheading.setGeometry(QRect(20, 0, 861, 51))
        font = QFont()
        font.setPointSize(22)
        self.bigheading.setFont(font)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 70, 761, 51))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget_2 = QWidget(self.frame)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(0, 0, 761, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.csvButton = QPushButton(self.horizontalLayoutWidget_2)
        self.csvButton.setObjectName(u"csvButton")

        self.horizontalLayout_2.addWidget(self.csvButton)

        self.excelButton = QPushButton(self.horizontalLayoutWidget_2)
        self.excelButton.setObjectName(u"excelButton")
        self.excelButton.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.excelButton)

        self.ptlButton = QPushButton(self.horizontalLayoutWidget_2)
        self.ptlButton.setObjectName(u"ptlButton")
        self.ptlButton.setEnabled(True)

        self.horizontalLayout_2.addWidget(self.ptlButton)

        self.dataTableScroll = QScrollArea(self.centralwidget)
        self.dataTableScroll.setObjectName(u"dataTableScroll")
        self.dataTableScroll.setEnabled(False)
        self.dataTableScroll.setGeometry(QRect(790, 70, 571, 491))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataTableScroll.sizePolicy().hasHeightForWidth())
        self.dataTableScroll.setSizePolicy(sizePolicy)
        self.dataTableScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 569, 489))
        self.dataTable = QTableWidget(self.scrollAreaWidgetContents)
        if (self.dataTable.columnCount() < 5):
            self.dataTable.setColumnCount(5)
        if (self.dataTable.rowCount() < 5):
            self.dataTable.setRowCount(5)
        self.dataTable.setObjectName(u"dataTable")
        self.dataTable.setGeometry(QRect(0, 0, 571, 491))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.dataTable.sizePolicy().hasHeightForWidth())
        self.dataTable.setSizePolicy(sizePolicy1)
        self.dataTable.setRowCount(5)
        self.dataTable.setColumnCount(5)
        self.dataTableScroll.setWidget(self.scrollAreaWidgetContents)
        self.optionbox = QScrollArea(self.centralwidget)
        self.optionbox.setObjectName(u"optionbox")
        self.optionbox.setGeometry(QRect(20, 130, 761, 431))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.optionbox.sizePolicy().hasHeightForWidth())
        self.optionbox.setSizePolicy(sizePolicy2)
        self.optionbox.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 759, 429))
        self.scrollArea = QScrollArea(self.scrollAreaWidgetContents_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 10, 741, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 739, 359))
        self.logicText = QTextEdit(self.scrollAreaWidgetContents_3)
        self.logicText.setObjectName(u"logicText")
        self.logicText.setGeometry(QRect(0, 40, 741, 321))
        font1 = QFont()
        font1.setPointSize(11)
        self.logicText.setFont(font1)
        self.bigheading_2 = QLabel(self.scrollAreaWidgetContents_3)
        self.bigheading_2.setObjectName(u"bigheading_2")
        self.bigheading_2.setGeometry(QRect(10, 0, 731, 31))
        font2 = QFont()
        font2.setPointSize(14)
        self.bigheading_2.setFont(font2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)
        self.buttonBottomFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.buttonBottomFrame.setObjectName(u"buttonBottomFrame")
        self.buttonBottomFrame.setEnabled(False)
        self.buttonBottomFrame.setGeometry(QRect(10, 380, 741, 41))
        self.buttonBottomFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttonBottomFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayoutWidget = QWidget(self.buttonBottomFrame)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 741, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.savevisButton = QPushButton(self.horizontalLayoutWidget)
        self.savevisButton.setObjectName(u"savevisButton")

        self.horizontalLayout.addWidget(self.savevisButton)

        self.savevisSVGButton = QPushButton(self.horizontalLayoutWidget)
        self.savevisSVGButton.setObjectName(u"savevisSVGButton")

        self.horizontalLayout.addWidget(self.savevisSVGButton)

        self.mermaidButton = QPushButton(self.horizontalLayoutWidget)
        self.mermaidButton.setObjectName(u"mermaidButton")

        self.horizontalLayout.addWidget(self.mermaidButton)

        self.saveptlButton = QPushButton(self.horizontalLayoutWidget)
        self.saveptlButton.setObjectName(u"saveptlButton")

        self.horizontalLayout.addWidget(self.saveptlButton)

        self.optionbox.setWidget(self.scrollAreaWidgetContents_2)
        self.showoffabel = QLabel(self.centralwidget)
        self.showoffabel.setObjectName(u"showoffabel")
        self.showoffabel.setGeometry(QRect(20, 40, 171, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.bigheading.setText(QCoreApplication.translate("MainWindow", u"Information gain l\u0113mumu koks", None))
        self.csvButton.setText(QCoreApplication.translate("MainWindow", u"Pievienot .csv", None))
        self.excelButton.setText(QCoreApplication.translate("MainWindow", u"Pievienot Excel", None))
        self.ptlButton.setText(QCoreApplication.translate("MainWindow", u"Pievienot .ptl", None))
        self.bigheading_2.setText(QCoreApplication.translate("MainWindow", u"Datora lo\u0123ika, veidojot koku:", None))
        self.savevisButton.setText(QCoreApplication.translate("MainWindow", u"Saglap\u0101t koku .png", None))
        self.savevisSVGButton.setText(QCoreApplication.translate("MainWindow", u"Saglap\u0101t koku .svg", None))
        self.mermaidButton.setText(QCoreApplication.translate("MainWindow", u"Kop\u0113t mermaid", None))
        self.saveptlButton.setText(QCoreApplication.translate("MainWindow", u"Saglab\u0101t .ptl", None))
        self.showoffabel.setText(QCoreApplication.translate("MainWindow", u"veidojis Armands Vagalis", None))
    # retranslateUi

