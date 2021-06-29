sudo apt update
sudo apt install snapd
sudo snap install core
sudo snap install teams-for-linux
echo "[Desktop Entry]
Name=Teams
Comment=Runs Teams
Icon=/home/pi/Downloads/Teams.png
Exec=/snap/teams-for-linux/current/teams-for-linux
Type=Application
Encoding=UTF-8
Terminal=false
Categories=None;" > /home/pi/Desktop/Teams.Desktop