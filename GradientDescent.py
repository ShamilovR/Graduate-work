from sympy import *
from math import fabs
from Parser import discard_zeros

class GradientDescent:
    def __init__(self, eps, alpha, betta, X, coefficients):
        self.eps = eps
        self.alpha = alpha
        self.betta = betta
        self.X = X
        self.coefs = coefficients
        self.result = 0
        self.prev_result = self.func_result(self.X[0], self.X[1])
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
        x1 = symbols('x1')
        x2 = symbols('x2')
        self.x_array.append(self.X[0])
        self.y_array.append(self.X[1])
        self.z_array.append(self.prev_result)
        self.first_step_result = discard_zeros([self.X[0], self.X[1], self.result])
        print(self.first_step_result)
        data.append([self.count, tab, '%.5f' % self.X[0], tab, '%.5f' % self.X[1], tab, '%.5f' % self.func_result(self.X[0], self.X[1])])
        while True:
            if fabs(self.result - self.prev_result) <= self.eps:
                return data
            while True:
                if self.count == 1000:
                    return data
                x_1 = self.X[0] - self.alpha * self.dfunc(x1).subs(x1, self.X[0])
                x_2 = self.X[1] - self.alpha * self.dfunc(x2).subs(x2, self.X[1])
                self.result = self.func_result(x_1, x_2)
                if self.prev_result > self.result:
                    self.prev_result = self.func_result(self.X[0], self.X[1])
                    self.X[0] = x_1
                    self.X[1] = x_2
                    self.count += 1
                    if self.count == 1:
                        self.first_step_result = discard_zeros([self.X[0], self.X[1], self.result])
                        print(self.first_step_result)
                    self.x_array.append(self.X[0])
                    self.y_array.append(self.X[1])
                    self.z_array.append(self.result)
                    data.append([self.count, tab, '%.5f' % x_1, tab, '%.5f' % x_2, tab, '%.5f' % self.result])
                    break
                else:
                    self.alpha *= self.betta
