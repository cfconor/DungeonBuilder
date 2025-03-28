from flask import Flask
from flask import request, escape, render_template

app = Flask(__name__)

@app.route("/")
def index():
  #rooms = str(escape(request.args.get("rooms","")))
  return (
      """<h1>Index</h1>"""
  ) 
    
@app.route("/rooms", methods=['GET','POST'])
def generateDungeon():
  if request.method == 'POST':
    rooms = request.form.get('rooms')
    #print("Rooms: " + rooms)
    if rooms.strip() == '':
      return "<h1>Invalid Number, please enter number</h1>"
    
    print("Generate Dungeon Here")
    return render_template('result.html', rooms=rooms)

  return render_template('rooms.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
