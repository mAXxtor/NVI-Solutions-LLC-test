import os
from dotenv import load_dotenv
from flask import Flask, request, render_template
from torchvision.io import read_image, ImageReadMode
from torchvision.models import ResNet50_Weights, resnet50
from torchvision.transforms.functional import get_image_size
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = './test_img/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

load_dotenv()

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = os.getenv(
    'SECRET_KEY',
    default='zr!=t*+74yz_551vbo$mu05+#4kh$+wdfvhywwkoowxy+nql)c')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def index():
    pic_data = {}
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],
                      secure_filename(file.filename)))
        img = read_image(f'test_img/{file.filename}', mode=ImageReadMode.RGB)
        width, height = get_image_size(img)

        # Step 1: Initialize model with the best available weights
        weights = ResNet50_Weights.DEFAULT
        model = resnet50(weights=weights)
        model.eval()

        # Step 2: Initialize the inference transforms
        preprocess = weights.transforms(antialias=True)

        # Step 3: Apply inference preprocessing transforms
        batch = preprocess(img).unsqueeze(0)

        # Step 4: Use the model and print the predicted category
        prediction = model(batch).squeeze(0).softmax(0)
        class_id = prediction.argmax().item()
        category_name = weights.meta['categories'][class_id]

        pic_data = dict(category=category_name, width=width, height=height)
    return render_template('index.html', **pic_data)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
