import fileinput


needExample = False
maxNumber = 5
class SemanticPattern:
    def __init__(self, word, pattern, example, count, exWord):
        self.word = word
        self.pattern = pattern
        self.example = example
        self.count = int(count)
        self.exWord = exWord

#make dictionary
f = open('result.txt', 'r')
dic = {}
for line in f:
	#print line
	tmp = line.split('\t')
	q = tmp[0]
	for i in range(1,len(tmp)-4):
		q = q + " " + tmp[i]
	pat = tmp[len(tmp)-4]
	sent = tmp[len(tmp)-3]
	count = tmp[len(tmp)-2]
	exWord = tmp[len(tmp)-1][0:len(tmp[len(tmp)-1])-1]
	if q not in dic:
		dic[q] = []
	dic[q].append(SemanticPattern(q,pat,sent,count,exWord))


for word in dic:
	dic[word] = sorted(dic[word], key=lambda ele: ele.count, reverse=True)
isEnding = False
commandMode = False
while True:
	if isEnding == True:
		break
	
	if commandMode == True:
		print("1.on/off example 2.change maximum number 3. back to query mode 4. exit ")
		while True:
			line = raw_input("command Mode--->")
			if line == "1":
				needExample = 1 - needExample
				if needExample == 1:
					print("Example on")
				else:
					print("Example off")
			if line == "2":
				tnum = int(raw_input("please enter a number: (1~10)"))
				if tnum > 0 and tnum < 10:
					maxNumber = tnum
					print "change to " + str(maxNumber)
				else:
					print "invalid number"
			if line == "3":
				commandMode = False
				break
			if line == "4":
				isEnding = True
				break
		continue
	line = raw_input("--->")
	if line == "#":
		commandMode = True
		continue
	if line in dic:
		cnt = 0
		for ele in dic[line]:
			print ele.word,
			print ele.pattern,
			print ele.count
			print ele.exWord
			if needExample:
				print ele.example
				print ""
			cnt = cnt + 1
			if cnt == maxNumber:
				break
	else:
		print "not found"
