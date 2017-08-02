from nltk.corpus import wordnet as wn
import fileinput
import sys

#f = open("bbtest.txt", "r")



def is_prep(word):
	if word[2] == "IN":
		return 1
	else:
		return 0
def is_verb(word):
	if word[2] == 'VB' or word[2] == "VBD" or word[2] == "VBG":
		return 1
	else:
		return 0

def is_DT(word):
	if word[2] == "DT":
		return 1
	else:
		return 0

def is_JJ(word):
	if word[2] == "JJ":
		return 1;
	else:
		return 0;

def is_NN(word):
	if word[2] == "NN" or word[2] == "NNS":
		return 1;
	else:
		return 0;

def print_sent(sent):
	slen = len(sent)
	for i in range(0,slen):
		if i != 0:
			sys.stdout.write(' ')
		sys.stdout.write(sent[i][0])
	sys.stdout.write('\t')		

def print_result(pat):
	plen = len(pat)
	for i in range(0,plen):
		sys.stdout.write(pat[i] + '\t')
	#sys.stdout.write('\n')

def trans(word):
	synset = wn.synsets(word,'n')
	if(synset):
		return synset[0].lexname()
	else:
		return word
def verb_grammar(sent):
	slen = len(sent)
	for i in range(0,slen):
		if is_verb(sent[i]):
			res = []
			#print("===> " + sent[i][1] + " "),
			res.append(sent[i][1])
			state = 0
			for j in range(i+1,slen):
				if state == 0:	#first state
					if is_prep(sent[j]):
						res.append(sent[j][1])
						state = 1;
					elif is_DT(sent[j]):
						state = 2;
					elif is_JJ(sent[j]):
						state = 3;
					elif is_NN(sent[j]):
						res.append(trans(sent[j][1]))
						print_result(res)
						print_sent(sent)
						sys.stdout.write(sent[j][1].lower())
						sys.stdout.write('\n')

						break
					else: 
						break
				elif state == 1: #PERP
					if is_prep(sent[j]):
						res.append(sent[j][1])
						state = 1;
					elif is_DT(sent[j]):
						state = 2;
					elif is_JJ(sent[j]):
						state = 3;
					elif is_NN(sent[j]):
						res.append(trans(sent[j][1]))
						print_result(res)
						print_sent(sent)
						sys.stdout.write(sent[j][1].lower())
						sys.stdout.write('\n')
						break
					else: 
						break
				elif state == 2: #DT
					if is_DT(sent[j]):
						state = 2;
					elif is_JJ(sent[j]):
						state = 3;
					elif is_NN(sent[j]):
						res.append(trans(sent[j][1]))
						print_result(res)
						print_sent(sent)
						sys.stdout.write(sent[j][1].lower())
						sys.stdout.write('\n')
						break
					else:
						break
				elif state == 3: #JJ
					if is_JJ(sent[j]):
						state = 3;
					elif is_NN(sent[j]):
						res.append(trans(sent[j][1]))
						print_result(res)
						print_sent(sent)
						sys.stdout.write(sent[j][1].lower())
						sys.stdout.write('\n')
						break
					else:
						break

def ADJ_grammar(sent):
	slen = len(sent)
	for i in range(0,slen):
		if is_JJ(sent[i]):
			res = []
			#print("===> " + sent[i][1] + " "),
			res.append(sent[i][1])
			state = 0
			for j in range(i+1,slen):
				if state == 0:	#first state
					if is_NN(sent[j]):
						res.append(trans(sent[j][1]))
						print_result(res)
						print_sent(sent)
						sys.stdout.write(sent[j][1].lower())
						sys.stdout.write('\n')
						break
					else: 
						break
input = []
for line in fileinput.input():
	if line != "\n":
		d = line.split('\t')
		input.append(d)
	else:
		#print(len(input))
		verb_grammar(input)
		ADJ_grammar(input)
		input = []


#VB/VBP/VBD (PREP) (DT) (JJ) NN
#JJ NN