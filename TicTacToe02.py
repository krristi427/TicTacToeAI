class TicTacToe:
    def __init__(self):

        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

        self.playerSymbol = ""
        self.playerPosition = []

        self.aiSymbol = ""
        self.aiPosition = []

        self.winner = None

        self.scoreBoard = None

        self.turn = 0

        self.optimalMove = int()

    def drawBoard(self):
        print(self.board[0] + " | " + self.board[1] + " | " + self.board[2])
        print("___" + "___" + "___")
        print(self.board[3] + " | " + self.board[4] + " | " + self.board[5])
        print("___" + "___" + "___")
        print(self.board[6] + " | " + self.board[7] + " | " + self.board[8])

    def choice(self):

        answer = input("What do you want to play as? (type x or o) ")

        if answer.upper() == "X":
            self.playerSymbol = "X"
            self.aiSymbol = "O"
        else:
            self.playerSymbol = "O"
            self.aiSymbol = "X"

        self.scoreBoard = {
            self.playerSymbol: -1,
            self.aiSymbol: 1,
            "tie": 0
        }

    def availableMoves(self):

        moves = []
        for i in range(0, len(self.board)):
            if self.board[i] == " ":
                moves.append(i)
        return moves

    def won_print(self):
        self.won()
        if self.winner == self.aiSymbol:
            print("AI wins :(")
            exit(0)
        elif self.winner == self.playerSymbol:
            print("Player Wins :)")
            exit(0)
        elif self.winner == "tie":
            print("Guess it's a draw")
            exit(0)

    def won(self):

        winningPositions = [{0, 1, 2}, {3, 4, 5}, {6, 7, 8},
                            {0, 4, 8}, {2, 4, 6}, {0, 3, 6},
                            {1, 4, 7}, {2, 5, 8}]

        for position in winningPositions:
            if position.issubset(self.playerPosition):
                self.winner = self.playerSymbol
                return True
            elif position.issubset(self.aiPosition):
                self.winner = self.aiSymbol
                return True
        if self.board.count(" ") == 0:
            self.winner = "tie"
            return True

        self.winner = None
        return False

    def set_i_ai(self, i):
        self.aiPosition.append(i)
        self.board[i] = self.aiSymbol

    def set_clear_for_ai(self, i):
        self.aiPosition.remove(i)
        self.board[i] = " "

    def set_i_player(self, i):
        self.playerPosition.append(i)
        self.board[i] = self.playerSymbol

    def set_clear_for_player(self, i):
        self.playerPosition.remove(i)
        self.board[i] = " "

    def findOptimalPosition(self):

        bestScore = float("-Infinity")
        elements = {}  # desperate times call for desperate measures

        for i in self.availableMoves():
            self.set_i_ai(i)
            score = self.minimax(False)
            if score > bestScore:
                bestScore = score
                elements[i] = bestScore
            self.set_clear_for_ai(i)
        if bestScore == 1:
            print("you fucked up larry")
        elif bestScore == 0:
            print("hm")
        else:
            print("whoops kristi made a prog. error")
        return max(elements, key=lambda k: elements[k])

    def minimax(self, isMaximizing):

        if self.won():
            return self.scoreBoard[self.winner]

        if isMaximizing:
            bestScore = float("-Infinity")
            for i in self.availableMoves():
                self.set_i_ai(i)
                bestScore = max(self.minimax(False), bestScore)
                self.set_clear_for_ai(i)
            return bestScore
        else:
            bestScore = float("Infinity")
            for i in self.availableMoves():
                self.set_i_player(i)
                bestScore = min(self.minimax(True), bestScore)
                self.set_clear_for_player(i)
            return bestScore

    def play(self):

        self.choice()

        while not self.won_print():
            if self.turn % 2 == 0:
                pos = int(input("Where would you like to play? (0-8) "))
                self.playerPosition.append(pos)
                self.board[pos] = self.playerSymbol
                self.turn += 1
                self.drawBoard()
            else:
                aiTurn = self.findOptimalPosition()
                self.aiPosition.append(aiTurn)
                self.board[aiTurn] = self.aiSymbol
                self.turn += 1
                print("\n")
                print("\n")
                self.drawBoard()
        else:
            print("Thanks for playing :)")


if __name__ == '__main__':
    tictactoe = TicTacToe()
    tictactoe.play()
