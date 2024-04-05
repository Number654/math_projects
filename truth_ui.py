# -*- coding: utf-8 -*-

from truthUserInterface import UiTruthtableWindow
from truthtable import LogicalExpression, DEFAULT_FUNC
from PyQt5.QtWidgets import *
import sys


def from_unicode(func_string):
    st = str(func_string)
    for v in DEFAULT_FUNC.keys():
        st = st.replace(v, DEFAULT_FUNC[v])
    return st


class DataContainer:

    def __init__(self):
        self.func_list = []
        self.raw_func_list = []
        self.results = []
        self.given_rows = []
        self.variables = set()
        self.given_generated = None  # Given table instance
        self.func_last = False  # If functions are the last columns

    def add_func(self, logexpr):
        self.func_list.append(logexpr)
        self.raw_func_list.append(logexpr.expression)
        self.variables.update(logexpr.variables)

    def add_result(self, res_obj):
        self.results.append(res_obj)

    def add_given_row(self, _row):
        self.given_rows.append(_row)

    def replace_func(self, index, new):
        self.func_list[index] = new
        self.raw_func_list[index] = new.expression

    def replace_given_row(self, index, new):
        self.given_rows[index] = new

    def del_func(self, index):
        self.func_list.pop(index)
        self.raw_func_list.pop(index)
        self.variables = set()
        for f in self.func_list:
            self.variables.update(f.variables)

    def clear_func(self):
        self.func_list = []
        self.variables = set()

    def clearall(self):
        self.clear_func()
        self.results = []
        self.given_rows = []
        self.given_generated = None
        self.func_last = False


class UiTruthtableWindowNitro(UiTruthtableWindow):

    def __init__(self, parent, _data_container):
        super().__init__()
        self.parent = parent
        self.data_container = _data_container

    def bind(self):
        self.add_func_btn.clicked.connect(self.add_function)
        self.del_func_btn.clicked.connect(self.delete_func)
        self.clear_functions_btn.clicked.connect(self.clear_func)
        self.confirm_func_btn.clicked.connect(self.confirm_functions)
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

        self.func_list.itemClicked.connect(self.change_func)

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
            self.del_func_btn.setEnabled(True)
            self.func_edit.clear()

    def insert_func_char(self, char):
        if char == ") " and self.func_edit.text()[-1] == " ":
            self.func_edit.backspace()
        self.func_edit.insert(char)

    def change_func(self, item):
        self.func_edit.clear()
        self.func_edit.insert(from_unicode(item.text()))

    def delete_func(self):
        if not self.func_list.selectedItems():
            return
        msg = QMessageBox.question(self.parent, "Confirm action", "Are you sure want to delete selected function?")
        if msg == QMessageBox.Yes:
            sel = self.func_list.selectedIndexes()[0].row()
            self.func_list.takeItem(sel)
            self.data_container.del_func(sel)
            del sel
            if not self.data_container.func_list:
                self.del_func_btn.setEnabled(False)

    def clear_func(self):
        msg = QMessageBox.question(self.parent, "Comfirm action", "Are you sure want to clear ALL functions?")
        if msg == QMessageBox.Yes:
            self.func_list.clear()
            self.func_edit.clear()
            self.data_container.clear_func()
            self.del_func_btn.setEnabled(False)

    def confirm_functions(self):
        if not self.data_container.func_list:
            return
        msg = QMessageBox.question(self.parent, "Confirm action",
                                   "Are you sure want to confirm all functions? Changing functions will be impossible.")
        if msg == QMessageBox.Yes:
            self.functions_group.setEnabled(False)
            self.fragment_group.setEnabled(True)

    def generate_given_head(self):
        pass


class TruthWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.data_container = DataContainer()
        ui = UiTruthtableWindowNitro(self, self.data_container)
        ui.setupUi(self)
        ui.bind()
        self.ui = ui


if __name__ == '__main__':
    truth_app = QApplication(sys.argv)
    win = TruthWindow()
    win.show()

    sys.exit(truth_app.exec_())
