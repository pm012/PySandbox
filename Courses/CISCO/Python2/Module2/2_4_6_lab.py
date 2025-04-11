'''
Your task is to write a program which is able to simulate the work of a seven-display device, although you're going to use single LEDs instead of segments.

Each digit is constructed from 13 LEDs (some lit, some dark, of course) – that's how we imagine it:

  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###
Note: the number 8 shows all the LED lights on.

Your code has to display any non-negative integer number entered by the user.

Tip: using a list containing patterns of all ten digits may be very helpful.
'''

digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number1(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


digits_map = {
    '0': [
        " ### ",
        "#   #",
        "#   #",
        "#   #",
        " ### "
    ],
    '1': [
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  ",
        "  #  "
    ],
    '2': [
        " ### ",
        "    #",
        " ### ",
        "#    ",
        " ### "
    ],
    '3': [
        " ### ",
        "    #",
        " ### ",
        "    #",
        " ### "
    ],
    '4': [
        "#   #",
        "#   #",
        " ### ",
        "    #",
        "    #"
    ],
    '5': [
        " ### ",
        "#    ",
        " ### ",
        "    #",
        " ### "
    ],
    '6': [
        " ### ",
        "#    ",
        " ### ",
        "#   #",
        " ### "
    ],
    '7': [
        " ### ",
        "    #",
        "   # ",
        "  #  ",
        "  #  "
    ],
    '8': [
        " ### ",
        "#   #",
        " ### ",
        "#   #",
        " ### "
    ],
    '9': [
        " ### ",
        "#   #",
        " ### ",
        "    #",
        " ### "
    ]
}

def print_number(number):
    num_str = str(number)
    # Create 5 empty lines
    output_lines = ['' for _ in range(5)]
    
    # For each digit, append its lines
    for digit in num_str:
        digit_lines = digits_map[digit]
        for i in range(5):
            output_lines[i] += digit_lines[i] + '  '  # add spacing between digits
    
    # Print all lines
    for line in output_lines:
        print(line)

if __name__ == "__main__":
    number = input("Enter the number you wish to display: ")
    print_number(number)
    print_number1(number)

    