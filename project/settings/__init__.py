"""
Call Appropriate Settings
"""

try:
    from .local import *
except:
    from .production import *
