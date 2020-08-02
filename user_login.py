import sqlite3

import sys

from PyQt5 import QtWidgets

#First,Create a user.You can do that user in your idle or in your data base.  





class Window(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.connection()

        self.init_ui()

    def connection(self):
    
        con = sqlite3.connect("database.db")

        self.cursor =con.cursor() 

        self.cursor.execute("Create Table If Not Exists Users(Name TEXT,Password TEXT)")

       


        con.commit()


    def init_ui(self):

        self.user_name = QtWidgets.QLineEdit()
        self.password = QtWidgets.QLineEdit()
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login = QtWidgets.QPushButton("Login")
        self.access = QtWidgets.QLabel("")

        v_box =QtWidgets.QVBoxLayout()

        v_box.addWidget(self.user_name)
        v_box.addWidget(self.password)
        v_box.addWidget(self.access)
        v_box.addStretch()
        v_box.addWidget(self.login)

        h_box = QtWidgets.QHBoxLayout()

        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)

        self.login.clicked.connect(self.login_)


        self.show()


    def login_(self):

        

        name = self.user_name.text()

        pas = self.password.text()

        self.cursor.execute("Select * From Users where Name =? and Password = ?",(name,pas))

        data = self.cursor.fetchall()

        if len(data) == 0:

            self.access.setText("There is no such user.\nPlease,Try Again.")


        else:
            
            self.access.setText("Welcome" + name)    




app = QtWidgets.QApplication(sys.argv)

window = Window()

sys.exit(app.exec_())














    