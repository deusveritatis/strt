ag1=$1

x="172.28.${ag1}."
if  [ "$3" -eq 0 ] 
then
  for (( i=1; i<=$2; i++ ))
  do      
        let "s=2*i"
	ip="${x}${s}"
	if ping -c 1 "$ip" &> /dev/null
	then
		echo "$ip" >> "on_ip.txt"
	else

		echo "$ip" >> "off_ip.txt"
	fi
  done
else
  for (( i=0; i<=$2; i++ ))
  do      
        let "s=2*i+1"
	ip="${x}${s}"
	if ping -c 1 "$ip" &> /dev/null
	then
		echo "$ip" >> "on_ip.txt"
	else

		echo "$ip" >> "off_ip.txt"
	fi
  done
fi
