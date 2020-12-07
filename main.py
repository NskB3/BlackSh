#encoding=utf8
import os
import subprocess
import sys
import time
import datetime
import readline
try:
    import colors
except:
    print("\033[91m[-] Colors module not installed, installing...\033[0m\n")
    os.system("wget https://pastebin.com/raw/jFzVbx71 -O colors.py")
    import colors
    print(colors.OK + colors.white + " Colors module successfully installed!" + colors.end)
    time.sleep(5)
    os.system("clear")

logfile = "/opt/blacksh/log.txt" #DON'T CHANGE THX
historyfile = ".blacksh_history"
logo = """

{0}
██████  ██       █████   ██████ ██   ██ ███████ ██   ██ 
██   ██ ██      ██   ██ ██      ██  ██  ██      ██   ██ 
{1}██████  ██      ███████ ██      █████   ███████ ███████ 
██   ██ ██      ██   ██ ██      ██  ██       ██ ██   ██ 
{2}██████  ███████ ██   ██  ██████ ██   ██ ███████ ██   ██ 
                                                        
                   By Xynmaps/Dump                         {3}                               


""".format(colors.purple,colors.grey,colors.purple,colors.end)
helpmsg = """
{0}Commands:
------------------
{1}
help - prints this help message.
proxy - turns on proxychains (default).
noproxy - turns off proxychains.
exit - exits BlackSh.
{2}
""".format(colors.dark_blue,colors.grey,colors.end)
def pcomm(comm):
    c = subprocess.Popen("proxychains " + comm,shell=True,stdout=subprocess.PIPE)
    return c.stdout.read()

def ncomm(comm):
    c = subprocess.Popen(comm,shell=True,stdout=subprocess.PIPE)
    return c.stdout.read()

def log(text):
    open(logfile, "a+").write('\n' + text)
    
def historylog(text):
    open(historyfile, "a+").write('\n' + text)
    
def main():
    print logo
    proxy = 1
    if os.geteuid() != 0:
        sys.exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
    log("BlackSh Opened by {0} on {1}".format(datetime.datetime.now(),str(os.getlogin())))
    while 1:
        try:
            comm = raw_input("{0}{1}@{2}blacksh;>{3} ".format(colors.purple,str(os.getlogin()),colors.grey,colors.end))
        except KeyboardInterrupt:pass;comm=""
        except EOFError:pass;comm=""
        if comm.lower().strip() != "":
                if comm.lower().strip() == "help" or comm.lower().strip() == "?": print helpmsg
                elif comm.lower().strip() == "proxy": proxy = 1;print(colors.OK + " Proxy mode turned on." + colors.end)     
                elif comm.lower().strip() == "noproxy": proxy = 0;print(colors.OK + " Proxy mode turned off." + colors.end) 
                elif comm.lower().strip() == "exit": print(colors.OK + " Thanks for using BlackSh, Goodbye.");sys.exit()
                else:
                    if proxy == 1:
                        out = pcomm(comm)
                        print out
                    elif proxy == 0:
                        out = ncomm(comm)
                        print out
                historylog(comm)
if __name__ == '__main__':
    main()