# code-editor-flask
Code editor written in HTML and CSS using FLask

## Overview
Here's an overview of the components we'll need:

- Frontend: HTML, CSS, and JavaScript with Ace editor

- Backend: Flask to handle code execution

  

## Setup
You must have python3 and git.

| OS | git | python |
| -------- | -------- | -------- |
| kubuntu 24.04.1 LTS   | 2.43.0, 2.45.2   | Python 3.12.3   |
| macOS Sequoia 15.1.1   | 2.39.5 (Apple Git-154)   | Python 3.12.7   |

Git clone current repo to your local machine

​	`git clone https://github.com/pflagerd/code-editor-flask.git`

Move to code-editor-flask repository

​	`cd path/to/code-editor-flask`

Type

```commandline
./RUNME
```

In the shell from which you just executed `./RUNME` you should see something like:
```
 * Serving Flask app 'app'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 259-072-464
127.0.0.1 - - [25/Oct/2024 09:32:42] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [25/Oct/2024 09:32:42] "GET /static/styles.css HTTP/1.1" 200 -
127.0.0.1 - - [25/Oct/2024 09:32:42] "GET /static/atom.ico HTTP/1.1" 200 -
127.0.0.1 - - [25/Oct/2024 09:33:03] "POST /run HTTP/1.1" 200 -
```

In a new browser window or tab, you should see something like this:

![Online Editor](https://github.com/user-attachments/assets/b2646db1-d179-4a7a-9c33-c5920558a2a0)
