# selenium-pytest-Gsearch

#### Tests
I've developed a small testing application under `selenium_tests/`. It uses **Pytest** as testing framework.
The tests are developed implementing a page object pattern.
They are run against the web https://www.google.com/.

## Running the tests locally 
Stepts for running the tests locally:

1) Make sure you are on the `selenium_tests/` root.
2) Set a Python virtual environment. Activate it.
3) Install all the dependencies defined on `selenium_tests/requirements.txt` (`pip install -r requirements.txt`).
4) Finally, simply run: `pytest`

