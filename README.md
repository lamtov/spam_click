## install chrome for ubuntu
## update chrome-driver for ubuntu
```
bash install_chrome.sh
```
## setup Japan font for ubuntu
```
sudo apt-get install language-pack-ja
sudo apt-get install japan*
```

## for window please validate version chrome to 88.0.4324.150 or download new chromedriver
https://chromedriver.chromium.org/downloads

## setup conda env minimal_example
```
wget https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
bash Anaconda3-2020.11-Linux-x86_64.sh
conda create -n minimal_example python=3.7 pyinstaller
conda activate minimal_example
conda install -y -c anaconda tk
conda install -y -c anaconda pillow

pip install selenium
pip install beautifulsoup4
pip install lxml
```
## run app
```
conda activate minimal_example
git clone https://github.com/lamtov/python_reins.git
cd python_reins
vim dataset/input.txt 
python main.py
```

```
pyinstaller --onefile  -F C:/Users/Lam/Documents/TOVANLAM_MMO/python_reins/main.py -p C:/Users/Lam/.conda/envs/minimal_example/python.exe
for window only
```

```angular2

pyinstaller --onefile  -F C:/Users/Lam/Documents/TOVANLAM_MMO/python_reins/main_a_hoan.py -p C:/Users/Lam/.conda/envs/minimal_example/python.exe

```