class LongestCommomSubsequence():
    def __init__(self, txt1, txt2):
        self.x = len(txt1)
        self.y = len(txt2)
        self.txt1 = txt1
        self.txt2 = txt2
        self.dptable = [[None]*(self.x + 1) for i in range(self.y + 1)]
    def mainFunc(self):
        for i in range(self.x+1):
            for j in range(self.y+1):
                if i == 0 or j == 0:
                    self.dptable[i][j] = 0
                elif self.txt1[i-1] == self.txt2[j-1]:
                    self.dptable[i][j] = 1 + self.dptable[i-1][j-1]
                else:
                    self.dptable[i][j] = max(self.dptable[i-1][j], self.dptable[i][j-1])

        return self.dptable[self.x][self.y]
X = 'ABCBAB'
Y = 'ACADRK'
test = LongestCommomSubsequence(X, Y)
print(test.mainFunc())
        