from flask import Flask, render_template
from gpiozero import LED
from gpiozero import Buzzer
from time import sleep

led=LED(17)
buzzer = Buzzer(22)
app = Flask(__name__)

@app.route('/json')
def json():
    return render_template('json.html')

@app.route('/transmission')
def transmission_start():
    led.on()
    buzzer.on()
    sleep(3)
    led.off()
    buzzer.off()
    return render_template('json.html')

@app.route('/dot')
def dot():
    led.on()
    buzzer.on()
    sleep(0.1)
    led.off()
    buzzer.off()
    return render_template('json.html')

@app.route('/dash')
def dash():
    led.on()
    buzzer.on()
    sleep(0.5)
    led.off()
    buzzer.off()
    return render_template('json.html')

if __name__ == "__main__":
    print("Morse Code is On")
    app.run(host='0.0.0.0', port=8000, debug=False)
