# Development Notes

Thank you for your interest in whecho's source code. New features and contributions are always welcome 🙂

Raise an issue or submit a pull request if you have any new ideas!

**Do not open PRs to `main`**, GitHub Actions stores the webhook URLs in repository secrets. If it is your first time contributing please create a new branch and **create the PR to `dev`**. The core maintainers will then evaluate the contribution and run it in GitHub Actions to verify no regression in functionality.

## building the project
- clone the repo & go to the directory of the `pyproject.toml` file
- clone the environment using the supplied environment.yml file
  - run `conda env create --file environment.yml`
- activate the environment `conda activate whecho`
- run `poetry build`
- install with `python -I -m pip install --force-reinstall --no-deps dist/whecho-0.0.0.tar.gz`

## running the unit tests
- make sure you have the environment installed
- navigate to the tests directory
- run `pytest`
- NOTE: to pass all the tests you must have the following environment variables pointing to a valid webhook URL
  - `TEST_URL` pointing to a discord webhook
  - `TEST_SLACK_URL` pointing to a slack webhook
  - `TEST_WEBEX_URL` pointing to a webex webhook
  - `TEST_DISCORD_URL` pointing to a discord webhook (ideally using the discordapp.com endpoint instead)
  - tox makes use of these environment variables during the automated testing