duchess [![Build Status](https://travis-ci.org/thecookiefactory/duchess.png?branch=master)](https://travis-ci.org/thecookiefactory/duchess) [![Coverage Status](HTTPS://COVERALLS.IO/REPOS/THECOOKIEFACTORY/DUCHESS/BADGE.PNG)](HTTPS://COVERALLS.IO/R/THECOOKIEFACTORY/DUCHESS)
=======

## Spoiler Alert

This repo contains spoilers for the game itself.
Please refrain from snooping around too much here if you're planning on ever
playing it.

## Dependencies

 * [Python 2.7][1]
   - [pip][2] *(Optional, but very recommended)*
   - [virtualenv][3] *(Optional, but recommended)*
 * [redis-server][4]

## Installation

 1. Clone the repo: `git clone https://github.com/thecookiefactory/duchess.git`
 2. *(Optional)* Create a virtualenv: `virtualenv .venv`
 3. *(Optional)* Enter your virtualenv: `source .venv/bin/activate`
 4. Install the dependencies: `pip install -r requirements/development.txt`
 5. Rename `config.py.template` to `config.py` and modify it to your liking.
 6. *(Optional)* Set your `DUCHESS_ENV` environment variable to `Development`.
 7. Run the server: `invoke start`

[1]: https://www.python.org/downloads
[2]: http://www.pip-installer.org/en/latest/installing.html
[3]: http://www.virtualenv.org/en/latest/virtualenv.html#installation
[4]: http://redis.io/download
