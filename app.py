from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_square', methods=['POST'])
def generate_square():
    n = int(request.form.get('n'))
    return render_template('square.html', n=n)

if __name__ == '__main__':
    app.run(debug=True)
