import subprocess
import time
from flask import Flask, render_template, request

app = Flask(__name__)

def restart():
    subprocess.run(['echo', '-n', '-e', '\x00\x01', '>', '/dev/hidraw0'],
                               stdout=subprocess.PIPE)
    time.sleep(1)
    subprocess.run(['echo', '-n', '-e', '\x00\xf1', '>', '/dev/hidraw0'],
                               stdout=subprocess.PIPE)
    
@app.route("/", methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        restart()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
