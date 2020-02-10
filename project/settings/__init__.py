"""
Call Appropriate Settings
"""
try:
    from .local import *
except:
    from .production import *

try:
    from .secret import *
except:
    pass
