import os
import sys

import pandas as pd
from flask import Flask
from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from stadistic.converter import conversion

sys.path.append('/path/to/py_files_and_packages')
from os.path import join, dirname, realpath
app = Flask(__name__)

# Flask object initialization
# app flask object has to be created before importing views below
# because it calls "import app from app"
stadistic = join(dirname(realpath(__file__)), 'stadistic')
ALLOWED_EXTENSIONS = set(['xlsx'])
app.config['stadistic'] = stadistic


@app.route('/')
def hello_world():
    return render_template('index.html')


# File extension checking
def allowed_filename(filename):
    print filename
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['GET', 'POST'])
def up():
    print "hola2"
    if request.method == 'POST':
        submitted_file = request.files['file']
        # print allowed_filename(submitted_file.filename)
        if submitted_file and allowed_filename(submitted_file.filename):
            filename = secure_filename(submitted_file.filename)
            submitted_file.save(os.path.join(app.config['stadistic'], filename))
            print "jocop"
            return redirect(url_for('uploaded_file'))
    return render_template('upload.html')


@app.route('/uploaded_file', methods=['GET', 'POST'])
def uploaded_file():
    conversion()
   # n =  os.path.join(app.config['stadistic'], 'Base de datos1 - proyecto No. 1.xlsx')
   # print os.path.join(app.config['stadistic'], 'csvfile.csv')
    data = pd.read_csv(os.path.join(app.config['stadistic'], 'csvfile.csv'), usecols=[0, 1])
    df2 = data.set_index("Fecha")
    df3 = data.set_index("Monto mensual")
   # print data
    females = pd.DataFrame(data["Fecha"], index=data["Monto mensual"])
    return render_template('view.html', tables=[data.to_html(classes='data')],
                           titles=['Tablas predictoras'])


if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug=True)
