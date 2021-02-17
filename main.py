import sys

import urllib.request as request
import random
import settings
from resolver import Resolver
import tldextract

# Variables
file = request.urlopen(settings.WORDS)

txt = file.read()
words = txt.splitlines()
if len(sys.argv) >= 2:
    label = tldextract.extract(sys.argv[1])
    print(f"{label.domain} -")
    if label.suffix:
        print(Resolver(sys.argv[1]).price())
    else:
        for TLD in settings.TLDS:
            domain = f"{label.domain}.{TLD}"
            print(Resolver(domain).price())
    print("\n")
else:
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
