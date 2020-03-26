from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # return "<h1> Hello World in Flask</h1>"
    return render_template('basic_view.html')

@app.route('/info')
def info():
    return "<h1> This is much easier than Django</h1>"


@app.route('/user_name/<name>')
def user_name(name):
    return "<h3>Username is {}. Uppercased</h3>".format(name.upper())


@app.route('/user_name_latin/<name>')
def user_name_latin(name):
    lat_name = ''
    if name[-1] == 'y':
        lat_name = name[:-1] + 'iful'
    else:
        lat_name = name + 'y'
    return "<h1>Hi {}! Your user latin name  is {} </h1>".format(name, lat_name)


@app.route('/some_site/<name>')
def some_site(name):
    my_sentence = 'some sentence in order to practice'
    my_dict = {'some_name': 'Dzanusz'}
    return render_template('some_site.html', name=name, my_sentence=my_sentence, my_dict=my_dict)


if __name__ == '__main__':
    app.run(debug=True)
