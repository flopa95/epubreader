from flask import Flask, render_template
import openbook

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', leftpage=openbook.read('C:\\Users\\jerry-chung\\Desktop\\EbookReader\\local_db\\Factfulness by Hans Rosling.epub'))

if __name__ == "__main__":
    app.run()