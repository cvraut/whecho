# Development Notes

Thank you for your interest in whecho's source code. New features and contributions are always welcome 🙂

Raise an issue or submit a pull request if you have any new ideas!

## building the project
- clone the repo & go to the directory of the `pyproject.toml` file
- clone the environment using the supplied environment.yml file
  - run `conda env create --file environment.yml`
- run `poetry build`
- install with `python -I -m pip install --force-reinstall --no-deps dist/whecho-0.0.0.tar.gz`

## running the unit tests
- make sure you have the environment installed
- navigate to the tests directory
- run `pytest`