# conftest.py

import sys
import os


def pytest_configure(config):
    # Get the absolute path of the 'app' folder
    app_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../app'))

    # Add the 'app' folder to the Python path
    sys.path.append(app_path)
