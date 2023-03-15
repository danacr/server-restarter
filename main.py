import os
import time
from flask import Flask, render_template, request

app = Flask(__name__)

def restart():
    os.system("echo -n -e '\x00\xf1' >/dev/hidraw0")
    time.sleep(1)
    os.system("echo -n -e '\x00\x01' >/dev/hidraw0")
    
@app.route("/", methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        restart()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
