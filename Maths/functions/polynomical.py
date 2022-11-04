from re import match


class polynomical_function:
    def __init__(self, expression: str):
        monomials = expression.split("+")
        for i in monomials:
            if match("(-?([0-9]+)?x(\*\*2)?) | [0-9]+", i):
                self.expression = expression
                self.indices = [i[0] if i[0] != "-" else i[1]
                                for i in monomials]

                if len(monomials) > 1:
                    self.monomials = [
                        polynomical_function(i) for i in monomials]
            else:
                raise ValueError

    def __repr__(self):
        return self.expression


p = polynomical_function("10x**2 + 2x + 5")

print(p.indices)
