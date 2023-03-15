import os
import time
from flask import Flask, render_template, request

app = Flask(__name__)

def restart():
    dev = os.open("/dev/hidraw0", os.O_RDWR)
    os.write(dev,"\x00\x01")
    time.sleep(1)
    os.write(dev, "\x00\xf1")

@app.route("/", methods=['GET', 'POST'])
def control():
    if request.method == 'POST':
        match request.form.get('action'):
            case "Restart":
                restart()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
