#!/usr/bin/env python
import os
import sys
import subprocess

if sys.version_info < (3, 12, 3):
    print("Current version " + sys.version.split()[0] + " is too old.  Must be 3.12.3 or later.", file=sys.stderr)
    sys.exit(1)

#print(__file__)
#print(os.path.abspath(__file__))

script_directory = os.path.dirname(os.path.abspath(__file__))
#print(script_directory)  # Does script_directory contain a trailing '/'?  No.
if not os.path.exists(script_directory + "/.venv"):  # if
    # cd script_directory
    os.chdir(script_directory)
    # python -m venv .venv
    process = subprocess.run(
        "python -m venv .venv".split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    print(process.stdout.decode('utf-8'))
    print(process.stderr.decode('utf-8'))
    print(process.returncode)

os.chdir(script_directory)
# python -m venv .venv
process = subprocess.run(
    ".venv/bin/pip freeze".split(),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

print(process.stdout.decode('utf-8'))
print(process.stderr.decode('utf-8'))
print(process.returncode)

if not process.stdout.decode('utf-8'):
    os.chdir(script_directory)
    # python -m venv .venv
    process = subprocess.run(
        ".venv/bin/pip install -r ./requirements.txt".split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    print(process.stdout.decode('utf-8'))
    print(process.stderr.decode('utf-8'))
    print(process.returncode)

    os.chdir(script_directory)
    # python -m venv .venv
    process = subprocess.run(
        ".venv/bin/python ./code-editor-flask.py".split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    print(process.stdout.decode('utf-8'))
    print(process.stderr.decode('utf-8'))
    print(process.returncode)

os.system("open http://localhost:5000")
os.execvp(".venv/bin/python", [".venv/bin/python", "./code-editor-flask.py"])
