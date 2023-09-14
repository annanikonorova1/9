from flask import Flask, request, render_template, session
import secrets
secrets.token_hex()

app = Flask(__name__)

app.secret_key = 'the random string'
@app.route('/')
def index():
    return render_template('hi.html')


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        return f'Hello,'

    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
