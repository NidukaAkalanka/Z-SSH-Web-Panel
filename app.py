import subprocess
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the user inputs from the form
        username = request.form['username']
        password = request.form['password']
        exd = request.form['exd']
        
        # Construct the command to execute the shell script with sudo
        command = f"sudo /path/to/your/script.sh {username} {password} {number}"
        
        # Execute the command and get the return code
        return_code = subprocess.call(command, shell=True)
        
        # Return a success message if the script returns code 0, else return an error message
        if return_code == 0:
            message = "Script executed successfully!"
        else:
            message = "Error executing script!"
        
        # Render the HTML template with the message
        return render_template('index.html', message=message)
    else:
        # Render the HTML template without a message
        return render_template('index.html')
