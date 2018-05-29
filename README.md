# Passphrase Generator

Generates secure passphrase from https://github.com/first20hours/google-10000-english 10000 English word list.

## Installation

### 1. Clone this repository

```
git clone https://github.com/hcngac/passphrase-generator.git
```

### 2. Clone google-10000-english into the repository

```
cd ./passphrase-generator
git clone https://github.com/first20hours/google-10000-english.git
```

### 3. Run main.py with Python 3

```
python3 ./main.py
```

## Usage

```
 
usage: main.py [-h] [-u] [-s] [-n WORDCOUNT] [-X MAXLEN] [-M MINLEN]

Generate password phrase from google-10000-english 10000 most frequent English
words.

optional arguments:
  -h, --help            show this help message and exit
  -u, --usa             Use USA version of 10000 most frequent words.
  -s, --no-swears       Exclude swear words.
  -n WORDCOUNT, --word-count WORDCOUNT
                        Number of words to form a pass phrase. (default: 4)
  -X MAXLEN, --max-word-length MAXLEN
                        Maximum number of letters in a word. (0 means
                        unlimited, default: 0)
  -M MINLEN, --min-word-length MINLEN
                        Minimum number of letters in a word. (0 means
                        unlimited, default: 6)
```