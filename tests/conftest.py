import os
import sys


try:
    import denis

except ImportError:
    filepath = os.path.dirname(__file__)
    rootpath = os.path.abspath(os.path.join(filepath, '..'))
    sys.path.insert(0, os.path.abspath(rootpath))
    import denis
