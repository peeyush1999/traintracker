import urllib2
from bs4 import BeautifulSoup
import os
import cookielib
import time


#-----------------------fields which needs to be change--------------------

print "never miss your train with train guru"
#Create Way2sms Id 
uname = "Way2Sms u name"
pass = " Way2Sms Password"

#enter mobile number in which you want to send text
mnumber = "Enter Mobile Number"

#enter Train number for which you want text
trainno ="Enter Train Number"

#enter your destination name in capital letter with correct spelling
destname = "Enter Destination Name"

note ="HOPE YOU HAVE HAPPY AND SAFE JOURNEY!!!!"



#----------------------------------------------------------------------------



#==========DO NOT ALTER BELOW CODE===============




def sendtext(message,number):
    #message = raw_input("Enter text: ")
    #number = raw_input("Enter number: ")

    if __name__ == "__main__":    
        username = "your_login_id"
        passwd = "your_password"

        message = "+".join(message.split(' '))

     #logging into the sms site
        url ='http://site24.way2sms.com/Login1.action?'
        data = 'username='+uname+'&password='+pass+'&Submit=Sign+in'

     #For cookies

        cj= cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

     #Adding header details
        opener.addheaders=[('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120')]
        try:
            usock =opener.open(url, data)
        except IOError:
            print "error"
            #return()

        jession_id =str(cj).split('~')[1].split(' ')[0]
        send_sms_url = 'http://site24.way2sms.com/smstoss.action?'
        send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'
        opener.addheaders=[('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
        try:
            sms_sent_page = opener.open(send_sms_url,send_sms_data)
        except IOError:
            print "error"
            #return()

        print "success" 
        #return ()




def traindata():

    #trainno = raw_input("Enter Train Number  : ")

    


    newurl = "http://spoturtrain.com/status.php?tno="+trainno+"&date=0"

    source = urllib2.urlopen(newurl)

    soup = BeautifulSoup(source ,"html.parser" )

    #print soup.prettify()

    links = soup.find_all('table')

    print links[1]

    #text = str(links)
    #print links[1].text
    return links[1].text



#-----------------------------------------------------------------


i=0

checktext = "#"

#sendtext(note,mnumber)
while(i!=1):

    
    


    temptext = traindata()
    text = temptext
    temptext = "+".join(temptext.split(" "))
    temptext = temptext.replace("++++++++++++++++++++","")
    temptext = temptext.replace("\n","")

    ctext =temptext.split(",")
    dest = temptext.split(" ")
    ctext =ctext[1] 


    #--------------------------------------------------------- 
    if(ctext != checktext):
        checktext = ctext
        print "checktest 2 " + checktext
        
        sendtext(temptext,mnumber)
    else:
        print "NO CHANGE!!!!"
        
    
    if(destname in dest):
        sendtext(destname+" is next station ",mnumber)

    if(("Arrived at "+destname in text) or ("Reached "+destname in text)) :
        i=1
        sendtext("Train Arrived at "+destname+" . Thank You for using Train Tracker",mnumber)    





    #------------------------------------------------------------
    time.sleep(15)

   

