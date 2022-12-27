# Login Manager with Flask for GUI and Web

[![Integration - Flask-PyWebView](https://github.com/igormcsouza/flask-pywebview/actions/workflows/ci.yml/badge.svg)](https://github.com/igormcsouza/flask-pywebview/actions/workflows/ci.yml)
[![Pre-Commit - Flask-PyWebView](https://github.com/igormcsouza/flask-pywebview/actions/workflows/pre-commit.yml/badge.svg)](https://github.com/igormcsouza/flask-pywebview/actions/workflows/pre-commit.yml)

Create a basic Login Manager that runs on the web and also as a GUI application in any platform.

## Docstring Code Style

I try to follow the code style from [google](https://google.github.io/styleguide/pyguide.html) but only for docstring until now, maybe in the future I'll take a look at the python code style and follow it too...

## How to Test

The project uses pytest and coverage to test the application and calculate how much of the code was covered on tests, to run them just execute the following line (be sure to install the test requirements first `pip install -r requirements.test.txt):

    pytest -vv --cov=project tests/ --cov-fail-under=100

I also added a code quality checker, which is the prospector, it runs the mypy with it to check type hints and ensure correcteness.

    prospector --profile prospector.yml --with-tool mypy package/

## Next Steps

- [x] Create Testes for all the scenarios and run it on CI
- [x] Add pre-commit hooks
- [ ] Deploy it on AWS?
- [ ] Improve readme by describing how to run GUI and Web.
- [ ] Add logging
