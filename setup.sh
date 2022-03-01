apt-get install libcurl4-openssl-dev -y
apt-get install libssl-dev -y
apt-get install libjansson-dev -y
apt-get install automake -y
apt-get install autotools-dev -y  
apt-get install build-essential -y
apt-get install nano -y


chmod +x edit-miner
chmod +x run-miner


apt-get install python3 -y
apt-get install pip -y
python3 -m pip install progress
python3 -m pip install requests


mv src_run_ccminer ../../etc
mv edit-miner ../../bin
mv run-miner ../../bin


run-miner


cd && cd ../etc/src_run_ccminer/ccminer_mmv
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
./build.sh

cd && cd ../etc
nano bash.bashrc

run-miner