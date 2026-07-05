import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, ".")

from run import app as application

if __name__ == "__main__":
    app = application