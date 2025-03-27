from flask import Flask
from flask import Request



app = Flask(__name__)


@app.route("/")

def index():
    rooms = Request.args.get("rooms","")
    return (
        """<form action="" method="get">
                <input type="text" name="rooms">
                <input type="submit" value="Generate">
              </form>"""
        + rooms
    ) 
    

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
