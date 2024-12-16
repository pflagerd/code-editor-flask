from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import sys
import subprocess
import tempfile

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json['code']

    with tempfile.NamedTemporaryFile() as temp:
        temp.write(code.encode('utf-8'))
        temp.flush()
    
        try:
            process = subprocess.Popen(
                ["python3", "-u", temp.name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )

            stdout, stderr = process.communicate()

            print(stdout.decode('utf-8'))
            print(stderr.decode('utf-8'))
            print(process.returncode)

            return jsonify({'output': stdout.decode('utf-8')})
        except Exception as e:
            return jsonify({'output': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
