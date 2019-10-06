#!/usr/bin/env python

import random
from os import getcwd
from sys import argv, exit
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QLineEdit,\
    QTextEdit, QRadioButton, QDoubleSpinBox, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon

class Cipher_App(object):
    def __init__(self):
        self.btn_style = """font:bold italic 20px;
                            color:#8b0000;
                            background-color:transparent;
                            border:2px outset #8b0000;
                            border-radius:14%;
                            padding:10%;
                            selection-color:#8b0000;
                            selection-background-color:transparent;"""
        self.ent_style = """background-color:transparent;
                            border:2px outset #808000;
                            border-radius:20%;
                            padding:10%;
                            color:black;
                            font:italic 18px;"""
        self.lbl_style = """background-color:transparent;
                            padding:4%;
                            text-align:center;
                            color:#8b0000;
                            font:bold italic 20px;"""
        self.logo_style = """background-color:transparent;
                             border-color:transparent;
                             border-radius:50%;"""
        self.disable_style = """font:bold italic 20px;
                                background-color:#dcdcdc;
                                border:2px dotted #dcdcdc;
                                border-radius:20%;"""
        self.FORM_style = """background-color:#98fb98;"""
        self.plane_2 = "abcdefghijklmnopqrstuvwxyz"
        self.plane_1 = "NOPQRSTUVWXYZABCDEFGHIJKLM"
        self.plane_4 = "0123456789"
        self.plane_3 = " .:;!$@?&,"
        self.steps = "aAbBcCd1DeEfFgG2hHiIjJ3kKlLmM4nNoOpP5qQrRsS6tTuUvVwWxX8yYzZ9"
        self.title = 'CHE-Cipher'
        self.wico = QIcon(getcwd() + '\\imgs\\CHE_g.ico')
        self.pxm = QPixmap(getcwd() + '\\imgs\\CHE_g.png')
        self.path = ""


    def Main_UI(self, FORM_1):
        FORM_1.setGeometry( 40, 40, self.pxm.width() + 700, self.pxm.height() + 400 )
        FORM_1.setWindowTitle( self.title )
        FORM_1.setWindowIcon( self.wico )
        FORM_1.setMaximumSize( self.pxm.width() + 700, self.pxm.height() + 400 )
        FORM_1.setMinimumSize( self.pxm.width() + 700, self.pxm.height() + 400 )
        FORM_1.setStyleSheet( self.FORM_style )
        #QLabel to set background(QPixmap)
        self.lbl_F = QLabel(FORM_1)
        self.lbl_F.setPixmap(self.pxm)
        self.lbl_F.setGeometry(350, 200, self.pxm.width(), self.pxm.height())
        #QLabel to show path from filedialog
        self.lbl_1 = QLabel(FORM_1)
        self.lbl_1.setGeometry(50, 10, 650, 60)
        self.lbl_1.setEnabled(False)
        self.lbl_1.setStyleSheet(self.disable_style)
        self.lbl_1.setText('File Path')
        #QLabel
        self.lbl_2 = QLabel(FORM_1)
        self.lbl_3 = QLabel(FORM_1)
        self.lbl_2.setText('Step :')
        self.lbl_3.setText('Add Step :')
        self.lbl_2.setGeometry(400, 80, 120, 40)
        self.lbl_3.setGeometry(400, 150, 120, 40)
        self.lbl_2.setStyleSheet(self.lbl_style)
        self.lbl_3.setStyleSheet(self.lbl_style)
        #QRadioButton to choose way
        self.rdo_1 = QRadioButton(FORM_1)
        self.rdo_1.clicked.connect(lambda:self.rdo1_state())
        self.rdo_1.move(10, 10)
        self.rdo_2 = QRadioButton(FORM_1)
        self.rdo_2.move(10, 160)
        self.rdo_2.setChecked(True)
        self.rdo_2.clicked.connect(lambda: self.rdo2_state())
        #QText to enter text
        self.txt_1 = QTextEdit(FORM_1)
        self.txt_1.setGeometry(50, 80, 300, 500)
        self.txt_1.setStyleSheet(self.ent_style)
        self.txt_1.setPlaceholderText('Enter text to encode or decode')
        #Create QPushButton
        self.btn_1 = QPushButton(FORM_1)
        self.btn_2 = QPushButton(FORM_1)
        self.btn_3 = QPushButton(FORM_1)
        self.btn_4 = QPushButton(FORM_1)
        self.btn_5 = QPushButton(FORM_1)
        self.btn_6 = QPushButton(FORM_1)
        self.btn_logo = QPushButton(FORM_1)
        #Buttons names
        self.btn_1.setText('Select')
        self.btn_2.setText('Encode')
        self.btn_3.setText('Decode')
        self.btn_4.setText('Cancel')
        self.btn_5.setText('Save')
        self.btn_6.setText('Show')
        #IsEnabled
        self.btn_1.setEnabled(False)
        self.btn_5.setEnabled(False)
        self.btn_6.setEnabled(False)
        #Geometry for Buttons
        self.btn_1.setGeometry(740, 40, 140, 60)
        self.btn_2.setGeometry(740, 190, 140, 60)
        self.btn_3.setGeometry(740, 340, 140, 60)
        self.btn_4.setGeometry(740, 490, 140, 60)
        self.btn_5.setGeometry(370, 490, 140, 60)
        self.btn_6.setGeometry(370, 400, 140, 60)
        self.btn_logo.setGeometry(350, 200, 200, 200)
        #Stylesheet for Buttons
        self.btn_1.setStyleSheet(self.disable_style)
        self.btn_2.setStyleSheet(self.btn_style)
        self.btn_3.setStyleSheet(self.btn_style)
        self.btn_4.setStyleSheet(self.btn_style)
        self.btn_5.setStyleSheet(self.disable_style)
        self.btn_6.setStyleSheet(self.disable_style)
        self.btn_logo.setStyleSheet(self.logo_style)
        #Buurons functions
        self.btn_1.clicked.connect(self.Select_File)
        self.btn_2.clicked.connect(self.How_Encode)
        self.btn_3.clicked.connect(self.How_Decode)
        self.btn_4.clicked.connect(FORM_1.close)
        self.btn_5.clicked.connect(self.Save)
        self.btn_6.clicked.connect(self.Show)
        self.btn_logo.clicked.connect(self.INFO)
        #QSpinBox
        self.spn_1 = QDoubleSpinBox(FORM_1)
        self.spn_1.setGeometry(540, 80, 100, 40)
        self.spn_1.setStyleSheet(self.btn_style)
        self.spn_1.setDecimals(0)
        self.spn_2 = QDoubleSpinBox(FORM_1)
        self.spn_2.setGeometry(540, 150, 100, 40)
        self.spn_2.setStyleSheet(self.btn_style)
        self.spn_2.setDecimals(0)


    #QFileDialog
    def Select_File(self):
        self.fdg = QFileDialog.getOpenFileNames(FORM_2, 'Select file','/', '*.txt')
        try:
            self.path = self.fdg[0][0]
            self.lbl_1.setText(self.path)
        except:
            self.lbl_1.setText('Warning : No Path')
            self.lbl_1.setStyleSheet('color:#ff0000;font:bold italic 20px;')


    def INFO(self):
        title = "CHECipher Informations"
        mesg = """{}, application to encrypt texts using Python.\n
                    Encryption algorithm was written via Python3.6\n
                    GUI was made via PyQt5-v5.10.1.\n
                    Version {} \n
                    Created By: Tarek Ghajary""".format(App.applicationName(), App.applicationVersion())
        self.msg_info = QMessageBox.information(FORM_1, title, mesg)

    #save text as file.txt function
    def Save(self):
        self.fdg_2 = QFileDialog.getSaveFileName(FORM_2, 'Save file', '/', '*.txt')
        try:
            self.save_path = self.fdg_2[0]
            with open(self.save_path, 'w') as file:
                try:
                    file.write(self.text_cipher)
                except:
                    file.write(self.origin_text)
                file.close()
                self.lbl_1.setText('Saved in : {}'.format(self.save_path))
                self.lbl_1.setStyleSheet('color:#228b22;font:bold italic 16px;')
        except:
            self.lbl_1.setText('No path to save file')
            self.lbl_1.setStyleSheet('color:#ff0000;font:bold italic 18px;')


    #Show text in textbox function
    def Show(self):
        if self.mod is "Encryption":
            self.txt_1.setText(self.text_cipher)
        elif self.mod is "Decryption":
            self.txt_1.setText(self.origin_text)


    #QRadioButton functions
    def rdo1_state(self):
        self.lbl_1.setStyleSheet(self.lbl_style)
        self.btn_1.setStyleSheet(self.btn_style)
        self.lbl_1.setEnabled(True)
        self.btn_1.setEnabled(True)
        self.txt_1.setStyleSheet(self.disable_style)
        self.btn_5.setStyleSheet(self.disable_style)
        self.txt_1.setEnabled(False)


    def rdo2_state(self):
        self.txt_1.setStyleSheet(self.ent_style)
        self.txt_1.setEnabled(True)
        self.lbl_1.setStyleSheet(self.disable_style)
        self.btn_1.setStyleSheet(self.disable_style)
        self.lbl_1.setEnabled(False)
        self.btn_1.setEnabled(False)

    #first step to encode-function
    def How_Encode(self):
        if self.rdo_1.isChecked():
            if self.path:
                self.file = open(self.path, 'r')
                self.text = self.file.read()
                self.step = int(self.spn_1.value())
                self.add_step = int(self.spn_2.value())
                self.lbl_1.clear()
                self.encodec = []
                self.cipher = []
                self.text_after_decodec = []
                self.Encodec(self.text, self.step, self.add_step)
                self.btn_5.setEnabled(True)
                self.btn_6.setEnabled(True)
                self.btn_5.setStyleSheet(self.btn_style)
                self.btn_6.setStyleSheet(self.btn_style)
            else:
                self.lbl_1.setText('No path to encryption that text.\nplease select file')
        elif self.rdo_2.isChecked():
            if self.txt_1.toPlainText():
                self.text = self.txt_1.toPlainText()
                self.step = int(self.spn_1.value())
                self.add_step = int(self.spn_2.value())
                self.txt_1.clear()
                self.encodec = []
                self.cipher = []
                self.text_after_decodec = []
                self.Encodec(self.text, self.step, self.add_step)
                self.btn_5.setEnabled(True)
                self.btn_6.setEnabled(True)
                self.btn_5.setStyleSheet(self.btn_style)
                self.btn_6.setStyleSheet(self.btn_style)
            else:
                self.lbl_1.setText('No text to encryption.\nplease enter text')
        self.mod = "Encryption"

    #first step to decode-functon
    def How_Decode(self):
        if self.rdo_1.isChecked():
            if self.path:
                self.file = open(self.path, 'r')
                self.text = self.file.read()
                self.step = int(self.spn_1.value())
                self.add_step = int(self.spn_2.value())
                self.lbl_1.clear()
                self.encodec = []
                self.cipher = []
                self.text_after_decodec = []
                self.Decodec(self.text, self.step, self.add_step)
                self.btn_5.setEnabled(True)
                self.btn_6.setEnabled(True)
                self.btn_5.setStyleSheet(self.btn_style)
                self.btn_6.setStyleSheet(self.btn_style)
            else:
                self.lbl_1.setText('No path to decryption that text.\nplease select file')
        elif self.rdo_2.isChecked():
            if self.txt_1.toPlainText():
                self.text = self.txt_1.toPlainText()
                self.step = int(self.spn_1.value())
                self.add_step = int(self.spn_2.value())
                self.txt_1.clear()
                self.encodec = []
                self.cipher = []
                self.text_after_decodec = []
                self.Decodec(self.text, self.step, self.add_step)
                self.btn_5.setEnabled(True)
                self.btn_6.setEnabled(True)
                self.btn_5.setStyleSheet(self.btn_style)
                self.btn_6.setStyleSheet(self.btn_style)
            else:
                self.lbl_1.setText('No text to decryption.\nplease enter text')
        self.mod = "Decryption"


    #Encodec function
    def Encodec(self, text='', step=0, step_plus=0):
        for letter in text:
            if letter in self.plane_1:
                letter = self.plane_2[self.plane_1.index(letter)]
                self.encodec.append(letter)
            elif letter in self.plane_2:
                letter = self.plane_1[self.plane_2.index(letter)]
                self.encodec.append(letter)
            elif letter in self.plane_3:
                letter = self.plane_4[self.plane_3.index(letter)]
                self.encodec.append(letter)
            elif letter in self.plane_4:
                letter = self.plane_3[self.plane_4.index(letter)]
                self.encodec.append(letter)
            else:
                letter = letter
                self.encodec.append(letter)
        for i in self.encodec:
            for j in range(step):
                s = random.choice(self.steps)
                self.cipher.append(s)
            step += step_plus
            self.cipher.append(i)
        self.text_cipher = "".join(self.cipher)
        if self.rdo_1.isChecked():
            self.txt_1.setText("Complete encryption,to save the cipher text as file.txt click 'Save'.\nTo Show the cipher text here click 'Show'")
            self.lbl_1.setText('Process is Completed')
            self.lbl_1.setStyleSheet('color:#32cd32;font:bold italic 20px;')
        elif self.rdo_2.isChecked():
            self.txt_1.setText("Complete process,to save the cipher text as file.txt click 'Save'.\nTo Show the cipher text here click 'Show'")
            self.lbl_1.setText('Process is Completed')
            self.lbl_1.setStyleSheet('color:#32cd32;font:bold italic 20px;')


    #Decodec function
    def Decodec(self, text='', step=0, step_plus=0):
        while step in range(len(text)):
            letter = text[step]
            if letter in self.plane_2:
                letter = self.plane_1[self.plane_2.index(letter)]
                self.text_after_decodec.append(letter)
            elif letter in self.plane_1:
                letter = self.plane_2[self.plane_1.index(letter)]
                self.text_after_decodec.append(letter)
            elif letter in self.plane_3:
                letter = self.plane_4[self.plane_3.index(letter)]
                self.text_after_decodec.append(letter)
            elif letter in self.plane_4:
                letter = self.plane_3[self.plane_4.index(letter)]
                self.text_after_decodec.append(letter)
            else:
                letter = letter
                self.text_after_decodec.append(letter)
            text = text[step+1:]
            step += step_plus
        self.origin_text = "".join(self.text_after_decodec)
        if self.rdo_1.isChecked():
            self.txt_1.setText("Complete process,to save the origin text as file.txt click 'Save'.\nTo show the origin text here click 'Show'")
            self.lbl_1.setText('Process is Completed')
            self.lbl_1.setStyleSheet('color:#32cd32;font:bold italic 20px;')
        elif self.rdo_2.isChecked():
            self.txt_1.setText("Complete process,to save the origin text as file.txt click 'Save'.\nTo show the origin text here click 'Show'")
            self.lbl_1.setText('Process is Completed')
            self.lbl_1.setStyleSheet('color:#32cd32;font:bold italic 20px;')


if __name__ == "__main__":
    App = QApplication(argv)
    App.setApplicationVersion('0.1.0 - 2019.1')
    App.setApplicationName('CHE-Cipher')
    FORM_1 = QWidget()
    FORM_2 = QWidget()
    Obj = Cipher_App()
    Obj.Main_UI(FORM_1)
    FORM_1.show()
    exit(App.exec_())
