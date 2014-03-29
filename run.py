#!/usr/bin/env python
from duchess import create_app

if __name__ == '__main__':
    duchess = create_app()
    duchess.run(host='0.0.0.0')
