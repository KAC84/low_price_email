listEmails = ['dickface@yahoo.com','joe@gmail.com','fuckface@hotmail.com','4themail@yahoo.com'] 
listTitles = ['HEAT', 'PLAY ME', 'COWBOY', 'Saucy']

print listEmails[0]
print listEmails[1]

for item in range(0,2):
	print listEmails[item]

for item in range(1,100):
	print item

# for item in range(0,11):
# 	print listEmails[item]

for i, j in zip(listEmails,listTitles):
	print 'authorname: ' + i
	print 'booktitle: ' + j

print ' --------  ------  ----- - '

for i, j in zip(listTitles, listEmails):
	print 'authorname: ' + j
	print 'booktitle: ' + i

print ' --------  ------  ----- - '


for a in listEmails:
	for b in listTitles:
		print 'authorname: ' + a
		print 'booktitle: ' + b			