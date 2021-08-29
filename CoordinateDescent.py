from math import fabs
from Parser import discard_zeros

class CoordinateDescent:
    def __init__(self, eps, alpha, betta, X, coefficients):
        self.eps = eps
        self.alpha = alpha
        self.betta = betta
        self.X = X
        self.coefs = coefficients
        self.k = 0
        self.j = 0
        self.n = 2
        self.result = 0
        self.prev_result = 0
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
        while True:
            self.result = self.func_result(self.X[0], self.X[1])
            data.append([self.count, tab, '%.5f' % self.X[0], tab, '%.5f' % self.X[1], tab,
                         '%.5f' % self.result])

            if self.count == 0 or self.count == 1:
                self.first_step_result = discard_zeros([self.X[0], self.X[1], self.result])
                print(self.first_step_result)

            self.x_array.append(self.X[0])
            self.y_array.append(self.X[1])
            self.z_array.append(self.result)

            if fabs(self.prev_result - self.result) <= self.eps:
                return data
            self.prev_result = self.result
            success = False
            S = []
            self.j = self.k - self.n * (self.k // self.n) + 1

            for i in range(self.n):
                if i + 1 == self.j:
                    S.append(1)
                else:
                    S.append(0)

            x1 = self.X[0] + self.alpha * S[0]
            x2 = self.X[1] + self.alpha * S[1]

            if self.func_result(x1, x2) < self.result:
                self.X[0] = x1
                self.X[1] = x2
            else:
                x1 = self.X[0] - self.alpha * S[0]
                x2 = self.X[1] - self.alpha * S[1]
                if self.func_result(x1, x2) < self.result:
                    self.X[0] = x1
                    self.X[1] = x2

            if not success:
                if self.j == self.n:
                    self.alpha *= self.betta

            self.k += 1
            self.count += 1




