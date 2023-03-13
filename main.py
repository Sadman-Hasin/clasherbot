#from bot import HappyClasher
from flask import Flask

app = Flask(__name__)
@app.route("/main")
def index():
    return "<p>Server Running...</p>"

#client = HappyClasher(os.getenv("EMAIL"), os.getenv("PASSWORD"))
#client.listen()
