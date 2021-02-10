from flask import Flask, render_template
from gpiozero import LED, Buzzer, TonalBuzzer
from gpiozero.tones import Tone
from time import sleep

led=LED(17)

app = Flask(__name__)

@app.route('/json')
def json():
    return render_template('json.html')

@app.route('/transmission')
def transmission_start_end():
    tbuzzer = TonalBuzzer(22)
    led.blink(0.025,0.025)
    tbuzzer.play(Tone(frequency=500))
    sleep(3)
    led.off()
    tbuzzer.stop()
    tbuzzer.close()
    return render_template('json.html')

@app.route('/dot')
def dot():
    buzzer = Buzzer(22)
    led.on()
    buzzer.on()
    sleep(0.1)
    led.off()
    buzzer.off()
    buzzer.close()
    return render_template('json.html')

@app.route('/dash')
def dash():
    buzzer = Buzzer(22)
    led.on()
    buzzer.on()
    sleep(0.5)
    led.off()
    buzzer.off()
    buzzer.close()
    return render_template('json.html')

if __name__ == "__main__":
    print("Morse Code is On")
    app.run(host='0.0.0.0', port=8000, debug=False)
