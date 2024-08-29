![Online Editor](./image-editor.png)

# code-editor-flask
Code editor written in HTML and CSS using FLask

## Overview
Here's an overview of the components we'll need:

- Frontend: HTML, CSS, and JavaScript with Ace editor
- Backend: Flask server to handle code execution
- AJAX to communicate between frontend and backend

## Setup
Git clone current repo on your local
```bash
git clone https://github.com/KevinJudith/code-editor-flask.git
```
Move to code-editor-flask repository
`cd path/to/code-editor-flask`

Install gunicorn, which will help you to run a HTTP server locally
```bash
pip install unicorn
```
Launch a local server with gunicorn
```bash
gunicorn app:app
```
You should see something like:
```
[2024-08-29 15:59:51 +0800] [95086] [INFO] Starting gunicorn 23.0.0
[2024-08-29 15:59:51 +0800] [95086] [INFO] Listening at: http://127.0.0.1:8000 (95086)
[2024-08-29 15:59:51 +0800] [95086] [INFO] Using worker: sync
[2024-08-29 15:59:51 +0800] [95087] [INFO] Booting worker with pid: 95087
```

Alternatively, you can also setup a python virtual environment
```bash
python3 -m menv myenv
```

This app has been deployed to https://render.com/

To deploy properly the app, you need the following files to indicate Render PaaS how to deploy your app using Flask and gunicorn

- requirements.txt
flask
flask-cors
gunicorn
- runtime.txt
python-3.12
- Procfile
web: gunicorn app:app
