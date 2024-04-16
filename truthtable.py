# -*- coding: utf-8 -*-

from math import log10
from copy import deepcopy as copy
from itertools import permutations
from collections.abc import Collection


UNICODE_FUNC = {"~": "¬", "/\\": "∧", "\\/": "∨", "->": "→", "=": "≡", "^": "⊕", "|": "∨", "&": "∧"}
DEFAULT_FUNC = {"¬": "~", "∧": "/\\", "∨": "\\/", "→": "->", "≡": "=", "⊕": "^"}
ENDVAR = r"\/)=>^"
ENDVAR_LTOR = r"\/)=-^"
WRAPPERS = "=>^"
LATIN = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUM = "0123456789"
N = None

"""
        ~        - not
        /\\  (&) - and
        \\/  (|) - or
        =        - ==
        ^        - xor
        ->       - (<=)
        
        
        0 - False
        1 - True
        ? - None (unknown value)

"""


def format_bin(bin_integer, signs):
    """
    Function for formatting binary num to specified length.
    11 -> [0, 0, 1, 1]
    :param bin_integer: binary integer
    :param signs: length
    :return: list of binary values (0 and 1)
    """
    s = str(bin_integer)[2:]
    z = signs-len(s)
    return [0 if i <= z else int(s[i-1-z]) for i in range(1, signs+1)]


def move(lst, index, nindex):
    new_vaues = copy(lst)
    val = new_vaues.pop(index)
    new_vaues.insert(nindex, val)
    return new_vaues


# Сравнить два набора данных, если считать, что, например, (None и 0) или (None и 1) - два равных элемента наборов
def eq_none(first, second):
    """
    Function for comparing two iterables (sized) if None is equal to 0 or 1.
    :param first: the first sized iterable
    :param second: the second sized iterable
    :return: True if equal
    """
    if len(first) != len(second):
        return False
    for fi, se in zip(first, second):
        if fi is not None and se is not None:
            if fi != se:
                return False
    return True


def generate_rows_for_column(values):
    return [Row((val,)) for val in values]


def typename(obj):
    return str(type(obj).__name__)


class BaseTable:

    """
    Superclass for any table class in this module.
    """

    def __init__(self, rows=()):
        if not isinstance(rows, Collection):
            raise TypeError("'rows' argument must be sized iterable, not '%s'" % typename(rows))
        self.rows = list(rows)
        self.amount = len(self.rows)
        self.row_len = None if not rows else len(self.rows[0])

    def __str__(self):
        return "\n".join((str(r) for r in self.rows))

    def __repr__(self):
        return str(self.__str__())

    def __getitem__(self, item):
        if not isinstance(item, int) or item < 0:
            raise TypeError("Index must be a natural number or 0")
        return copy(self.rows[item])

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Index (key) must be a natural number or 0")
        if not isinstance(value, Row):
            raise TypeError("Value must be instance of Row, not '%s'" % typename(value))
        self.rows[key] = copy(value)

    def __eq__(self, other):
        if not isinstance(other, BaseTable):
            raise TypeError("'==' not supported between instances of '%s' and '%s'" % (typename(self), typename(other)))
        if self.rows == other.rows and self.amount == other.amount:
            return True
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_column(self, x=0):
        if self.row_len is None:
            raise ValueError("Cannot get column from absolutely empty table")
        if x > self.row_len-1 or x < 0:
            raise IndexError("Column index is out of range")
        return Column(tuple((r[x] for r in self.rows)))

    def separate(self):  # Separate to columns
        if self.row_len is None:
            raise ValueError("Cannot separate absolutely empty table to columns")
        return tuple((self.get_column(x=c) for c in range(self.row_len)))
    
    def index_column(self, column):
        if not isinstance(column, Column):
            raise TypeError("Invalid type for indexing column: '%s'" % typename(column))
        return [i for i, r in enumerate(self.separate()) if r == column]

    def index_row(self, row):
        return [i for i, r in enumerate(self.rows) if r == row]

    def append(self, row):
        # row - object Row
        if not isinstance(row, Row):
            raise TypeError("Unknown type for append row to table: '%s'" % typename(row))
        if self.row_len is not None and self.row_len != len(row):
            raise ValueError("Unmatching length of given row and length of rows in this table")
        if self.row_len is None:
            self.row_len = len(row) if len(row) else None
        self.rows.append(row)
        self.amount += 1

    def row_in(self, row):
        if not isinstance(row, Row):
            raise TypeError("Unknown type for checking in table: '%s'" % typename(row))
        for x in self.rows:
            if x == row:
                return True
        return False

    def inject_table(self, table, x=0, y=0):
        """
        Method for injecting given table into this table.
        First value of first row in given table will have (x; y) coordinates relating to this table.
        Note: this method overwrites previous values in this table if they exist.
        :param table: instance of BaseTable class
        :param x: index (relating to this table) of value of row to inject (value at this index in
        this table will be overwritten).
        :param y: index (relating to this table) of row to inject (with overwriting)
        :return: None
        """
        if not isinstance(table, BaseTable):
            raise TypeError("Unknown type to inject: '%s'" % typename(table))
        if not table.amount or table.row_len is None:  # If an empty table is given
            return
        if x < 0 or y < 0:
            raise IndexError("Indexes must be natural numbers or 0")
        if x + table.row_len > self.row_len or y + table.amount > self.amount:
            raise IndexError("Cannot inject table (col %s; rows %s) at these indexes: x %s; y %s" %
                             (table.row_len, table.amount, x, y))
        for ys, row, trow in zip(range(y, table.amount+1), self.rows[y:(y+table.amount)], table.rows):
            for xs, col, tcol in zip(range(x, table.row_len+1), row[x+(x+table.row_len)], trow.values):
                self.rows[ys][xs] = tcol

    def __base_contain(self, other, start=0):
        if not isinstance(other, BaseTable):
            raise TypeError("'other' argument must be only BaseTable (or subclasses) instance")
        if not other.amount:
            return True
        if (not self.amount) and other.amount:
            return False
        if other.row_len is None:
            return True
        if self.row_len is None:
            return False
        stop = start + other.row_len-1
        if start < 0 or start > self.row_len-1 or stop > self.row_len-1:
            raise ValueError("Invalid index: start %s; length of row of given %s; max index %s" % (start, other.row_len,
                                                                                                   self.row_len-1))
        if (not start) and stop == -1 and self == other:  # If we don't have to check anything
            return True

    def contains(self, other, start=0, pattern=()):
        """
        Method for checking other instance of BaseTable if it is in this table.
        Warning: this method checks every row of other table for equality to every row
        in this table, consequently, the order of rows does not matter. To check with
        matching order, use BaseTable.total_contains method.
        Note: start index are index of columns, not rows.
        :param pattern: pattern for checking (moves values in rows and checks)
        :param other: instance of BaseTable class
        :param start: index of column to start checking
        :return: True if other table is in this table
        """
        f = self.__base_contain(other, start=start)
        if f is not None:
            return f
        del f
        found = []
        result = False
        for i in range(other.amount):
            interm = False
            given_row = copy(other.rows[i])
            if pattern:
                given_row.move_pattern(pattern=pattern, start=start)
            for y, row in enumerate(self.rows):
                if row[start:(start+other.row_len)] == given_row and y not in found:
                    found.append(y)
                    interm = True
                    break
            if not interm:
                break
            if i+1 == other.amount:
                result = True
                break
        del interm, found, given_row
        return result

    def total_contains(self, other, start=0):
        """
        Method for checking other instance of BaseTable if it is in this table
        with given order of rows.
        Note: start index are index of columns, not rows.
        :param other: instance of BaseTable class
        :param start: index of column to start checking
        :return: True if other table is in this table
        """
        f = self.__base_contain(other, start=start)
        if f is not None:
            return f
        del f
        i_interm = False
        for i in range(self.amount-other.amount+1):
            for r, gi in zip(self.rows[i:(i+other.amount)], other.rows):
                i_interm = True
                if r[start:(start+other.row_len)] != gi:
                    i_interm = False
                    break
            if i_interm:
                return True
        del i_interm
        return False


class Column(BaseTable):

    """
    Class for one column. In fact, this is table with only one column.
    """

    def __init__(self, rows=()):
        if len(rows) and not isinstance(rows[0], Row):
            rows = generate_rows_for_column(rows)
        super().__init__(rows)
        if self.row_len != 1:
            raise ValueError("Every row of 'column table' must be with length 1")
        self.row_len = 1  # If no rows given and row_len == None by default

    def get_column(self, x=0):  # For economy of time
        return self

    def index_column(self, column):  # For economy of time
        if self != column:
            raise ValueError("Given column is not equal to this column")
        return [0]

    def total_contains(self, other, start=0):  # For economy of time
        return self.__eq__(other)


class TruthTable(BaseTable):

    def __init__(self, variables, expressions):
        super().__init__()
        if not isinstance(variables, Collection):
            raise TypeError("'variables' argument must be sized iterable, not '%s'" % typename(variables))
        if not (isinstance(expressions, Collection) or isinstance(expressions, LogicalExpression)):
            raise TypeError("'expressions' argument must be sized iterable or LogicalExpression, not '%s'" %
                            typename(expressions))
        if isinstance(expressions, LogicalExpression):  # if we got only one expression
            expressions = [expressions]
        if not all((isinstance(i, LogicalExpression) for i in expressions)):
            raise TypeError("Unknown type for logical expression")
        if not expressions or not variables:
            raise ValueError("Cannot build truth table with no variables or no logical expressions")
        self.vars = list(variables)
        self.expressions = list(expressions)
        self.nvars = len(self.vars)
        self.nexpr = len(self.expressions)

        self.row_len = self.nvars+self.nexpr

    def __str__(self):
        # At first, generate head of table
        strings = [" ".join(self.vars)+"  "+self.generate_func_names("  ")]
        base = None
        for r in self.rows:
            base = " ".join(map(str, r.values[:self.nvars]))+"  "
            for n, expr_val in enumerate(r.values[self.nvars:], start=1):
                base += str(expr_val)+(" "*(6+int(log10(n))) if n < self.nexpr else "")
            strings.append(base)
        del base
        return "\n".join(strings)

    def generate_func_names(self, _join=""):
        gen = ("func%s" % x for x in range(1, self.nexpr+1))
        if not _join:
            return list(gen)
        return _join.join(gen)

    def abstract_equal(self, other):
        """
        Method for checking this truth table for equality to other if generated rows do not matter
        :param other: Instance of TruthTable
        :return: True if equal
        """
        if not isinstance(other, TruthTable):
            raise TypeError("'==' not supported between instances of '%s' and '%s'" % (typename(self), typename(other)))
        if (self.vars != other.vars or self.expressions != other.expressions or self.nexpr != other.nexpr
                or self.nvars != other.nvars):
            return False
        return True

    def generate_rows(self, func_vals=()):
        rng = range(2**self.nvars)
        count = 0
        if isinstance(func_vals, int) or isinstance(func_vals, bool):
            func_vals = (bool(func_vals),)
        if func_vals is None:
            func_vals = ()
        if func_vals:
            if len(func_vals) != self.nexpr:
                raise ValueError("Unmatching length of seq of values and expressions amount (%s != %s)" %
                                 (len(func_vals), self.nexpr))
            for x in rng:
                b = format_bin(bin(count), self.nvars)
                ev = []
                pass_row = False  # If the whole evaluated row doesn't match func_vals
                for ex, fval in zip(self.expressions, func_vals):
                    evaluated = ex.evaluate({var: val for var, val in zip(self.vars, b)})
                    if fval is not None:
                        if evaluated == fval:
                            ev.append(evaluated)
                        else:
                            pass_row = True  # This row of values of functions doesn't match func_vals
                            break
                    else:
                        ev.append(evaluated)  # If value of function, named fval doesn't matter
                if not pass_row:
                    self.append(Row(b + ev))  # Append to generated rows if values of functions are good
                count += 1
            del ev, evaluated, pass_row
        else:
            for x in rng:
                b = format_bin(bin(count), self.nvars)
                self.append(Row(b + [ex.evaluate({var: val for var, val in zip(self.vars, b)})
                                     for ex in self.expressions]))
                count += 1
        del b, count, rng

    def find_given(self, given, _all=True):
        if not isinstance(given, GivenTable):
            raise TypeError("'find_given' method requires GivenTable instance, not '%s'" % typename(given))
        if self.contains(given) and not _all:
            if given.row_len == given.movable_limit and given.nexpr:  # If answer must contain names of expressions
                return [' '.join(self.vars)] + self.generate_func_names()
            return [' '.join(self.vars)]

        result = []
        head = self.vars + self.generate_func_names()
        for variant in permutations(range(given.movable_limit)):
            if self.contains(given, pattern=variant):
                result.append(' '.join((head[x] for x in variant)))
                if not _all:
                    break
        del head
        return result


class GivenTable(BaseTable):

    """
    Superclass for all given table classes.
    Does not contain any info about positions of columns.
    """

    def __init__(self, rows=(), vars_amount=1, expr_amount=1):
        super().__init__(rows)
        vars_amount, expr_amount = ((0 if vars_amount == -1 else vars_amount),
                                    (0 if expr_amount == -1 else expr_amount))
        if self.row_len is not None and (self.row_len-vars_amount != expr_amount or
                                         self.row_len-expr_amount != vars_amount):
            raise IndexError("Amount of vars or exprs does not match length of row (%s + %s != %s)" %
                             (vars_amount, expr_amount, self.row_len))
        if self.row_len is None:
            self.row_len = vars_amount + expr_amount
        self.nexpr = expr_amount
        self.nvars = vars_amount
        self.movable_limit = self.row_len  # Max index of element in a row that is able to be moved

    def move_pattern(self, pattern, start=0):
        if not self.amount:
            return
        for r in range(self.amount):
            self.rows[r].move_pattern(pattern, start=start)


class GivenKnownExpressionsTable(GivenTable):

    """
    Class for processing given fragment of truth table that contains values of variables
    and contains values of expressions as last n columns.
    """

    def __init__(self, rows=(), vars_amount=1, expr_amount=1):
        if not vars_amount or not expr_amount:
            raise ValueError("Cannot create table without any vars or exprs")
        if vars_amount == -1 or expr_amount == -1 or vars_amount is None or expr_amount is None:
            raise ValueError("Cannot create table without info about amount of vars or exprs")
        super().__init__(rows=rows, vars_amount=vars_amount, expr_amount=expr_amount)
        self.movable_limit = vars_amount

    def __str__(self):
        strings = ["- "*self.nvars + " " + "  ".join(("func%s" % x for x in range(1, self.nexpr+1)))]
        base = None
        for r in self.rows:
            base = " ".join(map(lambda x: str(x) if x is not None else "?", r.values[:self.nvars])) + "  "
            for n, expr_val in enumerate(r.values[self.nvars:], start=1):
                base += ((str(expr_val) if expr_val is not None else "?") +
                         (" " * (6+int(log10(n))) if n < self.nexpr else ""))
            strings.append(base)
        del base
        return "\n".join(strings)

    def move_pattern(self, pattern, start=0):
        if start+len(pattern) > self.nvars:
            raise ValueError("Cannot move columns of values of expressions")
        super().move_pattern(pattern, start=start)


class GivenValuesTable(GivenTable):

    """
    Class for proccessing given fragment of truth table that contains only values of variables.
    """

    def __init__(self, rows=(), vars_amount=1):
        # Note: 'vars_amount' argument is used when 'rows' argument is an empty iterable
        # If something is wrong, exception will be generated in super call
        if rows and vars_amount == 1:
            vars_amount = len(rows[0])
        super().__init__(rows=rows, vars_amount=vars_amount, expr_amount=-1)
        self.movable_limit = vars_amount


class Row:

    def __init__(self, values=()):
        self.values = list(values)
        self.length = len(self.values)

    def __str__(self):
        return " ".join((str(v) if v is not None else "?" for v in self.values))

    def __repr__(self):
        return str(self.__str__())

    def __eq__(self, other):
        if not isinstance(other, Row):
            raise TypeError("Unknown type to check equality: '%s'" % typename(other))
        return eq_none(self.values, other.values)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __len__(self):
        return self.length

    def __getitem__(self, item):
        v = self.values[item]
        if not isinstance(v, Collection):
            return Row((v,))
        return Row(v)

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Index (key) must be a natural number or 0")
        self.values[key] = value

    # Method for checking indexes
    def __move_exeptions(self, index, nindex):
        if nindex < 0 or nindex > self.length-1:
            raise IndexError("Cannot move element of row to index: %s; max %s, min 0" % (nindex, self.length-1))
        if index < 0 or index > self.length-1:
            raise IndexError("Invalid index of element: %s; max %s, min 0" % (index, self.length-1))

    # move value at one index to new index without replacement
    def move(self, index, nindex, change=True, lim=None, start=0):
        if lim is not None:
            if lim <= start:
                raise IndexError("Limite of index <= start index (%s <= %s)" % (lim, start))
        if index == nindex:
            if not change:
                return Row(self.values)
            return
        self.__move_exeptions(index, nindex)
        val = self.values[start:lim]
        n_val = (self.values[:start]+move(val, index-start, nindex-start) +
                 self.values[(self.length-(lim if lim is not None else 0)):])
        del val
        if change:
            self.values = copy(n_val)
            del n_val
            return
        return Row(n_val)

    def move_pattern(self, pattern, change=True, start=0):
        # 012 -> 102
        # Note: indexes are NOT absolute: pattern works only in the specified range [start:stop]
        # For example, if range of this row is 0, 1, 2, 3, 4, 5 and start is 1,
        # Then index 0 in pattern will reference to value of this row at index 1
        le = len(pattern)
        if le > (self.length-start):
            raise ValueError("Pattern is too long (start index %s; pattern %s values; row %s values accessible)" %
                             (start, le, self.length-start))
        if tuple(pattern) == tuple(range(self.length)):  # If pattern has no effect
            return
        new = [None]*le
        for val, new_index in zip(self.values[start:(start+le)], pattern):
            new[new_index] = val
        n_new = self.values[:start]+new+self.values[(start+le):]
        del new, le
        if change:
            self.values = copy(n_new)
            return
        return Row(n_new)


class LogicalExpression:

    def __init__(self, string, check=False, unicode_support=False):
        self.expression, self.variables = LogicalParser.parse(str(string))
        self.uni_convert = unicode_support
        if check:
            self.evaluate({key: 0 for key in self.variables})  # Generates exception if something is wrong
        if unicode_support:
            self.raw_string = string

    def __str__(self):
        return self.expression

    def __repr__(self):
        return str(self.__str__())

    def __eq__(self, other):
        if not isinstance(other, LogicalExpression):
            raise TypeError("'==' not supported between instances of 'LogicalExpression' and '%s'" % typename(other))
        return self.expression == other.expression

    def __ne__(self, other):
        return not self.__eq__(other)

    def evaluate(self, keyval):
        _keyval = copy(keyval)
        keys = set(_keyval.keys())
        lk = len(keys)
        lv = len(self.variables)
        if lk < lv:
            raise NameError("Logical expression requires %s variables, %s given" % (lv, lk))
        missing = tuple(self.variables.difference(keys.intersection(self.variables)))
        if missing:
            # If there are a lot of given vars but at least one required wasn't given
            raise NameError("Not all required variables given; missing: %s" % str(missing))
        del missing, lk, lv
        for diff in keys.difference(self.variables):
            _keyval.pop(diff)
        del keys
        return int(eval(self.expression, _keyval))

    def to_unicode(self):
        if not self.uni_convert:
            return ""
        ustr = copy(self.raw_string)
        for k in UNICODE_FUNC.keys():
            ustr = ustr.replace(k, UNICODE_FUNC[k])
        return ustr


class LogicalParser:

    def __init__(self, *args, **kwargs):
        raise RuntimeError("'LogicalParser' class is only for static methods")

    @staticmethod
    def parse(string):
        if string.count("(") != string.count(")"):
            raise SyntaxError("Invalid syntax: parentheses mismatch")
        string = string.replace(" ", "").replace("|", "\\/").replace("&", "/\\")

        result = ""
        stack = ""
        var_stack = ""
        variables = set()
        level = 0
        not_close_index = None
        two_sign_operat = False
        imax = len(string)-1
        for i, sym in enumerate(string):
            if sym == "(":
                result += "("
                level += 1
            elif sym == "~" and string[i - 1] in WRAPPERS:  # If 'not' have to be wrapped with brackets
                result += "(not "
                not_close_index = LogicalParser.lookup(i, level, string)
            elif sym == ")":
                result += ")"
                level -= 1
                if var_stack:
                    variables.add(var_stack)
                    var_stack = ""
            else:
                if sym in r"\/->":
                    stack += sym
                    if two_sign_operat:
                        result += stack.replace("->", " <= ").replace("/\\", " and ").replace("\\/", " or ")
                        stack = ""
                    elif var_stack:
                        variables.add(var_stack)
                        var_stack = ""
                    two_sign_operat = not two_sign_operat
                elif sym == "~":
                    result += "not "
                elif sym == "=":
                    result += " == "
                    if var_stack:
                        variables.add(var_stack)
                        var_stack = ""
                else:
                    result += sym
                    if (sym in NUM and var_stack) or sym in LATIN:
                        var_stack += sym
                    elif var_stack:
                        variables.add(var_stack)
                        var_stack = ""
            if not_close_index is not None and i == not_close_index:
                result += ")"
                not_close_index = None
            if i == imax and var_stack:
                variables.add(var_stack)
                var_stack = ""
        del level, not_close_index, two_sign_operat, stack, var_stack, imax
        return result, variables

    @staticmethod
    def lookup(not_index, level, data):  # Close opened bracket
        if data[not_index + 1] != "(":  # If 'not' does not operate another brackets but operates only a variable
            max_index = len(data) - 1
            for x, df in enumerate(data[not_index:]):
                if df in ENDVAR_LTOR:
                    return not_index + x - 1
                elif not_index + x == max_index:  # If EOL, but there is anyway 'not' before var
                    return max_index
            return -1

        dl = copy(level)
        for x, lk in enumerate(data[not_index:]):
            if lk == "(":
                dl += 1
            elif lk == ")":
                dl -= 1
                if dl == level:
                    return not_index + x
            elif dl == level and lk in ENDVAR:
                return not_index + x
        del dl
        return -1
