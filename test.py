from flask import Flask , render_template,request,url_for

myapp = Flask(__name__)

@myapp.route('/')
def index():
    return render_template('index.html',title='home' )

if __name__ == '__main__':
    myapp.run(debug=True, port=1234)