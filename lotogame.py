import random as rd
import time

class PlayingMan:
	def __init__(self, name=None):
		self.name = name
		self.card = None
		self.make_card()

	def __str__(self):
		return ('-' * 11 + ' Your card ' + '-' * 12 + '\n') + '\n'.join(['\t'.join([str(elem) for elem in line]) \
		 for line in self.card]) + '\n' + ('-' * 34)

	def make_card(self):
		all_nums = [i for i in range(1, 91)]
		card_lines = []
		for i in range(3):
			time_list = []
			for i in range(5):
				number = rd.choice(all_nums)
				all_nums.remove(number)
				time_list.append(number)
			time_list.extend([' ', ' ', ' ', ' '])
			card_lines.append(rd.sample(time_list, len(time_list)))
		self.card = card_lines
		return self.card
class PlayingCom:
	def __init__(self):
		self.name = 'computer'
		self.com_card = None
		self.make_card()

	def __str__(self):
		return (('-' * 9 + ' Computers card ' + '-' * 9 + '\n')) + '\n'.join(['\t'.join([str(elem) for elem in line]) \
		 for line in self.com_card]) + '\n' + ('-' * 34)

	def make_card(self):
		all_nums = [i for i in range(1, 91)]
		card_lines = []
		for i in range(3):
			time_list = []
			for i in range(5):
				number = rd.choice(all_nums)
				all_nums.remove(number)
				time_list.append(number)
			time_list.extend([' ', ' ', ' ', ' '])
			card_lines.append(rd.sample(time_list, len(time_list)))
		self.com_card = card_lines
		return self.com_card

class LotoGame:
	def __init__(self):
		self.time1 = time.time()
		self.man = PlayingMan()
		self.computer = PlayingCom()
		self.boxes = rd.sample(range(1, 90 + 1), 90)

	def generator(self):
		for el in self.boxes:
			yield el

	def moves_round(self):
		g = self.generator()
		count = 89
		while True:
			for i in g:
				out = 0
				end = 0
				box = i
				print(f'New box: {box} (left {count})')
				count -= 1
				print(self.man)
				print(self.computer)
				man_input = (input(f'Cross out the number? (yes/no): '))
				if man_input != 'yes':
					if man_input != 'no':
						print('Well, what kind of moron cant enter "yes" or "no" normally, start playing again fuck(reload the programm)')
						time2 = time.time()
						nedd_time = time2 - self.time1
						print(f'You play {int(nedd_time)} seconds')
						print('You will exit in 15 sec, wait')
						time.sleep(15)
						return False
				if man_input == 'yes':
					for line in self.man.card:
						if not box in line:
							out += 1
						if box in line:
							index = line.index(box)
							line.remove(box)
							line.insert(index, '-')
					if out == 3:
						print('The game is over, there is no {} in your card'.format(box))
						time2 = time.time()
						nedd_time = time2 - self.time1
						print(f'You play {int(nedd_time)} seconds')
						print('You will exit in 15 sec, wait')
						time.sleep(15)
						return False
				if man_input == 'no':
					for line in self.man.card:
						if box in line:
							print('The game is over, there is {} in your card'.format(box))
							time2 = time.time()
							nedd_time = time2 -self.time1
							print(f'You play {int(nedd_time)} seconds')
							print('You will exit in 15 sec, wait')
							time.sleep(15)
							return False
				for line in self.computer.com_card:
					if box in line:
						index = line.index(box)
						line.remove(box)
						line.insert(index, '-')
					if not box in line:
						pass
				for line in self.man.card:
					if line.count('-') == 5:
						end += 1
						if end == 3:
							print('You WIN!!! Congratulations')
							time2 = time.time()
							nedd_time = time2 -self.time1
							print(f'You play {int(nedd_time)} seconds')
							print('You will exit in 15 sec, wait')
							time.sleep(15)
							return False
				end = 0
				for line in self.computer.com_card:
					if line.count('-') == 5:
						end += 1
						if end == 3:
							print('Computer win, sorry, you are loser!')
							time2 = time.time()
							nedd_time = time2 - self.time1
							print(f'You play {int(nedd_time)} seconds')
							print('You will exit in 15 sec, wait')
							time.sleep(15)
							return False

# a = input('The game is played using special cards on which numbers are marked, and chips (barrels) with numbers.' + '\n'
# 			'The game has 2 players: user and computer. Each at the beginning is given a random card.' + '\n'
# 			'Each turn, one random barrel is selected and displayed on the screen. A player card and a computer card are also displayed.' + '\n'
# 			'The number of barrels is 90 pieces (with numbers from 1 to 90).)' + '\n'
# 			'Enter anything to start: ')
if True:
	loto = LotoGame()
	loto.moves_round()
