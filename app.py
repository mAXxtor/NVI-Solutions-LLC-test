import os
from flask import Flask, redirect, request, render_template
from torchvision.transforms.functional import get_image_size
from torchvision.io import read_image
from torchvision.models import ResNet50_Weights, resnet50
from werkzeug.utils import secure_filename
DEBUG = True
# папка для сохранения загруженных файлов
UPLOAD_FOLDER = './test_img/'
# расширения файлов, которые разрешено загружать
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config.from_object(__name__)
app.secret_key = 'the random string'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000


@app.route('/', methods=['GET', 'POST'])
def index():
    pic_data = {}
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],
                               secure_filename(file.filename)))
        img = read_image(f'test_img/{file.filename}')
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
        score = prediction[class_id].item()
        category_name = weights.meta["categories"][class_id]
        print(f"{category_name}: {100 * score:.1f}%")
        print(f"{width}, {height}")
        pic_data = dict(category=category_name, width=width, height=height)
        # return redirect(request.url)
    return render_template('index.html', **pic_data)