# Senkrypt
Senkrypt is a new encryption system made by me and takaso

# Basic usage
**disclosure: use "-" instead of the spaces to encrypt a word, don't use "<" or ">" as key**

**Encrypt a word:**

`python3 senkrypt.py -e oscuro -k key` ==> _`2a82ba2cc2602c02a8`_

**Decrypt a word:**

`python3 senkrypt.py -d 2a82ba2cc2602c02a8 -k key` ==> _`oscuro`_

# Old encoding system
## You can use senkrypt also without key, as encoding system


**Encode a word: (without key)**

`python3 senkrypt.py -e sesso` ==> _`22b23f23f1f923f`_

**Decode a word: (without key)**

`python3 senkrypt.py -d 22b23f23f1f923f` ==> _`sesso`_

**Credits**

@komodoooo

@takaso
