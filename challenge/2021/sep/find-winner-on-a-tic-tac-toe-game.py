class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        def checkWin(moves):
            row = [0, 0, 0]
            col = [0, 0, 0]
            dia = [0, 0]
            for m in moves:
                row[m[0]] += 1
                col[m[1]] += 1
                if (m[0] == m[1]):
                    dia[0] += 1
                if (m[0] + m[1] == 2):
                    dia[1] += 1
            if (row.count(3) or col.count(3) or dia.count(3)):
                return True
            return False

        A = moves[0::2]
        B = moves[1::2]

        if (checkWin(A)):
            return "A"
        elif (checkWin(B)):
            return "B"
        elif (len(moves) == 9):
            return "Draw"
        else:
            return "Pending"

s = Solution()
print(s.tictactoe([[0,0],[2,0],[1,1],[2,1],[2,2]]))
