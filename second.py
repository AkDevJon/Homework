from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QLabel, QHBoxLayout,QLineEdit,QMessageBox
from os import system
from random import *
import sys
system('cls')

class Start(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(150,80)
        self.add_obj=MainBox()
        self.btn=QPushButton("START",self)
        self.btn.setFixedSize(100,50)
        self.btn.clicked.connect(self.show_win)
    def show_win(self):
        self.add_obj.show()
     
class MainBox(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,350)
        self.lst_of_colors=["yellow","green","black","red","blue","orange","pink"]
        
        self.info_label=QLabel("")
        self.editor=QLineEdit()
        self.editor.setPlaceholderText("Qaysi rangligini yozing...")
        self.answer=QLabel("")
        
        
        
        
        self.start=QPushButton("START")
        self.start.clicked.connect(self.start_button)
        self.check=QPushButton("CHECK")
        self.check.clicked.connect(self.check_button)
        self.close_win=QPushButton("CLOSE")
        self.close_win.clicked.connect(self.close_button)
        
        self.f_h_lay=QHBoxLayout()
        self.f_h_lay.addStretch()
        self.f_h_lay.addWidget(self.info_label)
        self.f_h_lay.addStretch()
        
        self.s_h_lay=QHBoxLayout()
        self.s_h_lay.addStretch()
        self.s_h_lay.addWidget(self.editor)
        self.s_h_lay.addStretch()
        
        self.th_h_lay=QHBoxLayout()
        self.th_h_lay.addStretch()
        self.th_h_lay.addWidget(self.answer)
        self.th_h_lay.addStretch()
        
        self.v_lay=QVBoxLayout()
        self.v_lay.addLayout(self.f_h_lay)
        self.v_lay.addStretch()
        self.v_lay.addLayout(self.s_h_lay)
        self.v_lay.addStretch()
        self.v_lay.addLayout(self.th_h_lay)
        self.v_lay.addStretch()
        
        self.main_lay=QVBoxLayout()
        self.h_bottom_lay=QHBoxLayout()
        self.h_bottom_lay.addWidget(self.start)
        self.h_bottom_lay.addWidget(self.check)
        self.h_bottom_lay.addWidget(self.close_win)
        self.main_lay.addLayout(self.v_lay)
        self.main_lay.addLayout(self.h_bottom_lay)
        self.setLayout(self.main_lay)
    
    def start_button(self):
        self.info_label.setText(choice(self.lst_of_colors))
        self.chosen_color=choice(self.lst_of_colors)
        self.info_label.setStyleSheet(f"color: {self.chosen_color}")
        
    def check_button(self):
        if self.editor.text()==self.chosen_color:
            print("True")
        else:
            print("False")
        
        self.editor.clear()
    
    def close_button(self):
        self.close()        
app=QApplication(sys.argv)
win=Start()
win.show()
app.exec_()