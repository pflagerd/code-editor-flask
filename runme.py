#!/usr/bin/env python3
import os
import sys
import subprocess
import time
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


def main(args, debug=False):
    if sys.version_info < (3, 12, 3):
        print("Current version " + sys.version.split()[0] + " is too old.  Must be 3.12.3 or later.", file=sys.stderr)
        sys.exit(1)

    if debug:
        print(__file__)
        print(os.path.abspath(__file__))

    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)
    if debug:
        print(script_directory)  # Does script_directory contain a trailing '/'?  No.
    if not os.path.exists(script_directory + "/.venv"):  # if
        spawn_result = spawn("python3 -m venv .venv")
        if spawn_result.returncode:
            raise RuntimeError("python3 -m venv .venv failed: " + spawn_result.stderr)
        if debug:
            print(spawn_result)

    stdout = spawn(".venv/bin/pip freeze").stdout
    if debug:
        print(f'stdout == {stdout}')

    if not stdout:
        spawn_result = spawn(".venv/bin/pip install -r requirements.txt")
        if debug:
            print(spawn_result)

    spawn("open http://localhost:5000")
    # time.sleep(5)  # browser appears even to wait long enough if I introduce an artifical pause.
    os.execvp(".venv/bin/python3", [".venv/bin/python3", "./code-editor-flask.py"])


if __name__ == "__main__":
    sys.exit(main(sys.argv))

