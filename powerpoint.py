import os
import time
import sys




def read_textual_powerpoint(filepath):
	blocks = []
	with open(filepath, "r") as ins:
		current_block = []
		for line in ins:
			new_block = False
			
			if len(line) > 0 and line[0] != "" and line[0] != "\t" and line[0] != "\n":
				blocks.append(current_block)
				current_block = []

			current_block.append(line)

	return blocks

def print_block(block):
	for line in block:
		sys.stdout.write(line)

def clear_page():
	clear = lambda: os.system('clear')
	clear()

def app(filepath):
	blocks = read_textual_powerpoint(filepath)
	print blocks

	def inp_loop(block_index=0):
		clear_page()
		print_block(blocks[block_index])

		inp = raw_input(':')

		if inp == 'j':
			block_index -= 1
		if inp == 'k':
			block_index += 1
		if inp == 'q':
			sys.exit()

		if block_index < 0:
			block_index = len(blocks) - 1
		elif block_index > len(blocks) - 1:
			block_index = 0

		inp_loop(block_index)
	inp_loop()

if len(sys.argv) < 2:
	print "You need to supply a file to read"
else:
	app(sys.argv[1])


