import wikipedia
import time
import datetime
import socket
i=0
file_name=open("result.log","a")
while(i!=1):
	name =raw_input("Enter the world you want to search: ")
	
	try:
		page_result=wikipedia.page(name)
	except:
		result=wikipedia.search(name)
		print "There are many names of this Kind ....Choose one index"
		for t in range(0,len(result)):
			if name.lower()!=result[t].lower():
				print str(t)+" "+result[t]
		index=raw_input();
		page_result=wikipedia.page(result[int(index)])
	link_result=page_result.url
	print link_result
	ip=socket.gethostbyname(socket.gethostname())
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	file_name.write(ip+" "+st+" Name= "+name+"  Link= "+link_result+"\n \n")
	temp=raw_input("Enter 1 to stop: ")
	i=int(temp)

file_name.close()