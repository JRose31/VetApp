from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/test')
def test():  # put application's code here
    return render_template('test.html', name='Test')


@app.route('/image-upload', methods=('GET', 'POST'))
def img_upload():
    if request.method == 'POST':
        petname = request.form['petname']
        pettype = request.form.get('pettype')
        img_obj = request.files.get('imagefile')
        img_file = img_obj.filename

        print(f"All values passed: {petname, pettype, img_file}")

    return render_template('image_upload.html', name='Uploader')


if __name__ == '__main__':
    app.run()
