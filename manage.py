#!/usr/bin/env python
import os
import sys
import dotenv
from os.path import join, dirname

if __name__ == "__main__":
	dotenv_path = join(dirname(__file__), '.env')
	dotenv.load_dotenv(dotenv_path)

	os.environ.setdefault("DJANGO_SETTINGS_MODULE", "foodbank_api.settings")
	
	from django.core.management import execute_from_command_line

	execute_from_command_line(sys.argv)
