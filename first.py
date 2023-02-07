from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QLabel, QHBoxLayout,QLineEdit,QMessageBox
from os import system
from random import *
import sys
system('cls')
class First(QWidget):
    def __init__(self):
        super().__init__()
        self.add_obj=Window()
        self.btn=QPushButton("START",self)
        self.btn.clicked.connect(self.show_btn)
        self.btn.setFixedSize(200,50)
    
    def show_btn(self):
        self.add_obj.show()
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.words=["turkiston","qoraqamish","novza","chinorlar","haybatli"]
        self.setFixedSize(400,450)
        
        self.info_label=QLabel("So'zni toping!")
        self.info_label.setFixedSize(100,50)
        self.word=QLabel()
        self.editor=QLineEdit()
        self.editor.setPlaceholderText("So'z kiriting...")
        self.editor.setFixedSize(120,30)
        
        self.f_h_lay=QHBoxLayout()
        self.f_h_lay.addStretch()
        self.f_h_lay.addWidget(self.info_label)
        self.f_h_lay.addStretch()
        
        self.s_h_lay=QHBoxLayout()
        self.s_h_lay.addStretch()
        self.s_h_lay.addWidget(self.word)
        self.s_h_lay.addStretch()
        
        self.th_h_lay=QHBoxLayout()
        self.th_h_lay.addStretch()
        self.th_h_lay.addWidget(self.editor)
        self.th_h_lay.addStretch()
        
        self.v_lay=QVBoxLayout()
        self.v_lay.addLayout(self.f_h_lay)
        self.v_lay.addStretch()
        self.v_lay.addLayout(self.s_h_lay)
        self.v_lay.addStretch()
        self.v_lay.addLayout(self.th_h_lay)
        self.v_lay.addStretch()
        
        self.msg=QMessageBox()
        self.start=QPushButton("START")
        self.start.clicked.connect(self.start_button)
        self.check=QPushButton("CHECK")
        self.check.clicked.connect(self.check_button)
        self.close_win=QPushButton("CLOSE")
        self.close_win.clicked.connect(self.close_button)
        
        self.h_bottom_lay=QHBoxLayout()
        self.h_bottom_lay.addWidget(self.start)
        self.h_bottom_lay.addWidget(self.check)
        self.h_bottom_lay.addWidget(self.close_win)
        
        self.main_lay=QVBoxLayout()
        self.main_lay.addLayout(self.v_lay)
        self.main_lay.addLayout(self.h_bottom_lay)
        self.setLayout(self.main_lay)
    def start_button(self):
        self.holder=choice(self.words)
        self.word_sender="".join(sample(self.holder, len(self.holder)))
        self.word.setText(self.word_sender)
        self.word.adjustSize()    
    
    def check_button(self):
        if self.holder==self.editor.text():
            self.msg.setText("True")
        else:
            self.msg.setText("False")
        self.msg.show()
    def close_button(self):
        self.close()
        
app=QApplication(sys.argv)
win=First()
win.show()
app.exec_()
        
        