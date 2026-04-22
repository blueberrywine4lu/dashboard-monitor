from flask import Flask, render_template
import psutil
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disco = psutil.disk_usage("/").percent
    ora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", cpu=cpu, ram=ram, disco=disco, ora=ora)

if __name__== "__main__":
    app.run(debug=True)
