from flask import Flask, Response
from markupsafe import escape

app1 = Flask(__name__)

@app1.route('/')
def hello_world():
    try:
        with open("/server.txt", "r") as f:
            content = f.read()
            with open("/loremipsum.txt", "r") as lorem:
                content += "\n\n" + lorem.read()
            return Response(content, mimetype="text/plain")
    except:
        return "404! Could not read /server.txt file!"

@app1.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

if __name__ == '__main__':
    app1.run(debug=True, host='0.0.0.0')
