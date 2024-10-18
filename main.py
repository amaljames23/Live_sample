from flask import *
from public import public
from admin import admin

app=Flask(__name__,template_folder="docs")

app.secret_key="abcdet"

app.register_blueprint(public)
app.register_blueprint(admin)



app.run(debug=True)




