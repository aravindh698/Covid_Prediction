import os
from flask import Flask
from app2 import app as application
if __name__  == '__main__':
   port = int(os.environ.get('PORT', 5000))
   application.run(host='0.0.0.0', port=port)
