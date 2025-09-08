from flask import Flask, render_template, jsonify
import subprocess
import signal
import os

app = Flask(__name__)

process = None  # global process handler

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/start")
def start():
    global process
    if process is None or process.poll() is not None:  # not running
        process = subprocess.Popen(["python", "src/Virtual_Mouse.py"])
        return jsonify({"status": "Virtual Mouse started"})
    else:
        return jsonify({"status": "Already running"})

@app.route("/stop")
def stop():
    global process
    if process and process.poll() is None:  # still running
        if os.name == "nt":  # Windows
            process.send_signal(signal.CTRL_BREAK_EVENT)
        else:  # Linux/macOS
            process.terminate()
        process = None
        return jsonify({"status": "Virtual Mouse stopped"})
    else:
        return jsonify({"status": "Not running"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
