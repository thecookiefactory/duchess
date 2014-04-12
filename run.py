#!/usr/bin/env python
from os import getenv

from duchess import create_app

if __name__ == '__main__':
    duchess = create_app()
    duchess.run(host='0.0.0.0', port=int(getenv('PORT', 5000)))
