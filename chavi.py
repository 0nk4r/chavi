import sys
import PyPDF2
from PyPDF2 import PdfFileReader
import time
from termcolor import colored  ,cprint

cprint  ('''
      
  .oooooo.   ooooo   ooooo       .o.       oooooo     oooo ooooo 
 d8P'  `Y8b  `888'   `888'      .888.       `888.     .8'  `888' 
888           888     888      .8"888.       `888.   .8'    888  
888           888ooooo888     .8' `888.       `888. .8'     888  
888           888     888    .88ooo8888.       `888.8'      888  
`88b    ooo   888     888   .8'     `888.       `888'       888  
 `Y8bood8P'  o888o   o888o o88o     o8888o       `8'       o888o   ''' ,"green" )
cprint  ("                                                       Version 1.2",'red')
            	    
cprint  (" |  ........................................... |" ,'green')
cprint  (" |                                              |" ,'green')          
cprint  (" |  eAdhaar Pdf Password Cracker By @omi-k      |" ,'green')
cprint  (" |  Useg : python chavi.py  <pdf_file>          |" ,'green')
cprint  (" |  ........................................... |" ,'green')

helpmsg = "Usage: chavi.py  pdf_file "
if len(sys.argv) < 1:
    print (helpmsg)
    sys.exit()
      
start = "1971"
end = "2016"
count= 1
pdffile = PdfFileReader(sys.argv[1])

if not pdffile.isEncrypted:
    print("[!] The file is not protected with any password. Exiting.....")
    time.sleep(1)
    sys.exit()

cprint  ("\n[+] Attempting to Brute force. This could take some time...",'green')
cprint("Trysting ",'blue') 

for x in range (int(start) , int(end)):
    with open("name.txt",'r') as f:
        for word in f.read().split():
            # return(str(word)+str(x))
            sys.stdout.write('\r' + (str(word)+str(x)) )
            sys.stdout.flush() 
            count = count+ 1    
            if pdffile.decrypt(str(word)+str(x)) > 0:
             sys.stdout.flush()
             cprint  ("\n[+]",'green',end='') 
             print ('Number of combination tried ', count)
             cprint  ("\n[+]",'green',end='')  
             print ('Password is:'  + str(word)+str(x))
             cprint  ("\n[+]",'green',end='') 
             print ("[...Exiting...]")
             sys.exit()  


	   
