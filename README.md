Instructions
==========================

conda create -n venv python=2.7 anaconda

source venv/Scripts/activate

To install dependencies:
python -m pip install -r requirements.txt

install separately
 apt-get mongodb, enchant,
pip install redis, 
python-dateutil, egenix-mx-base 

git clone https://github.com/andymccurdy/redis-py.git
python setup.py install
```

To run tests:
```
nosetests tests
```

windows uses are required to install openssl manually
https://slproweb.com/products/Win32OpenSSL.html
linux users using debian/ubuntu sudo apt-get install openssl
