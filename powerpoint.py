import os
import time
import sys

def read_textual_powerpoint(filepath):
	blocks = []
	with open(filepath, "r") as ins:
		line_number = 0
		current_block = []
		for line in ins:
			new_block = False
			
			if len(line) > 0 and line[0].isalpha() and len(current_block) > 0:
				blocks.append(current_block)
				current_block = []

			# print line
			current_block.append(line)
			line_number += 1

		if len(current_block) > 0:
			blocks.append(current_block)

	return blocks

def print_blocks(blocks):
	for block in blocks:
		print_block(block)

def print_block(block):
	for line in block:
		sys.stdout.write(line)

def clear_page():
	clear = lambda: os.system('clear')
	clear()

def app(filepath):
	blocks = read_textual_powerpoint(filepath)

	def inp_loop(block_index=0):
		clear_page()
		print_block(blocks[block_index])

		inp = raw_input('\n:')

		if inp == 'j' or inp == 'd':
			block_index -= 1
		if inp == 'k' or inp == 'f':
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


