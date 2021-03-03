import ftplib
global ftp
ftp= ftplib.FTP()

host = "waws-prod-dm1-059.ftp.azurewebsites.windows.net"
port = 21
ftp.connect(host, port)
print (ftp.getwelcome())
try:
     print ("Logging in...")
     ftp.login("lextor\$lextor", "Wdbb7kgJs96zTLFDlk4dgxqKahuqkEnhhPlgueEgc3cbWiP2fQ4C01KkTE7R")
     print ("Logged in...")
     ftp.cwd('/site/wwwroot')
     ftp.storbinary('STOR sonicread.txt', open('sonicread.txt','rb'))
     print ("Upload Successful...")
except:
     "failed to login"
raw_input('Press Enter to exit')
