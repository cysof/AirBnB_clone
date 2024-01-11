#!/usr/bin/python3

"""
Importing FileStorage (modules and package)
and setting that equal to storage and calling reload
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
