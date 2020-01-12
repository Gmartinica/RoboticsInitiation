from pyduino import *
from flask import Flask, request, render_template
import time

app = Flask(__name__)

# initialize connection to Arduino
# if serial port is not '/dev/cu.usbmodem145201/'
# then
# a = Arduino(serial_port='yourporthere')
a = Arduino()
time.sleep(2)
#git test

# state pins
LED_PIN = 13

# led pin as output
a.set_pin_mode(LED_PIN,'O')

# Define methods to get information
@app.route('/', methods = ['POST', 'GET'])
def requests():
    # variables for template page
    author = "Gabriel"
    ledmode = ''

    if request.method == 'POST':
        # if we press the turn on button
        if request.form['button'] == 'Turn On':
            print ('TURN ON')
            a.digital_write(LED_PIN, 1)
            ledmode = "ON"

        # if we press the turn off button
        elif request.form['button'] == 'Turn Off':
            print ('TURN OFF')
            a.digital_write(LED_PIN, 0)
            ledmode = "OFF"

        else:
            pass

    # default page
    return render_template('index.html', author=author, value=ledmode)


if __name__ == "__main__":

    app.run(host='localhost', debug=False)
