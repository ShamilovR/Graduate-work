from sympy import *
from math import fabs
from Parser import discard_zeros

class SteepestDescent:
    def __init__(self, eps, X, coefficients):
        self.eps = eps
        self.X = X
        self.coefs = coefficients
        self.result = 0
        self.prev_result = 0
        self.count = 0
        self.x_array = []
        self.y_array = []
        self.z_array = []
        self.first_step_result = []

    def dfunc(self, d):
        x1, x2 = symbols('x1 x2')
        return diff(self.coefs[0] * x1 ** 2 + self.coefs[1] * x2 ** 2 + self.coefs[2] * x1 + self.coefs[3] * x2 + self.coefs[4], d)

    def func_result(self, x1, x2):
        return self.coefs[0] * (x1 ** 2) + self.coefs[1] * (x2 ** 2) \
               + self.coefs[2] * x1 + self.coefs[3] * x2 + self.coefs[4]

    def iteration_proccess(self):
        tab = '       '
        data = [['k', tab, 'x_0', tab + len(str(self.X[0])) * ' ', 'x_1' + tab + len(str(self.X[1])) * ' ',
                 tab, 'F(X_k)']]
        alpha = symbols('alpha')
        x1 = symbols('x1')
        x2 = symbols('x2')
        while True:
            if self.count == 500:
                return data
            self.result = self.func_result(self.X[0], self.X[1])
            data.append([self.count, tab, '%.5f' % self.X[0], tab, '%.5f' % self.X[1], tab,
                         '%.5f' % self.result])

            if self.count == 1 or self.count == 0:
                self.first_step_result = discard_zeros([self.X[0], self.X[1], self.result])
                print(self.first_step_result)

            self.x_array.append(self.X[0])
            self.y_array.append(self.X[1])
            self.z_array.append(self.result)

            if fabs(self.result - self.prev_result) <= self.eps:
                return data

            self.prev_result = self.result

            dx1 = self.X[0] - alpha * self.dfunc(x1).subs(x1, self.X[0])
            dx2 = self.X[1] - alpha * self.dfunc(x2).subs(x2, self.X[1])

            fi = self.func_result(dx1, dx2)
            dfi = diff(fi, alpha)

            alpha_result = solve(dfi, alpha)

            if len(alpha_result) == 0:
                alpha_result = 0
            else:
                alpha_result = alpha_result[0].n()

            self.X[0] = dx1.subs(alpha, alpha_result)
            self.X[1] = dx2.subs(alpha, alpha_result)

            self.count += 1


