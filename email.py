from _misc import listEmails, listTitles
import time 

senderEmail  = 'kcowser@randomhouse.com'
emailSubject = 'Subject: Low Price Promo for ' 

stop_time = 0.5


messageFrom = 'From: From Person ' + senderEmail
messageTo   = 'To: To Person '
messageBody = 'This is a test e-mail message.'
#create an Subject variable

for emailaddy, title in zip(listEmails,listTitles):

	print messageFrom 
	print messageTo + emailaddy
	print emailSubject + title.upper() #this merges the subject line variable declared up top to the title and then uppercases the title
	print ''
	print messageBody
	print '--------'
	time.sleep(stop_time)


