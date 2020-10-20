#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 18:45:53 2020

@author: delta-coder
"""

from pytube import YouTube
import sys
import subprocess

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(670, 163)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_total = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_total.setObjectName("verticalLayout_total")
        self.verticalLayout_top = QtWidgets.QVBoxLayout()
        self.verticalLayout_top.setObjectName("verticalLayout_top")
        self.horizontalLayout_input = QtWidgets.QHBoxLayout()
        self.horizontalLayout_input.setObjectName("horizontalLayout_input")
        self.label_ytlink = QtWidgets.QLabel(self.centralwidget)
        self.label_ytlink.setObjectName("label_ytlink")
        self.horizontalLayout_input.addWidget(self.label_ytlink)
        self.lineEdit_ytlink = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_ytlink.setInputMask("")
        self.lineEdit_ytlink.setText("")
        self.lineEdit_ytlink.setObjectName("lineEdit_ytlink")
        self.horizontalLayout_input.addWidget(self.lineEdit_ytlink)
        self.verticalLayout_commandLinkButtons = QtWidgets.QVBoxLayout()
        self.verticalLayout_commandLinkButtons.setObjectName("verticalLayout_commandLinkButtons")
        self.commandLinkButton_audio = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_audio.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_audio.setSizePolicy(sizePolicy)
        self.commandLinkButton_audio.setObjectName("commandLinkButton_audio")
        self.verticalLayout_commandLinkButtons.addWidget(self.commandLinkButton_audio)
        self.commandLinkButton_video = QtWidgets.QCommandLinkButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.commandLinkButton_video.sizePolicy().hasHeightForWidth())
        self.commandLinkButton_video.setSizePolicy(sizePolicy)
        self.commandLinkButton_video.setObjectName("commandLinkButton_video")
        self.verticalLayout_commandLinkButtons.addWidget(self.commandLinkButton_video)
        self.horizontalLayout_input.addLayout(self.verticalLayout_commandLinkButtons)
        self.verticalLayout_top.addLayout(self.horizontalLayout_input)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_top.addWidget(self.progressBar)
        self.verticalLayout_total.addLayout(self.verticalLayout_top)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YTDownloader"))
        self.label_ytlink.setText(_translate("MainWindow", "YouTube Link:"))
        self.lineEdit_ytlink.setPlaceholderText(_translate("MainWindow", "Hier eingeben..."))
        self.commandLinkButton_audio.setText(_translate("MainWindow", "Audio"))
        self.commandLinkButton_video.setText(_translate("MainWindow", "Video"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec_())