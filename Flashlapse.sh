if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
	cd /home/pi/Flashlapse_NEO
	git pull
fi

cd /home/pi/Flashlapse_NEO/_python
sudo python3 Main.py