# piglatin
Microservice to translate text into Pig Latin.


##Installation
```
git clone https://github.com/Curly-Mo/piglatin.git
python setup.py install
```

###Optional Dependencies
This service uses the NLTK library for parsing English vowel sounds. If NLTK is not installed, it will fallback to a naive parser that is unaware of silent consonants.
####Installation
```
# Install NLTK
pip install nltk
# Install NLTK data
python -m nltk.downloader all
```

##Run
```
sudo python manage.py server --port 80
# or without sudo privileges
python manage.py server --port 5000
```

##Usage
```
curl -G http://localhost:80/translate --data-urlencode "text=Translate this text into Piglatin."
```
####Expected Response
```
{
  "text": "Anslatetray isthay exttay intoyay Iglatinpay."
}
```

##Testing
###Install test extras
```
pip install -e ".[test]"
```
###Run
```
python test.py
```
