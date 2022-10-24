# Favicon-Hash
Calculate Favicon Hash for Shodan


## Setup
```
git clone https://github.com/kh4sh3i/Favicon-Hash.git
cd Favicon-Hash
pip3 install -r requirements.txt
```


## Usage
```
usage: favhash.py [-h] [-t TARGET] [-l LIST]

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        The hostname of the target, eg: github.com
  -l LIST, --list LIST  List of target url saperated with new line
```


## Example
```
python3 favhash.py -t github.com

python3 favhash.py -l test.txt
```