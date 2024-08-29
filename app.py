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
        exec(code)
        sys.stdout = old_stdout
        return jsonify({'output': redirected_output.getvalue()})
    except Exception as e:
        sys.stdout = old_stdout
        return jsonify({'output': str(e)})

if __name__ == '__main__':
    app.run(debug=True)