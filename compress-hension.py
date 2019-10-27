from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    return render_template('results.html', video_id=text)


if __name__ == '__main__':
    app.run()