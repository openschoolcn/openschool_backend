# -*- coding: utf-8 -*-
import os

apis = os.listdir(os.path.dirname(__file__))
apis.remove("__init__.py")
apis.remove("__pycache__")

for api in apis:
    exec(f"from .{api} import {api}")
