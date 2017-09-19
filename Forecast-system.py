from flask import Flask, render_template
from flask import render_template, request, redirect, url_for
import os
import os
from flask import Flask
from werkzeug.utils import secure_filename
from os.path import join, dirname, realpath

app = Flask(__name__)

#Flask object initialization
#app flask object has to be created before importing views below
#because it calls "import app from app"
UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'UPLOAD_FOLDER')
ALLOWED_EXTENSIONS = set(['xlsx'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route('/')
def hello_world():
    return render_template('index.html')
#File extension checking
def allowed_filename(filename):
    print filename
    return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSIONS
@app.route('/upload', methods=['GET', 'POST'])
def up():
    if request.method == 'POST':
        submitted_file = request.files['file']
        print allowed_filename(submitted_file.filename)
        if submitted_file and allowed_filename(submitted_file.filename):
            filename = secure_filename(submitted_file.filename)
            submitted_file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print "jocop"
            return redirect(url_for('uploaded_file'))
    return render_template('upload.html')
@app.route('/uploaded_file', methods=['GET', 'POST'])
def uploaded_file():
    return render_template('readCSV.html')
if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
