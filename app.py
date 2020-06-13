import json
from tempfile import NamedTemporaryFile

from flask import Flask, render_template, request

from grobid.grobid_client_generic import grobid_client_generic

app = Flask(__name__)


@app.route('/version')
def version():
    return '0.0.1'


@app.route('/')
def root():
    return render_template('index.html')


# TODO: Add consolidation
@app.route('/citation/process', methods=['POST'])
def process_citations():
    file = request.files['input']
    grobid = grobid_client_generic(config_path="./config.json")
    tf = NamedTemporaryFile()
    tf.write(file.read())
    return grobid.process_pdf(tf.name, 'processCitations', headers={'Accept': 'application/x-bibtex'})


@app.route('/references/process', methods=['POST'])
def process_references():
    file = request.files['input']
    grobid = grobid_client_generic(config_path="./config.json")
    tf = NamedTemporaryFile()
    tf.write(file.read())
    result = grobid.process_pdf(tf.name, 'processReferences', headers={'Accept': 'application/x-bibtex'})

    return result


@app.route('/header/process', methods=['POST'])
def process_header():
    file = request.files['input']
    grobid = grobid_client_generic(config_path="./config.json")
    tf = NamedTemporaryFile()
    tf.write(file.read())
    return grobid.process_pdf(tf.name, 'processHeader', headers={'Accept': 'application/x-bibtex'})


@app.route('/config', methods=['GET'])
def get_config(config_json='./config.json'):
    config = json.loads(open(config_json).read())
    return config


if __name__ == '__main__':
    app.run(host='0.0.0.0')
