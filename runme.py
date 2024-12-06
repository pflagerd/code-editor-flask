#!/usr/bin/env python3
import os
import os.path
import subprocess
import sys
import time
from types import SimpleNamespace


def main(args, debug=False):
    supported_python_versions = [(3, 11, 2), (3, 12, 3), (3, 12, 8), (3, 13, 0)]
    if (sys.version_info.major, sys.version_info.minor, sys.version_info.micro) not in supported_python_versions:
        print("Current version " + sys.version.split()[0] + " not tested.  Must be one of " + version_info_tuple_to_str(supported_python_versions), file=sys.stderr)
        sys.exit(1)

    if debug:
        print(__file__)
        print(os.path.abspath(__file__))

    script_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_directory)
    if debug:
        print(script_directory)  # Does script_directory contain a trailing '/'?  No.

    stdout = spawn("./bin/pip3 freeze").stdout
    if debug:
        print(f'stdout == {stdout}')

    if not stdout:
        spawn_result = spawn("bin/pip3 install -r requirements.txt")
        if debug:
            print(spawn_result)


    if not spawn('which open').returncode:
        subprocess.Popen(["open", "http://127.0.0.1:5000"])
        #was: spawn("open http://127.0.0.1:5000")
    elif not spawn('which gio').returncode:
        subprocess.Popen(["gio", "open", "http://127.0.0.1:5000"])
    else:
        print('Neither open nor gio is available in your PATH, cannot launch default browser', file=sys.stderr)

    os.execvp("bin/python3", ["bin/python3", "./code-editor-flask.py"])

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

def version_info_tuple_to_str(version_info_tuple):
    s = ""
    for version_info in version_info_tuple:
        if s:
            s += ", "
            s += ", "
        s += str(version_info[0]) + "." + str(version_info[1]) + "." + str(version_info[2])
    return s


if __name__ == "__main__":
    sys.exit(main(sys.argv))

