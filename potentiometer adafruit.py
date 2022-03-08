#her tar den inn alle relativ informasjon sån den trenger for å funke
import time
from Adafruit_IO import Client, Feed, RequestError
import pyfirmata

#connecter seg opp til adafruit
run_count = 0
ADAFRUIT_IO_USERNAME = "Light082"
ADAFRUIT_IO_KEY = "aio_SsxY72QOhqZbcUQAhMm1j3YmqZaL"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#connecter seg til arduinoen
board = pyfirmata.Arduino('COM4')

it = pyfirmata.util.Iterator(board)
it.start()

#her er alle portans på arduinoen som blir brukt
digital_output = board.get_pin('d:9:o')
digital_output2 = board.get_pin('d:10:o')
digital_output3 = board.get_pin('d:11:o')
digital_output4 = board.get_pin('d:12:o')
analog_input = board.get_pin('a:0:i')

#alle feeds som blir brukt og lager dei om til ein variabel. 
try:
    lys2 = aio.feeds('lys2')
    lys3 = aio.feeds('lys3')
    lys4 = aio.feeds('lys4')
    digital = aio.feeds('digital')
    analog = aio.feeds('analog')
except RequestError:
    feed = Feed(name='digital')
    feed2 = Feed(name='analog')
    feed3 = Feed(name='lys2')
    feed4 = Feed(name='lys3')
    feed5 = Feed(name='lys4')
    digital = aio.create_feed(feed)
    analog = aio.create_feed(feed2)
    lys2 = aio.create_feed(feed3)
    lys3 = aio.create_feed(feed4)
    lys4 = aio.create_feed(feed5)
    
#her prøver arduinoen å komunisere med adafruit
while True:
    data = aio.receive(digital.key)
    data3 = aio.receive(lys2.key)
    data4 = aio.receive(lys3.key)
    data5 = aio.receive(lys4.key)
    data2 = aio.send(analog.key, analog_input.read())

    #her er alle statementsane som styrer allt
    if data.value == "ON":
        digital_output.write(True)
    if data3.value == "ON":
        digital_output2.write(True)
    if data4.value == "ON":
        digital_output3.write(True)
    if data5.value == "ON":
        digital_output4.write(True)
    if data.value == "OFF":
        digital_output2.write(False)
    if data3.value == "OFF":
        digital_output3.write(False)
    if data4.value == "OFF":
        digital_output4.write(False)
    if data5.value == "OFF":
        digital_output.write(False)
    time.sleep(3)
