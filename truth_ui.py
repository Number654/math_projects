# -*- coding: utf-8 -*-

from truthUserInterface import UiTruthtableWindow
from truthtable import LogicalExpression, DEFAULT_FUNC, NUM
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
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

    def del_given_row(self, index):
        self.given_rows.pop(index)

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
        self.head_generated = False
        self.changing_row = False

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

        self.generate_head_btn.clicked.connect(self.generate_given_head)
        self.add_row_btn.clicked.connect(self.add_given_row)
        self.del_row_btn.clicked.connect(self.delete_row)
        self.change_row_btn.clicked.connect(self.choose_change)
        self.apply_change_row_btn.clicked.connect(self.apply_changes)

        self.clearall_btn.clicked.connect(self.clearall)
        self.get_result_btn.clicked.connect(self.compute_result)

        self.func_list.itemClicked.connect(self.change_func)

    @staticmethod
    def generate_error(text):
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
            self.func_list.clearSelection()
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
            self.func_list.clearSelection()
            self.func_edit.clear()

    def generate_given_head(self):
        self.fragment_table.setColumnCount(len(self.data_container.variables)+len(self.data_container.func_list))
        self.fragment_table.setHorizontalHeaderLabels(["--"]*(len(self.data_container.variables)) +
                                                      (["F%s" % ("" if not n else str(n)) for n in
                                                       range(len(self.data_container.func_list))] if
                                                      self.check_if_last.checkState() else
                                                      ["--"]*len(self.data_container.func_list)))
        self.fragment_table.resizeColumnsToContents()
        self.head_generated = True

    def operate_given_row(self):
        if not self.head_generated:
            return
        entered = self.row_edit.text()
        if not entered.replace(" ", ""):
            return
        vcount = 0
        maxcount = len(self.data_container.variables) + len(self.data_container.func_list)
        ent_sep = []
        for val in entered.split(" "):
            if not val:
                continue
            vcount += 1
            if vcount > maxcount:
                UiTruthtableWindowNitro.generate_error("Invalid row data: unmatching length")
                return
            if val not in NUM:
                if val != "N" and val != "n":
                    UiTruthtableWindowNitro.generate_error("Invalid row data: unexpected symbol: %s" % val)
                    return
                ent_sep.append("N")
                continue
            ent_sep.append(val)
        if vcount < maxcount:
            UiTruthtableWindowNitro.generate_error("Invalid row data: unmatching length")
            return

        return tuple(ent_sep)

    def add_given_row(self):
        ent_sep = self.operate_given_row()
        if ent_sep is None:
            return
        if ent_sep not in self.data_container.given_rows:
            self.data_container.add_given_row(ent_sep)
            self.fragment_table.setRowCount(self.fragment_table.rowCount()+1)
            for n, val in enumerate(ent_sep):
                self.fragment_table.setItem(self.fragment_table.rowCount()-1, n,
                                            QTableWidgetItem(val))
            self.del_row_btn.setEnabled(True)
            self.change_row_btn.setEnabled(True)
            self.row_edit.clear()

    def delete_row(self):
        if not self.fragment_table.selectedItems():
            return
        msg = QMessageBox.question(self.parent, "Confirm action", "Are you sure want to delete selected row?")
        if msg == QMessageBox.Yes:
            sel = self.fragment_table.selectedIndexes()[0].row()
            self.fragment_table.removeRow(sel)
            self.data_container.del_given_row(sel)
            self.row_edit.clear()
            self.fragment_table.clearSelection()
            del sel
            if not self.data_container.given_rows:
                self.del_row_btn.setEnabled(False)
                self.change_row_btn.setEnabled(False)
                self.apply_change_row_btn.setEnabled(False)
            if self.changing_row:
                self.add_row_btn.setEnabled(True)
                self.fragment_table.setEnabled(True)
                self.check_if_last.setEnabled(True)
                self.generate_head_btn.setEnabled(True)
                self.change_row_btn.setEnabled(bool(self.data_container.given_rows))
                self.changing_row = False

    def choose_change(self):
        if not self.fragment_table.selectedItems():
            return
        self.row_edit.insert(" ".join(self.data_container.given_rows[self.fragment_table.selectedIndexes()[0].row()]))
        self.apply_change_row_btn.setEnabled(True)
        self.add_row_btn.setEnabled(False)
        self.fragment_table.setEnabled(False)
        self.check_if_last.setEnabled(False)
        self.generate_head_btn.setEnabled(False)
        self.change_row_btn.setEnabled(False)
        self.changing_row = True

    def apply_changes(self):
        ent_sep = self.operate_given_row()
        if ent_sep is None:
            self.delete_row()
            return

        sel = self.fragment_table.selectedIndexes()[0].row()
        if ent_sep != self.data_container.given_rows[sel]:
            for n, val in enumerate(ent_sep):
                self.data_container.replace_given_row(sel, ent_sep)
                self.fragment_table.setItem(sel, n,
                                            QTableWidgetItem(val))
        self.apply_change_row_btn.setEnabled(False)
        self.add_row_btn.setEnabled(True)
        self.fragment_table.setEnabled(True)
        self.check_if_last.setEnabled(True)
        self.generate_head_btn.setEnabled(True)
        self.change_row_btn.setEnabled(True)
        self.row_edit.clear()
        self.fragment_table.clearSelection()
        self.changing_row = False

    def clearall(self):
        msg = QMessageBox.question(self.parent, "Confirm action",
                                   "Are you sure want to RESET ALL data in this session? It can't be undone!")
        if msg == QMessageBox.Yes:
            self.data_container.clearall()
            self.changing_row = False
            self.head_generated = False
            self.fragment_table.clearSelection()
            self.func_list.clearSelection()
            self.results_list.clearSelection()
            self.fragment_group.setEnabled(False)
            self.result_group.setEnabled(False)

            self.func_list.clear()
            self.func_edit.clear()
            self.del_func_btn.setEnabled(False)

            self.fragment_table.clear()
            self.fragment_table.setRowCount(0)
            self.fragment_table.setColumnCount(0)

            self.results_list.clear()
            self.del_row_btn.setEnabled(False)
            self.change_row_btn.setEnabled(False)
            self.apply_change_row_btn.setEnabled(False)
            self.functions_group.setEnabled(True)

    def compute_result(self):
        if not self.data_container.func_list or not self.data_container.given_rows:
            return
        print("enough")


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
