from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    first = request.form('first')
    second = request.form('second')
    return redirect(url_for('thx', first=first, second=second))


@app.route('/username', methods=['GET', 'POST'])
def user():
    if request.method == 'GET':
        return render_template('username.html')
    username = request.form('username')
    return redirect(url_for('pass_var', username=username))


@app.route('/pass_var', methods=['GET', 'POST'])
def pass_var():
    lower_letter = False
    upper_letter = False
    num_end = False
    username = request.form.get('username')
    lower_letter = any(c.islower() for c in username)
    upper_letter = any(c.isupper() for c in username)
    num_end = username[-1].isdigit()
    #TODO without any function
    # for i in username:
    #     if any(i.islower()) == True:
    #         lower_letter = True
    #     if any(i.isupper()):
    #         upper_letter = True
    #     if username[-1].isdigit():
    #         num_end = True
    username = lower_letter and upper_letter and num_end
    return render_template('pass_ver.html', user_name=username,
                           lower_letter=lower_letter,
                           upper_letter=upper_letter,
                           num_end=num_end)


@app.route('/thx', methods=['GET', 'POST'])
def thx():
    first = request.form.get('first')
    second = request.form.get('second')

    return render_template('thx.html', first=first, second=second)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True)