from flask import Flask, render_template
from flask import Flask, render_template
from gpiozero import LED
from time import sleep
from pynput.mouse import Listener

led=LED(17)
app = Flask(__name__)

@app.route('/json')
def json():
    return render_template('json.html')

@app.route('/dot')
def dot():
    led.on()
    sleep(0.1)
    led.off()
    return render_template('json.html')

@app.route('/dash')
def dash():
    led.on()
    sleep(0.5)
    led.off()
    return render_template('json.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
