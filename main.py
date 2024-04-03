# -*- coding: utf-8 -*-

from copy import copy
from numbers import Rational
from abc import ABC, abstractmethod
from math import gcd, ceil, floor, pow, trunc


# __add__, __ceil__, __eq__, __floor__, __floordiv__, __le__, __lt__, __mod__, __mul__, __neg__, __pos__, __pow__,
# __radd__, __rfloordiv__, __rmod__, __rmul__, __round__, __rpow__, __rtruediv__, __truediv__, __trunc__


def common_denom(*fractions):
    common = gcd(*[one.n for one in fractions])
    return [one.to_denominator(common) for one in fractions]


def uroot(x, n, eps=1e-16):
    if isinstance(x, SuperFraction):
        return x.root(n)
    if isinstance(n, SuperFraction):
        return uroot(x, float(n))
    prev_y = 0
    next_y = x
    while abs(next_y - prev_y) >= eps:
        prev_y = next_y
        next_y = (prev_y * (n - 1) + x / prev_y ** (n - 1)) / n

    return next_y


def npow(x, n, eps=1e-16):
    if isinstance(n, SuperFraction):
        return uroot(x ** n.m, n.n, eps=eps)


class SuperFraction(Rational, ABC):

    def __init__(self, *args, accuracy=16):
        super(SuperFraction, self).__init__()
        self.m = 0  # Числитель
        self.n = 1  # Знаменатель

        l_args = len(args)
        if not l_args:
            raise TypeError("%s takes at least 1 argument, %s given" % (self.__class__.__name__, l_args))
        elif l_args == 1:
            _a = args[0]
            if isinstance(_a, int):
                self.m, self.n = _a, 1
            elif isinstance(_a, float):
                _a = round(_a, accuracy)
                _u = str(_a).split(".")
                _n = 10 ** len(_u[1])
                _m = int(_u[1]).__trunc__() + int(_u[0]).__trunc__() * _n
                self.m, self.n = _m, _n
                del _u, _n, _m
            elif isinstance(_a, SuperFraction):
                self.m, self.n = _a.m, _a.n
            else:
                raise TypeError("Invalid type: %s" % type(_a))
            del _a
        elif l_args == 2 or l_args == 3:
            _a0 = args[0]
            _a1 = args[1]
            if l_args == 2:
                if not (isinstance(_a0, int) or isinstance(_a0, float) or isinstance(_a0,
                                                                                     SuperFraction)) and \
                        not (isinstance(_a1, int) or isinstance(_a1, float) or isinstance(_a1, SuperFraction)):
                    raise TypeError("Invalid types for numerator or denominator: %s and %s" %
                                    (type(_a0), type(_a1)))
                elif isinstance(_a0, float) or isinstance(_a1, float):
                    _f = Fraction(Fraction(_a0, accuracy=accuracy) / Fraction(_a1, accuracy=accuracy))
                    self.m, self.n = _f.m, _f.n
                    del _f
                elif isinstance(_a0, int) and isinstance(_a1, int):
                    self.m, self.n = _a0, _a1
                elif isinstance(_a0, SuperFraction) or isinstance(_a0, SuperFraction):
                    self.m, self.n = Fraction(_a0 / _a1).base
            else:  # if 3
                if not (isinstance(_a1, int) or isinstance(args[2], float)) and not (isinstance(_a1, int) or
                                                                                     isinstance(_a1, float)) \
                        and not (isinstance(_a0, int) or isinstance(_a0, float)):
                    raise TypeError("Invalid types for number, numerator or denominator: %s, %s and %s" %
                                    (type(_a0), type(_a1), type(args[2])))
                _f = Fraction(args[2] * _a0 + _a1, args[2])
                self.m, self.n = _f.m, _f.n
                del _f
            del _a0, _a1

        else:
            raise TypeError("Too many arguments, expected 1, 2, or 3 arguments, got %s instead" % l_args)

    @property
    def base(self):
        return self.m, self.n

    def __str__(self):
        return f"({self.m}/{self.n})"

    def __repr__(self):
        return str(self.__str__())

    def assign(self, other):
        if not isinstance(other, SuperFraction):
            raise TypeError("assign() method suppors Fractions only")
        self.m, self.n = other.m, other.n

    def to_denominator(self, n):
        """Привести к знаменателю n. Метод будет дореализован в подклассах."""
        if n % self.n:
            return

    def _compare(self, other, sign):
        if self.__class__.__name__ == "SuperFraction":
            raise NotImplementedError
        formatted = common_denom(self, other)  # Don't delete!
        return eval(f"formatted[0].m {sign} formatted[1].m")

    @property
    def numerator(self):
        return self.m

    @property
    def denominator(self):
        return self.n

    def __abs__(self):
        abs_ed = copy(self)
        abs_ed.m, abs_ed.n = abs(self.m), abs(self.n)
        return abs_ed

    def __pos__(self):
        return self

    @abstractmethod
    def root(self, n):
        pass

    def reduce(self):
        pass


class Fraction(SuperFraction):

    def to_denominator(self, n):
        super(Fraction, self).to_denominator(n)
        return Fraction(self.m * (n / self.n), n)

    def __neg__(self):
        return Fraction(self.m.__neg__(), self.n)

    def __add__(self, other):
        other = Fraction(other)
        if self.n != other.n:
            new_self, other = common_denom(self, other)
        else:
            new_self = self
        return Fraction(new_self.m + other.m, new_self.n)

    def __iadd__(self, other):
        self.assign(copy(self) + Fraction(other))
        return self

    def __ceil__(self):
        return Fraction(ceil(self.m / self.n))

    def __eq__(self, other):
        return self._compare(other, "==")

    def __ne__(self, other):
        return not self.__eq__(other)

    def __floor__(self):
        return Fraction(floor(self.m / self.n))

    def __floordiv__(self, other):
        return self.__truediv__(other).__floor__()

    def __le__(self, other):
        return self._compare(other, "<=")

    def __lt__(self, other):
        return self._compare(other, "<")

    def __ge__(self, other):
        return self._compare(other, ">=")

    def __gt__(self, other):
        return self._compare(other, ">")

    def __mod__(self, other):
        return abs(self - other * (self // other))

    def __mul__(self, other):
        other = Fraction(other)
        return Fraction(self.m * other.m, self.n * other.n)

    def __imul__(self, other):
        self.assign(copy(self) * Fraction(other))
        return self

    def __pow__(self, power, accuracy=16):
        return Fraction(pow(self.m, power), pow(self.n, power))

    def __ipow__(self, power):
        self.assign(copy(self).__pow__(power))
        return self

    def __radd__(self, other):
        return self.__add__(other)

    def __rfloordiv__(self, other):
        return self.__rtruediv__(other).__floor__()

    def __rmod__(self, other):
        return abs(other - self * (other // self))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __round__(self, n=None):
        return round(float(self), n)

    def __rpow__(self, other):
        return uroot(pow(other, self.m), self.n)

    def __rsub__(self, other):
        return (-self).__add__(other)

    def __rtruediv__(self, other):
        return self.reverse() * other

    def __sub__(self, other):
        return self.__add__(-other)

    def __isub__(self, other):
        self.assign(copy(self) - Fraction(other))
        return self

    def __truediv__(self, other):
        other = Fraction(other).reverse()
        return self * other

    def __ifloordiv__(self, other):
        self.assign(copy(self) / Fraction(other))
        return self

    def __trunc__(self):
        return self.__int__()

    def __float__(self):
        return self.m / self.n

    def __int__(self):
        return trunc(self.__float__())

    def __hash__(self):
        return hash((self.m, self.n))

    def root(self, n):
        return Fraction(uroot(self.m, n), uroot(self.n, n))

    def reverse(self):
        return Fraction(self.n, self.m)
