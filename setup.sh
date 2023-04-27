#!usr/bin/bash
sleep 2
echo -e "\e[91mNOTE : 200 MB storage space for setuping tools  \e[0m(Enter for start setuping) ";
sleep 1
read -p " : "
apt install exiftool -y
apt install php -y
apt install python3 -y
apt install git -y
pip install requests

echo -e "\e[92m setuping cloudflare\e[0m"
git clone https://github.com/BHUTUU/cloudflare-ui.git
bash cloudflare-ui/setup.sh
echo -e "\e[91m setuping done \e[0m"
chmod +x H-king.sh
sleep 1
echo "		"
sleep 2
echo "	"

echo -e "			\e[91m bash H-king.sh \e[0m ---> for starting tool"
