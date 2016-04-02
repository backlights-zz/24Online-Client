import urllib2
import socket
import sys
import ssl
class LPUnet(object):
    def __init__(self,user_id,password):
        self.user_id = user_id
        self.password = password
        self.URL = 'https://internet.lpu.in/24online/servlet/E24onlineHTTPClient'
    def connect(self):
        self.post_data = "mode=191&logintype=2&ipaddress="+socket.gethostbyname(socket.gethostname())+"&mac=08%3A5b%3A0e%3A40%3Aed%3A5a&servername=172.20.2.2&username="+self.user_id+"&password="+self.password
        try:
            #turn off the SSL verification
            ssl._create_default_https_context = ssl._create_unverified_context
            
            #disabling the default system Proxy Settings
            proxy = urllib2.ProxyHandler({})
            opener = urllib2.build_opener(proxy)
            urllib2.install_opener(opener)
            
            #posting the data to the server
            resp=urllib2.urlopen(self.URL,self.post_data,60).read()                
            
            print resp[resp.find('message='):resp.find('&',resp.find('message='))]
            
        except Exception as ex:
            print "[ERROR]: "+str(ex)
        

#main
try:
    lpu = LPUnet(sys.argv[1],sys.argv[2])
    lpu.connect()
    del lpu    
except Exception as ex:
    print "[ERROR] : use 24Online-Client [user_id] [password]"
    print str(ex)
