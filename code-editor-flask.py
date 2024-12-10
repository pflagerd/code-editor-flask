from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import sys
from io import StringIO

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run', methods=['POST'])
def run_code():
    code = request.json['code']
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    
    try:
        r, w = os.pipe()
        stdout_fd = os.dup(1)
        os.dup2(w, 1)
        exec(code)
        os.dup2(stdout_fd, 1)
        os.close(w)
        os.close(stdout_fd)
        sys.stdout = old_stdout
        with os.fdopen(r) as pipe:
            output = pipe.read()
        print("HERE", file=sys.stderr)
        print(output, file=sys.stderr)
        os.close(r)
        return jsonify({'output': output})
    except Exception as e:
        sys.stdout = old_stdout
        return jsonify({'output': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
