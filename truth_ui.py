# -*- coding: utf-8 -*-

from truthUserInterface import UiTruthtableWindow
from truthtable import LogicalExpression, Row
from PyQt5.QtWidgets import *
import sys


class DataContainer:

    def __init__(self):
        self.func_list = []
        self.results = []
        self.given_rows = []
        self.given_generated = None  # Given table instance
        self.func_last = False  # If functions are the last columns

    def add_func(self, logexpr):
        self.func_list.append(logexpr)

    def add_result(self, res_obj):
        self.results.append(res_obj)

    def add_given_row(self, _row):
        self.given_rows.append(_row)

    def replace_func(self, index, new):
        self.func_list[index] = new

    def replace_given_row(self, index, new):
        self.given_rows[index] = new

    def del_func(self, index):
        self.func_list.pop(index)

    def clear_func(self):
        self.func_list = []

    def clearall(self):
        self.clear_func()
        self.results = []
        self.given_rows = []
        self.given_generated = None
        self.func_last = False


class UiTruthtableWindowNitro(UiTruthtableWindow):

    def __init__(self, _data_container):
        super().__init__()
        self.data_container = _data_container

    def bind(self):
        self.add_func_btn.clicked.connect(self.add_function)
        self.not_btn.clicked.connect(lambda: self.insert_func_char("~"))
        self.and_btn.clicked.connect(lambda: self.insert_func_char("/\\ "))
        self.or_btn.clicked.connect(lambda: self.insert_func_char("\\/ "))
        self.follow_btn.clicked.connect(lambda: self.insert_func_char("-> "))
        self.equal_btn.clicked.connect(lambda: self.insert_func_char("= "))
        self.xor_btn.clicked.connect(lambda: self.insert_func_char("^ "))
        self.x_var_btn.clicked.connect(lambda: self.insert_func_char("x "))
        self.y_var_btn.clicked.connect(lambda: self.insert_func_char("y "))
        self.closebrackets_btn.clicked.connect(lambda: self.insert_func_char(") "))
        self.z_var_btn.clicked.connect(lambda: self.insert_func_char("z "))
        self.w_var_btn.clicked.connect(lambda: self.insert_func_char("w "))
        self.a_var_btn.clicked.connect(lambda: self.insert_func_char("a "))
        self.b_var_btn.clicked.connect(lambda: self.insert_func_char("b "))
        self.c_var_btn.clicked.connect(lambda: self.insert_func_char("c "))
        self.d_var_btn.clicked.connect(lambda: self.insert_func_char("d "))
        self.zero_btn.clicked.connect(lambda: self.insert_func_char("0 "))
        self.one_btn.clicked.connect(lambda: self.insert_func_char("1 "))
        self.openbrackets_btn.clicked.connect(lambda: self.insert_func_char("("))

        self.func_list.itemActivated.connect(self.change_func)

    def generate_error(self, text):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.exec_()

    def add_function(self):
        entered = self.func_edit.text()
        if not entered.replace(" ", ""):
            return
        try:
            fnc = LogicalExpression(entered, check=True, unicode_support=True)
        except (TypeError, SyntaxError, NameError):
            self.generate_error("Invalid syntax of logical function.")
            return
        if fnc not in self.data_container.func_list:
            self.data_container.add_func(fnc)
            self.func_list.addItem(fnc.to_unicode())

    def insert_func_char(self, char):
        if char == ") " and self.func_edit.text()[-1] == " ":
            self.func_edit.backspace()
        self.func_edit.insert(char)

    def change_func(self, item):
        print(item.text())


class TruthWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.data_container = DataContainer()
        ui = UiTruthtableWindowNitro(self.data_container)
        ui.setupUi(self)
        ui.bind()
        self.ui = ui


if __name__ == '__main__':
    truth_app = QApplication(sys.argv)
    win = TruthWindow()
    win.show()

    sys.exit(truth_app.exec_())
