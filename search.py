def exist(board, word):
    def dfs(board, word, i, j, k):
        if k == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
            return False

        temp = board[i][j]
        board[i][j] = '#'
        result = (dfs(board, word, i + 1, j, k + 1) or
                  dfs(board, word, i - 1, j, k + 1) or
                  dfs(board, word, i, j + 1, k + 1) or
                  dfs(board, word, i, j - 1, k + 1))

        board[i][j] = temp

        return result

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == word[0] and dfs(board, word, i, j, 0):
                return True

    return False
