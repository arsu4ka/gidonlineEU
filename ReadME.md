# Gidonline.eu account creation script

This is a simple python script written using requests-html library and some others. It's made for fun, just to improve some practical skills not meant to abuse, hack or ddos an existing web-site.If it's braking some existing licenes I'll delete it (just let me know).

## Installation

Download the repository using

```bash
git clone https://github.com/arsu4ka/gidonileEU.git
```

or download it directly from github.

Then install all required packages:

```bash
pip install requirements.txt
```

## Usage

Basically, main func for account creation located at

```bash
./gidonline/gidonline.py
```

file.

**Example of code:**

```python
from gidonline.gidonline import register

# returns dict with account credentials if it was created successfully and 'None' if not
register(email='test.email@email.test')
```

## List of parameters for register() func

* __*email*__ - ***Required***. Email for which account will be created.

* __*username*__ - **Optional**. Username for account. Should be unique on the site. If it isn't script will automatically change it to a random one.

* __*password*__ - **Optional**. Password for account. Shouldn't be shorter than 6 symbols. If it is script will automatically change it to a random one.


## Note

Don't forget to paste your ***2capthca.com API key*** in

```bash
./gidonline/config.py
```

file. Otherwise, it won't work.