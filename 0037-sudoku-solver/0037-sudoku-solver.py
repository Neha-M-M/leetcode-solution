class Solution:
    def solveSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        # Initialize
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empty.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + c // 3].add(val)

        def backtrack(i):
            if i == len(empty):
                return True

            r, c = empty[i]
            box = (r // 3) * 3 + c // 3

            for val in "123456789":
                if val not in rows[r] and val not in cols[c] and val not in boxes[box]:
                    board[r][c] = val
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box].add(val)

                    if backtrack(i + 1):
                        return True

                    # undo
                    board[r][c] = "."
                    rows[r].remove(val)
                    cols[c].remove(val)
                    boxes[box].remove(val)

            return False

        backtrack(0)
