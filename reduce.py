import fileinput
import sys
from operator import itemgetter, attrgetter
sents = []
for line in fileinput.input():
	line = line[0:len(line)-1]
	#line = line.lower()
	t = line.split('\t')
	for i in range(0,len(t)-2):
		t[i] = t[i].lower()
	sents.append(t)
def cal(ele):
	elen = len(ele)
	tmp = ""
	for i in range(0,elen-2):
		tmp = tmp + ele[i] + ' '
	return tmp
arr = sorted(sents, key=cal)
alen = len(arr)

def sameEle(ele1,ele2):
	len1 = len(ele1)
	len2 = len(ele2)
	if len1 != len2:
		return 0
	for i in range(0,len1-2):
		if ele1[i] != ele2[i]:
			return 0
	return 1
cnt = 1
exampleWord = {}
for i in range(0,alen):
	ok = 1
	ele = arr[i]
	if i < (alen-1):#not last
		ele2 = arr[i+1]
		if sameEle(ele,ele2) == 1:
			ok = 0
			cnt = cnt + 1
	word = ele[len(ele)-1]
	if word not in exampleWord:
		exampleWord[word] = 0
	exampleWord[word] = exampleWord[word] + 1

	if ok == 1:
		sorted_ex = sorted(exampleWord.items(), key=itemgetter(1),reverse=True)
		#print("=="+ele[len(ele)-1]+"==")
		for i in range(0,len(ele)-1):
			sys.stdout.write(ele[i]+'\t')
		sys.stdout.write(str(cnt) + '\t')
		z = 3 if len(sorted_ex) > 3 else len(sorted_ex)
		for i in range(0,z):
			if i != 0: sys.stdout.write(' ')
			sys.stdout.write(sorted_ex[i][0]+'(' + str(sorted_ex[i][1]) + ')')

		sys.stdout.write('\n')
		cnt = 1
		exampleWord = {}
