import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    nod = request.form['nod']

    # Run the shell script using sudo and pass in the user inputs as arguments
    result = subprocess.run(['sudo', '/path/to/shell/script.sh', username, password, nod])

    if result.returncode == 1:
        # Script returned success, show success message
        return render_template('success.html')
    else:
        # Script returned an error, show error message
        return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True)
