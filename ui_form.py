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
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1384, 591)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutMain = QVBoxLayout(self.centralwidget)
        self.verticalLayoutMain.setObjectName(u"verticalLayoutMain")
        self.bigheading = QLabel(self.centralwidget)
        self.bigheading.setObjectName(u"bigheading")
        font = QFont()
        font.setPointSize(22)
        self.bigheading.setFont(font)

        self.verticalLayoutMain.addWidget(self.bigheading)

        self.showoffabel = QLabel(self.centralwidget)
        self.showoffabel.setObjectName(u"showoffabel")

        self.verticalLayoutMain.addWidget(self.showoffabel)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.csvButton = QPushButton(self.frame)
        self.csvButton.setObjectName(u"csvButton")

        self.horizontalLayout_2.addWidget(self.csvButton)

        self.excelButton = QPushButton(self.frame)
        self.excelButton.setObjectName(u"excelButton")

        self.horizontalLayout_2.addWidget(self.excelButton)

        self.ptlButton = QPushButton(self.frame)
        self.ptlButton.setObjectName(u"ptlButton")

        self.horizontalLayout_2.addWidget(self.ptlButton)


        self.verticalLayoutMain.addWidget(self.frame)

        self.horizontalLayoutData = QHBoxLayout()
        self.horizontalLayoutData.setObjectName(u"horizontalLayoutData")
        self.optionbox = QScrollArea(self.centralwidget)
        self.optionbox.setObjectName(u"optionbox")
        self.optionbox.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.verticalLayoutOption = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayoutOption.setObjectName(u"verticalLayoutOption")
        self.bigheading_2 = QLabel(self.scrollAreaWidgetContents_2)
        self.bigheading_2.setObjectName(u"bigheading_2")
        font1 = QFont()
        font1.setPointSize(14)
        self.bigheading_2.setFont(font1)

        self.verticalLayoutOption.addWidget(self.bigheading_2)

        self.logicText = QTextEdit(self.scrollAreaWidgetContents_2)
        self.logicText.setObjectName(u"logicText")
        font2 = QFont()
        font2.setPointSize(11)
        self.logicText.setFont(font2)

        self.verticalLayoutOption.addWidget(self.logicText)

        self.buttonBottomFrame = QFrame(self.scrollAreaWidgetContents_2)
        self.buttonBottomFrame.setObjectName(u"buttonBottomFrame")
        self.horizontalLayout = QHBoxLayout(self.buttonBottomFrame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.savevisButton = QPushButton(self.buttonBottomFrame)
        self.savevisButton.setObjectName(u"savevisButton")

        self.horizontalLayout.addWidget(self.savevisButton)

        self.savevisSVGButton = QPushButton(self.buttonBottomFrame)
        self.savevisSVGButton.setObjectName(u"savevisSVGButton")

        self.horizontalLayout.addWidget(self.savevisSVGButton)

        self.mermaidButton = QPushButton(self.buttonBottomFrame)
        self.mermaidButton.setObjectName(u"mermaidButton")

        self.horizontalLayout.addWidget(self.mermaidButton)

        self.saveptlButton = QPushButton(self.buttonBottomFrame)
        self.saveptlButton.setObjectName(u"saveptlButton")

        self.horizontalLayout.addWidget(self.saveptlButton)


        self.verticalLayoutOption.addWidget(self.buttonBottomFrame)

        self.optionbox.setWidget(self.scrollAreaWidgetContents_2)

        self.horizontalLayoutData.addWidget(self.optionbox)

        self.dataTableScroll = QScrollArea(self.centralwidget)
        self.dataTableScroll.setObjectName(u"dataTableScroll")
        self.dataTableScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.verticalLayoutDataTable = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayoutDataTable.setObjectName(u"verticalLayoutDataTable")
        self.dataTable = QTableWidget(self.scrollAreaWidgetContents)
        self.dataTable.setObjectName(u"dataTable")
        self.dataTable.setRowCount(5)
        self.dataTable.setColumnCount(5)

        self.verticalLayoutDataTable.addWidget(self.dataTable)

        self.dataTableScroll.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayoutData.addWidget(self.dataTableScroll)


        self.verticalLayoutMain.addLayout(self.horizontalLayoutData)

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
        self.showoffabel.setText(QCoreApplication.translate("MainWindow", u"veidojis Armands Vagalis", None))
        self.csvButton.setText(QCoreApplication.translate("MainWindow", u"Pievienot .csv", None))
        self.excelButton.setText(QCoreApplication.translate("MainWindow", u"Pievienot Excel", None))
        self.ptlButton.setText(QCoreApplication.translate("MainWindow", u"Pievienot .ptl", None))
        self.bigheading_2.setText(QCoreApplication.translate("MainWindow", u"Datora lo\u0123ika, veidojot koku:", None))
        self.savevisButton.setText(QCoreApplication.translate("MainWindow", u"Saglap\u0101t koku .png", None))
        self.savevisSVGButton.setText(QCoreApplication.translate("MainWindow", u"Saglap\u0101t koku .svg", None))
        self.mermaidButton.setText(QCoreApplication.translate("MainWindow", u"Kop\u0113t mermaid", None))
        self.saveptlButton.setText(QCoreApplication.translate("MainWindow", u"Saglab\u0101t .ptl", None))
    # retranslateUi

