from flask import Flask
from flask import request, render_template
from markupsafe import escape

app = Flask(__name__)

import dungeonbuilder.views