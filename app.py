import gd
from flask import Flask

app = Flask(__name__)

try:
    mem = gd.memory.get_memory()
except:
    print("Please open GD!")
    exit(1)

@app.route('/write/<pointer>/<byte>')
def on(pointer, byte):
    a = bytes([int(a, 16) for a in pointer.split(",")])
    b = int(byte, 16)
    mem.write_bytes(gd.memory.Buffer(a), b)
    return "ok"