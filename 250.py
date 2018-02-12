class BrokenChessboard:
    def minimumFixes(self, board):
        BW = ['B', 'W']
        cor_cell = 0
        resB = 0
        for R, row in enumerate(board):
            for C, v in enumerate(row):
                if v != BW[cor_cell]:
                    resB += 1

                cor_cell = (cor_cell + 1) % 2

        cor_cell = 1
        resW = 0
        for R, row in enumerate(board):
            for C, v in enumerate(row):
                if v != BW[cor_cell]:
                    resW += 1

                cor_cell = (cor_cell + 1) % 2

        res = min(resB, resW)

        return res

S = BrokenChessboard()
print(S.minimumFixes(["BWB", "BBW", "BWW"]))
print(S.minimumFixes(["BWBBB", "WWBBW", "BBBBW", "WBWBB"]))





