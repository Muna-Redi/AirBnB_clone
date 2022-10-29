#!/usr/bin/env python3
""" sets up storage instance of class FileStorage """

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
