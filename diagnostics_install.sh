#!/bin/sh
mkdir -p /usr/local/avanslora
cd /usr/local/avanslora
echo "Cloning DiagnosticsCircuit and Adafruit_Python_DHT repos..."
git clone https://github.com/AvansLora/DiagnosticsCircuit.git
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
apt install build-essential python-dev python-pip -y
cd /usr/local/avanslora/Adafruit_Python_DHT
python setup.py install
pip install requests
echo "append 'cd /usr/local/avanslora/DiagnosticsCircuit/ && python index.py &' to /etc/rc.local"
sudo sed -i -e '$i cd /usr/local/avanslora/DiagnosticsCircuit/ && python index.py &\n' /etc/rc.local
