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
    
@app.route("/rooms", methods=['GET','POST'])
def generateDungeon():
    

    if request.method == 'POST':
      rooms = request.args.get('rooms')
      if rooms.strip() == '':
        return "<h1>Invalid Number, please enter number</h1>"
      
      print("Generate Dungeon Here")
      return render_template('result.html')

    return render_template('rooms.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
