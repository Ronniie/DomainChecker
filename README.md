<p align="center">
  <img src="https://media.discordapp.net/attachments/296460174074576897/811637699630727178/unknown.png" alt="DomainChecker"/>
  </a>
</p>

# DomainChecker
DomainChecker grabs two random words, combines them and checks configured TLDs. This is a simple Python Script, which will be expanded.
## How to install:
Run these following commands.
```
virtualenv venv --python=python3
pip3 install -r requirements.txt
python3 main.py
```
## How to use:
Any of these commands works!
```
python3 main.py # Loops through random words, and shows the selected TLDs. 
python3 main.py DomainName # Loops through selected TLDs.
python3 main.py DomainName.com # Searches for the selected domain and TLD.
```

# Todo
- Add Commenting.
- Possibile Optimizations.
- - Scrap all prices from same page?
- Django Application
- - Dashboard with approval, sends user to checkout page?
- - Stores within a Database, constantly running in the background using Docker.
- - Possible auto buy when approved instead of sending to a checkout page?
