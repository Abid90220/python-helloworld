import io
import os.path
from setuptools import setup

VERSION_PATH = os.path.join(os.path.dirname(__file__), "helloworld/VERSION.txt")
with open(VERSION_PATH, encoding="utf-8") as f:
    version = f.read().strip()

setup(
    version=version,
)
