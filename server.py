from flask import Flask, render_template, redirect

server = Flask(__name__)

@server.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    server.run(debug=True, port=4917)