from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)


@app.route("/")
def main():
    return render_template ('sprC.html')

@app.route("/dodaj")
def dodaj():
    return render_template ('ladowanie.html')


@app.route("/kont")
def kont():
    return render_template ('kontakt.html')


uploads = os.path.join(app.instance_path, 'uploads')
os.makedirs(uploads)


@app.route('/zapis', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(os.path.join(uploads, secure_filename(f.filename)))
      return 'file uploaded successfully'



if __name__== "__main__":
    app.run()