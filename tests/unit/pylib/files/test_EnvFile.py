import os
from unittest import mock
from pylib.files.EnvFile import EnvFile

def test_set_env_variables():
    # Create a mock file object
    mock_file = mock.Mock()
    mock_file.readlines.return_value = [
        "VAR1=value1\n",
        "VAR2=value2\n",
        "# Comment line\n",
        "VAR3=value3\n",
        "VAR4=value4\n",
        "VAR5=value5\n",
    ]

    # Create an instance of EnvFile with the mock file object
    env_file = EnvFile(filepath="test.env")
    env_file.readlines = mock.Mock(return_value=mock_file.readlines())

    # Call the set_env_variabes method
    count = env_file.set_env_variabes(bypass_errors=True)

    # Assert that the environment variables are set correctly
    assert count == 5
    assert os.environ["VAR1"] == "value1"
    assert os.environ["VAR2"] == "value2"
    assert os.environ["VAR3"] == "value3"
    assert os.environ["VAR4"] == "value4"
    assert os.environ["VAR5"] == "value5"