from flask import Flask, render_template
import openbook

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html', leftpage=openbook.read('C:\\Users\\User\\Desktop\\Crazy Rich Asians.epub'),rightpage=openbook.read2('C:\\Users\\User\\Desktop\\Crazy Rich Asians.epub'))

if __name__ == "__main__":
    app.run()

