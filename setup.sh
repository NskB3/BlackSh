clear
echo "BLACKSH INSTALLER SCRIPT ;BY XYNMAPS;"
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi
sleep 2
echo "UPDATING PACKAGE LISTS..."
sleep 2
apt-get update -y
clear
echo "INSTALLING WGET..."
sleep 2
apt install wget -y
logdate=`date`
clear
echo "INSTALLING PYTHON2..." 
sleep 2
apt install python2 -y
clear
echo "INSTALLING AND STARTING TOR..."
sleep 2
apt install tor -y
tor &
sleep 10
clear
echo "INSTALLING AND CONFIGURING PROXYCHAINS..."
sleep 2
apt install proxychains -y
echo "socks4 127.0.0.1 9050" >> /etc/proxychains.conf
echo "quiet_mode" >> /etc/proxychains.conf
clear
echo "CREATING LOGDIR/LOGFILE..."
sleep 2
mkdir /opt/blacksh
clear
echo "logfile created at $logdate" >> /opt/blacksh/log.txt
echo "clear" >> .blacksh_history
echo "WGETTING COLORS MODULE..."
sleep 2
wget https://pastebin.com/raw/jFzVbx71 -O colors.py
clear
echo "SETUP DONE."