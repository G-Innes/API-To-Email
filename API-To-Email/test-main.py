import pytest
import sys
from main import arguments, check_email, EmailNotValidError


# sys.argv to simulate valid arguments
# call function and assign the returned values to recipient and api
# assert that recipient is equal to 'recipient@gmail.com' and api is equal to 'meme'
def test_valid_arguments():
    sys.argv = ["script.py", "recipient@gmail.com", "meme"]
    recipient, api = arguments()

    assert recipient == "recipient@gmail.com"
    assert api == "meme"

# sys.argv to simulate invalid arguments
# use of context manager to check if SystemExit exception is raised when calling arguments()
# check the printed output using capsys to capture the output
# assert that the output is equal to the expected message
def test_invalid_arguments(capsys):
    sys.argv = ['test.py']

    with pytest.raises(SystemExit):
        arguments()

    output = capsys.readouterr().out.strip()
    assert output == 'Invalid Number Of Arguments!⛔️'

# assign a valid email to recipietn variable
# call check_email() with recipient & assign returned value to result
# assert result is equal to the expected message 'Check your inbox!'
def test_valid_email():
    recipient = 'code@gmail.com'

    result = check_email(recipient)

    assert result == 'Valid Email!✅'

# assign recipient variable to invalid email address
# call check_email function with invalid recipient
# if exception is not raised, the test fails and raises an assertion error with error message
def test_invalid_email():
    recipient = 'email'

    try:
        check_email(recipient)
        assert False, 'Expected EmailNotValidError to be raised.'
    except EmailNotValidError:
        pass