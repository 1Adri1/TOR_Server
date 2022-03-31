# import requests module
import requests
import sys
from requests.auth import HTTPBasicAuth
  
# Making a get request
#http://192.168.2.220/tor?tor=

# Change URL and auth to get it running.


def tornr(no):
    if(no==0):
        tor('http://192.168.2.220/tor?tor=')
    elif(no==1):
        tor('http://192.168.2.220/tor?tor=')
    elif(no==2):
        tor('http://192.168.2.221/tor?tor=')
    elif(no==3):
        tor('http://192.168.2.221/tor?tor=')
    elif(no==4):
        tor('http://192.168.2.222/tor?tor=')
    else:
        print("Wrong input")



def tor(adresse):
    response = requests.get(adresse + sys.argv[1],
    auth = HTTPBasicAuth('user', 'password'))
    print(response.text)


tornr(int(sys.argv[1]))


  
