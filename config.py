# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

envPath = join(dirname(__file__), '.env')
load_dotenv(envPath)

# Accessing variables.
TOKEN = os.getenv('DANEEL_TOKEN')
GITHUB_USER = os.getenv('DANEEL_GITHUB_USER')
GITHUB_PASS = os.getenv('DANEEL_GITHUB_PASS')
