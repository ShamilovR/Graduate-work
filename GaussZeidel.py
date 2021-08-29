from sympy import *
from math import fabs
from Parser import discard_zeros

class GaussZeidel:
    def __init__(self, eps, X, coefficients):
        self.eps = eps
        self.X = X
        self.coefs = coefficients
        self.result = 0
        self.prev_result = 0
        self.n = 2
        self.k = 0
        self.j = 0
        self.count = 0
        self.x_array = []
        self.y_array = []
        self.z_array = []
        self.first_step_result = []

    def func_result(self, x1, x2):
        return self.coefs[0] * x1 ** 2 + self.coefs[1] * x2 ** 2 + self.coefs[2] * x1 * x2


    def iteration_proccess(self):
        tab = '       '
        data = [['k', tab, 'x_0', tab + len(str(self.X[0])) * ' ', 'x_1' + tab + len(str(self.X[1])) * ' ',
                 tab, 'F(X_k)']]
        alpha = symbols('alpha')
        data.append([self.count, tab, '%.5f' % self.X[0], tab, '%.5f' % self.X[1], tab, '%.5f' % self.func_result(self.X[0], self.X[1])])
        self.first_step_result = discard_zeros([self.X[0], self.X[1], self.func_result(self.X[0], self.X[1])])
        self.x_array.append(self.X[0])
        self.y_array.append(self.X[1])
        self.z_array.append(self.func_result(self.X[0], self.X[1]))

        while True:
            self.result = self.func_result(self.X[0], self.X[1])

            if fabs(self.result - self.prev_result) <= self.eps:
                return data
            else:
                self.k = 0
                self.j = 0

            self.prev_result = self.func_result(self.X[0], self.X[1])

            while (self.j < self.n):
                S = []
                self.j = self.k - self.n * (self.k // self.n) + 1

                for i in range(self.n):
                    if i + 1 == self.j:
                        S.append(1)
                    else:
                        S.append(0)

                x1 = self.X[0] + alpha * S[0]
                x2 = self.X[1] + alpha * S[1]

                dFx = diff(self.func_result(x1, x2), alpha)

                alpha_result = solve(dFx, alpha)

                if len(alpha_result) == 0:
                    alpha_result = 0
                else:
                    alpha_result = alpha_result[0].n()

                self.X[0] = x1.subs(alpha, alpha_result)
                self.X[1] = x2.subs(alpha, alpha_result)

                self.k += 1
                self.count += 1
                self.result = self.func_result(self.X[0], self.X[1])
                data.append([self.count, tab, '%.5f' % self.X[0], tab, '%.5f' % self.X[1], tab, '%.5f' % self.result])

                self.x_array.append(self.X[0])
                self.y_array.append(self.X[1])
                self.z_array.append(self.result)
                if self.count == 1:
                    self.first_step_result = discard_zeros(
                        [self.X[0], self.X[1], self.func_result(self.X[0], self.X[1])])
                    print(self.first_step_result)
