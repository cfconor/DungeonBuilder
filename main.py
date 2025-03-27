from flask import Flask
from flask import request, escape, render_template

app = Flask(__name__)

@app.route("/")
def index():
    rooms = str(escape(request.args.get("rooms","")))
    return (
        """<form actio  n="" method="get">
                <input type="text" name="rooms">
                <input type="submit" value="Generate">
              </form>"""
        + rooms
    ) 
    
@app.route("/rooms", methods=['GET'])
def generateDungeon():
    rooms = request.args.get('rooms')

    if rooms is None: #No number entered, show input form
        return render_template('rooms.html')
    elif rooms.strip() == '':
        return "<h1>Invalid Number, please enter number</h1>"
    try:
        print("Generate Dungeon Here")
        return render_template('result.html')
    except ValueError:
        return "<h1>Couldn't generate dungeon</h1>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
