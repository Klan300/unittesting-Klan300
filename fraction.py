import math


class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """

    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        if type(numerator) is not int:
            if type(numerator) is not float:
                raise TypeError("numerator is not int")  
            elif not math.isnan(numerator):
                raise TypeError("numerator is not int")  
        if type(denominator) is not int :
            if type(denominator) is not float:
                raise TypeError("denominator is not int")  
            if not math.isnan(denominator):
                raise TypeError("denomiantor is not int")

        if denominator == 0 or math.isnan(numerator/denominator):
            self.numerator = math.nan
            self.denominator = math.nan
        else:
            gcd = math.gcd(numerator, denominator)
            frac = numerator/denominator
            if frac > 0:
                self.numerator = abs(int(numerator/gcd))
                self.denominator = abs(int(denominator/gcd))
            elif frac < 0:
                if denominator < 0:
                    self.numerator = int(-numerator/gcd)
                    self.denominator = abs(int(denominator/gcd))
                else:
                    self.numerator = int(numerator/gcd)
                    self.denominator = int(denominator/gcd)
            else:
                self.numerator = int(numerator/gcd)
                self.denominator = int(denominator/gcd)



    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = ((self.numerator * frac.denominator) +
                     (frac.numerator * self.denominator))
        denominator = self.denominator * frac.denominator



        return Fraction(numerator, denominator)

    # TODO write __mul__ and __str__.  Verify __eq__ works with your code.
    # Optional have fun and overload other operators such as
    # __sub__ for f-g
    # __gt__  for f > g
    # __neg__ for -f (negation)

    def __mul__(self, frac):
        """Multiply 2 fraction 
        """
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator
        return Fraction(numerator, denominator)

    def __str__(self):
        if self.denominator == 1 or math.isnan(self.numerator/self.denominator):
            result = f"{self.numerator}"
        else:
            result = f"{self.numerator}/{self.denominator}"
        return result

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.__str__() == frac.__str__()
