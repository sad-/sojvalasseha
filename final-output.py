# Takes in a bunch of .out files containing solutions for corresponding .in files 
# and outputs a single solutions.out file

out = open('solutions.out', 'w')
for i in range(1,493):
	try: 
		s = 'final/' + str(i) + '.out'
		f = open(s, 'r')
		curr = ''
		for line in f:
			curr += line[:-1] + '; '
		out.write(curr + '\n')
	except FileNotFoundError:
		out.write('None\n')