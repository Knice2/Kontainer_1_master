from flask import Flask
app = Flask('_name_')

@app.route("/")
#Add Debug Configuration
def hello():
    return "Hello World"
    
if '_name_' == "_main_":
    app.run(host='0.0.0.0')
    