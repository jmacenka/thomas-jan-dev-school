from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)


def send_message_to_backend(to_numner: str, message: str, url: str = "http://localhost:8000/post"):
    msg_obj = {
        "to_numner": to_numner,
        "message": message,
    }
    response = requests.post(url, data=msg_obj)
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/send_sms', methods=['POST'])
def send_sms():
    to_number = request.form['to_number']
    message = request.form['message']

    response = send_message_to_backend(to_number, message)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=3000)
