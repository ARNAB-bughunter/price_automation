import smtplib
import requests
from bs4 import BeautifulSoup
import time
from datetime import datetime
import  pytz

def fun():
	web_url='https://www.flipkart.com/lenovo-ryzen-5-3600-8-gb-ram-nvidia-geforce-gtx-1650-super-graphics-1-tb-hard-disk-256-ssd-capacity-windows-10-64-bit-4-graphics-memory-gaming-tower/p/itmba80fd2a28a7d?pid=CPUFZFNTBU8VYAKV&otracker=wishlist&lid=LSTCPUFZFNTBU8VYAKVBAF9MB&fm=organic&iid=b15b8810-0462-4ad3-92af-cfe153d80c4b.CPUFZFNTBU8VYAKV.PRODUCTSUMMARY&ppt=hp&ppn=homepage&ssid=6knl05x84w0000001634223038259'

	r=requests.get(web_url)

	sub="YOU ITEM PRICE"
	body=''
	
	soup=BeautifulSoup(r.content,'html.parser')
	
	if (soup.find_all("div",{"class":"_16FRp0"})):
		body+='SOLD OUT,'
		body+='\n'
		body+=soup.find('div',{"class":"_30jeq3 _16Jk6d"}).string
	else:
		body+='NOW AVAILABLE,'
		body+='\n'
		body+=soup.find('div',{"class":"_30jeq3 _16Jk6d"}).string

	
	body+="\n Link: "+web_url

	body=body.replace("₹",'INR==>')



	my_msg=f'Subject: {sub}\n\n{body}'

	s=smtplib.SMTP('smtp.gmail.com',587)
	s.starttls()
	s.login('testnaha420@gmail.com', 'test5678910#?')

	s.sendmail('testnaha420@gmail.com', 'arnabnaha219@gmail.com', my_msg)
	s.quit()



my_hour=10
my_minute=11


while True:
	if datetime.now(pytz.timezone('Asia/Kolkata')).hour  == my_hour and datetime.now(pytz.timezone('Asia/Kolkata')).minute  == my_minute:
		fun()
		break
		
		
