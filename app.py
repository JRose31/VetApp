from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/test')
def test():  # put application's code here
    return render_template('test.html', name='Test')


@app.route('/image-upload', methods=['GET', 'POST'])
def img_upload():
    data = {"Pet types": ['Dog', 'Cat', 'Ferret', 'Snake', 'Bird']}
    return render_template('image_upload.html', name='Uploader', data=data)


@app.route('/image-processing', methods=['POST'])
def img_processing():
    if request.method == 'POST':
        pet_name = request.form['pet_name']
        pet_type = request.form.get('pet_type')
        img_obj = request.files.get('image_file')
        img_file = img_obj.filename

        pet_data = {
            'name': pet_name,
            'type': pet_type,
            'filename': img_file
        }

        print(f"All values passed: {pet_name, pet_type, img_file}")

    return render_template('image_processing.html', name='Processor', data=pet_data)


if __name__ == '__main__':
    app.run()
