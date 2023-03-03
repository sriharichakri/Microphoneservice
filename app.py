from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['blob']
    file.save(os.path.join(os.getcwd(), file.filename))
    return 'File uploaded successfully'
@app.route('/getfiles', methods=['GET'])
def get_files():
    return 'File fetched successfully'
if __name__ == '__main__':
    app.run(debug=True)
