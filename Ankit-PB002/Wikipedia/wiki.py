import sys
import wikipedia
from time import gmtime, strftime
import time
import socket
from progressbar import ProgressBar

pbar = ProgressBar()
# print pbar
text= sys.argv
if(len(text)>1):
	article=" ".join(text[1:])
else:
	article=raw_input("Please enter the article name: ")
# temp=wikipedia.search(article)
# print temp
# data = wikipedia.page(temp[0])
try:
    data = wikipedia.page(article)
    # print data.summary
except:
    articles = wikipedia.search(article)
    print "There are too many \""+article+"\" select from the following:"
    for i, temp in enumerate(articles):
    	if temp.lower()!= article.lower():
        	print i, temp
    choice = int(raw_input("Enter a choice(number): "))
    # assert choice in xrange(len(topics))
    data=wikipedia.page(articles[choice])



time= strftime("%Y-%m-%d %H:%M:%S", gmtime())
ip= socket.gethostbyname(socket.gethostname())
f=open("wiki.log","a")
f.write(ip+" "+time+" "+data.title+" "+data.url+"\n")
# pbar.stop()
# pbar.join()
# for i in range(100):
#     time.sleep(1)
#     sys.stdout.write("\r%d%%" % i)
#     sys.stdout.flush()
# print data.title
# print data.url