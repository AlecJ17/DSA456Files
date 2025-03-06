# Main Author:
# Main Reviewer:

from ctypes.wintypes import tagPOINT
from a1_partd import get_overflow_list, overflow
from a1_partc import Queue

def copy_board(board):
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board


### Kevin

def evaluate_board(board, player):
    # win and lose have same score
    winning_score = float('inf')
    losing_score = float('-inf')

    total_board_gems = 0
    player_num_gems = 0

    # Loop into each cell of board
    # if cell != 0 add into total_board_gems
    # check cell player 1 or player 2 and then player_num_gems
    # check winning or losing and return player_num_gems
    for row in board:
        for cell in row:
            if cell != 0:
                total_board_gems += abs(cell)
                if (player == 1 and cell > 0) or (player == -1 and cell < 0):
                    player_num_gems += abs(cell)
    if player_num_gems == total_board_gems:
        return winning_score
    if player_num_gems == 0:
        return losing_score
    return player_num_gems


class GameTree: # Kevin
    class Node:
        def __init__(self, board, depth, player, tree_height = 4):
            self.board = board
            self.depth = depth
            self.player = player
            self.children = []
            self.score = None
            self.move = None
    def __init__(self, board, player, tree_height = 4):
        self.player = player
        self.board = copy_board(board)
        self.root = self.Node(board, 0, player)
        self.tree_height = tree_height
        self.build_tree(self.root, tree_height)

    #Kevin
    def build_tree(self, node, height):
        if height == 0: # conditon stop recursive
            return
        # Loop all cell of board
        for row in range(len(node.board)):
            for col in range(len(node.board[0])):
                # if board empty or board belong to player => copy node to new board and assign newboard[row][col] +=node.player +1
                if node.board[row][col] == 0 or node.board[row][col] * node.player > 0:
                    newboard = copy_board(node.board)
                    newboard[row][col] += node.player

                    # solve overflow
                    if get_overflow_list(newboard):
                        queue= Queue()
                        queue.enqueue(newboard)
                        overflow(newboard, queue)
                        newboard = queue.dequeue()

                    # After solve overflow create Node depth+1 for oppenent Player
                    child_node = self.Node(newboard, node.depth + 1, -node.player)

                    child_node.move = (row, col)
                    node.children.append(child_node)

                    # call recurisve to tree_height -1
                    self.build_tree(child_node, height - 1)

    #Alec
    def minimax(self, node):
        if not node.children:
            node.score = evaluate_board(node.board, node.player)
            return node.score

        if node.depth % 2 == 0:  # Maximizer's turn
            max_score = float('-inf')  # Initialize to negative when compare with score
            for child in node.children:
                score = self.minimax(child)
                max_score = max(max_score, score)  # update max_score
            node.score = max_score
        else:  # Minimizer's turn
            min_score = float('inf')  # Initialize to positive infinity
            for child in node.children:
                score = self.minimax(child)
                min_score = min(min_score, score)  # Update min_score
            node.score = min_score

        return node.score

    #Alec
    def get_move(self):
        maxscore = float('-inf')

        # Search and find the best move in children with minimax algorithm
        for child in self.root.children:
            score = self.minimax(child)
            if score > maxscore:
                maxscore = score
                best_move = child.move
        return best_move
        #Alec
    def clear_tree(self):
        self.delete_nodes(self.root)

    def delete_nodes(self, node):
        if not node:
            return
        for child in node.children:
            self.delete_nodes(child)
        del node






