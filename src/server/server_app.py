import json
import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
        return (
            "<h1>Distant Reading Archive</h1><p>This site is a prototype "
            "API for distant reading of science fiction novels.</p>"
        )
@app.route('/api/zach', methods=['GET'])
def api_zach():
        return (
            "zach's info"
        )


@app.route('/login', methods=['POST'])
def login():
    user = request.payload
    print(user)
    return user


app.run()
