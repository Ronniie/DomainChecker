import urllib.request as request
import random
import settings
from resolver import Resolver
# Variables
file = request.urlopen(settings.WORDS)

txt = file.read()
words = txt.splitlines()

while True:
    label = (
        random.choice(words).decode("UTF-8").rstrip().capitalize() +
        random.choice(words).decode("UTF-8").rstrip().capitalize()
    )
    print(f"{label} -")
    for TLD in settings.TLDS:
        domain = f"{label}.{TLD}"
        print(Resolver(domain).price())

    print("\n")
