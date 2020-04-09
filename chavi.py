	import sys
from pyPdf import PdfFileReader
from termcolor import colored

print colored('''
      
  .oooooo.   ooooo   ooooo       .o.       oooooo     oooo ooooo 
 d8P'  `Y8b  `888'   `888'      .888.       `888.     .8'  `888' 
888           888     888      .8"888.       `888.   .8'    888  
888           888ooooo888     .8' `888.       `888. .8'     888  
888           888     888    .88ooo8888.       `888.8'      888  
`88b    ooo   888     888   .8'     `888.       `888'       888  
 `Y8bood8P'  o888o   o888o o88o     o8888o       `8'       o888o   ''' ,'green' )
print colored("                                                       Version 0.1",'red')
            	    
print colored(" |  ........................................... |" ,'green')
print colored(" |                                              |" ,'green')          
print colored(" |  eAdhaar Pdf Password Cracker By @omi-k      |" ,'green')
print colored(" |  Useg : python chavi.py  <pdf_file>          |" ,'green')
print colored(" |  ........................................... |" ,'green')
#  (red, white, red, white, red, white, red, white, red, white, red, white,
#        red, white, end))

helpmsg = "Usage: chavi.py  pdf_file "
if len(sys.argv) < 1:
        print helpmsg
        sys.exit()
      
start = "1970"
end = "2016"
count= 1
pdffile = PdfFileReader(file(sys.argv[1], "rb"))
if pdffile.isEncrypted == False:
        print colored("[!] The file is not protected with any password. Exiting." ,'red')
        exit

print colored("[+] Attempting to Brute force. This could take some time...")
       
for x in range (int(start) , int(end)):
        with open("name.txt",'r') as f:
                for word in f.read().split():
                        # return(str(word)+str(x)) 
			sys.stdout.write('\r' + (str(word)+str(x)) )
			sys.stdout.flush() 
			count = count+ 1    
                        if pdffile.decrypt(str(word)+str(x)) > 0:
				print '\nNumber of combination tried ', count
                                print colored("\n[+]",'green') 
				print ('Password is:'  + str(word)+str(x))
                                print colored("\n[+]",'green') 
                                print ("[...Exiting...]")
                                sys.exit()




	   
