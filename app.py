import gd
from flask import Flask

app = Flask(__name__)

try:
    gd = gd.memory.get_memory()
except:
    print("Please open GD!")
    exit(1)

@app.route('/on')
def on():
    gd.enable_noclip()
    return "Turned on"

@app.route('/off')
def off():
    gd.disable_noclip()
    return "Turned off"