# How to Contribute

`pybluedot` uses Travis CI for Continuous Integration. This runs both unit tests as well as linting checks to ensure code quality.

It's very easy to run these checks for yourself, without even having to push any code or open a PR. All you need to do is install virtualenv and tox:

    pip install virtualenv tox

Then, you can run these three commands from inside this repository (they are the same commands that Travis will run):

- `tox -epep8`: This runs PEP8 and other style checks on your code
- `tox -epy27`: This runs unit tests
- `tox -ecover`: This runs coverage testing

If those three commands run without error, then you're ready to open a Pull Request. If not, please address those issues (of course, feel free to reach out on Slack for any assistance with this).

# Tips

## Cryptography Failure on OSX

If you are developing on OSX and are seeing this error when running Tox:

    fatal error: too many errors emitted, stopping now [-ferror-limit=]

    20 errors generated.

    error: command 'cc' failed with exit status 1

Make sure you're running the latest version of virtualenv and pip, then destroy and re-run Tox, and you should be good.