#!/usr/bin/env python
import os
import sys
import subprocess
from types import SimpleNamespace


def spawn(command_line):
    process = subprocess.run(
        command_line.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    return SimpleNamespace(
        stdout=process.stdout.decode('utf-8'),
        stderr=process.stderr.decode('utf-8'),
        returncode=process.returncode
    )


def main(args):
    if sys.version_info < (3, 12, 3):
        print("Current version " + sys.version.split()[0] + " is too old.  Must be 3.12.3 or later.", file=sys.stderr)
        sys.exit(1)

    # print(__file__)
    # print(os.path.abspath(__file__))

    script_directory = os.path.dirname(os.path.abspath(__file__))
    # print(script_directory)  # Does script_directory contain a trailing '/'?  No.
    if not os.path.exists(script_directory + "/.venv"):  # if
        os.chdir(script_directory)
        print(str(spawn("python -m venv .venv")))

    os.chdir(script_directory)
    stdout = spawn(".venv/bin/pip freeze").stdout
    # print(f'stdout == {stdout}')

    if not stdout:
        os.chdir(script_directory)
        print(spawn(".venv/bin/pip freeze"))

        spawn(".venv/bin/python ./code-editor-flask.py")

    os.system("open http://localhost:5000")
    os.execvp(".venv/bin/python", [".venv/bin/python", "./code-editor-flask.py"])


if __name__ == "__main__":
    sys.exit(main(sys.argv))

