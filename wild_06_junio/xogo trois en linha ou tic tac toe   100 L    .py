import os

os.system("clear")

class Board():
	def __init__(self):
		self.cells = ["N", " ", " ", " ", " ", " ", " ", " ", " ", " "]

	def display(self):
		print (" %s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
		print ("-----------")
		print (" %s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
		print ("-----------")
		print (" %s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
		print ("-----------")

	def update_cell(self, cell_number, player):
		if self.cells[cell_number] == " ":
			self.cells[cell_number] = player

	def is_winner(self, player):
		if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
			return True
		if self.cells[4]==player and self.cells[5]==player and self.cells[6]==player:
			return True
		if self.cells[7]==player and self.cells[8]==player and self.cells[9]==player:
			return True
		if self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
			return True
		if self.cells[3]==player and self.cells[5]==player and self.cells[7]==player:
			return True
		if self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
			return True
		if self.cells[2]==player and self.cells[5]==player and self.cells[8]==player:
			return True
		if self.cells[3]==player and self.cells[6]==player and self.cells[9]==player:
			return True	
		return False

	def is_tie(self):
		# if board.is_winner(player1) == False and board.is_winner(player2) == False and " " not in self.cells:
		if " " not in self.cells:
			return True
		else:
			return False

	def reset(self):
		self.cells = ["N", " ", " ", " ", " ", " ", " ", " ", " ", " "]


board = Board()

def print_header():
	print("Welcome to Tic -Tac_Toe\n")   #by adding \n, skip a line below

def refresh_screen():
	#clear screen
	os.system("clear")
	print_header()
	board.display()

turn = "X"
while True:
	refresh_screen()
	global player	

	#check winner and print
	if board.is_winner("X"):
		print("\nX wins! \n")
		play_again = input("Would you like to play again? (Y/N) >").upper()  #if input lowercase will be converted into uppercase.
		if play_again == "N":
			break
		else:
			board.reset()
			refresh_screen()
	elif board.is_winner("O"):
		print("\nO wins! \n")
		play_again = input("Would you like to play again? (Y/N) >").upper()  #if input lowercase will be converted into uppercase.
		if play_again == "N":
			break
		else:
			board.reset()
			refresh_screen()
	if board.is_tie():
		print("\n It a tie game. \n")
		play_again = input("Would you like to play again? (Y/N) >").upper()  #if input lowercase will be converted into uppercase.
		if play_again == "N":
			break
		else:
			board.reset()
			refresh_screen()

	# get X input
	choice = int(input("\n%s) Please choose 1-9. >" %turn))  #input(" ")  can get the input you type in after the string
	#update board
	board.update_cell(choice, turn)
	if turn == "X":
		turn = "O"
	else:
		turn ="X"