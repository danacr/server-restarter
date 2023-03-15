import os
import time
import subprocess
from flask import Flask, render_template, request

app = Flask(__name__)

def restart():
    dev = os.open("/dev/hidraw0", os.O_RDWR)
    os.write(dev,b'\x00'b'\x01')
    time.sleep(1)
    os.write(dev,'\x00'b'\xf1')

@app.route("/", methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        match request.form.get('action'):
            case "Restart":
                subprocess.run([busylight_path, 'on', 'green'],
                               stdout=subprocess.PIPE)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
