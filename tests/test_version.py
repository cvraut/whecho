import subprocess
import toml
import os

def test_version_consistency():
    # get the directory of the test_version.py file
    test_version_path = os.path.dirname(os.path.realpath(__file__))
    # Read the version from pyproject.toml
    with open(f"{test_version_path}/../pyproject.toml", "r") as f:
        pyproject_data = toml.load(f)
    expected_version = pyproject_data["tool"]["poetry"]["version"]

    # Run the whecho --version command
    output = subprocess.check_output(["whecho", "--version"], universal_newlines=True)

    # Extract the version from the output
    actual_version = output.strip()

    # Compare the versions
    assert actual_version == expected_version, "Version mismatch between whecho command and pyproject.toml"