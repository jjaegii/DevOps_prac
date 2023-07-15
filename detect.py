from ultralytics import YOLO
from PIL import Image
import os, io
from flask import Flask, render_template, request, url_for

IMAGE_DIR = os.environ.get('IMAGE_DIR')
if IMAGE_DIR is None:
    IMAGE_DIR = "static/imgs"
else:
    IMAGE_DIR = os.path.join("static", IMAGE_DIR)

if not os.path.exists("static"):
    os.makedirs("static")

if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

def load_model():
    model = YOLO("model/yolov8n.pt")
    return model

app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.files['file'].filename == '':
        return render_template('error.html')
    # save image to disk
    f = request.files['file']
    f.save(os.path.join(IMAGE_DIR, f.filename))
    f_name = os.path.join(IMAGE_DIR, f.filename)
    
    preds, results = run_model(f_name, model)
    if preds == -1 and img_url == -1:
        return render_template('error.html')

    # get predicted image path
    pred_img_path = os.path.join(results[0].save_dir.replace('static/', ''), f_name.split('/')[-1])
    img_url = url_for('static', filename=pred_img_path)

    return render_template('predict.html', results=preds, img_url=img_url)

def run_model(f_name, model):
    preds = []
    try:
        img = Image.open(f_name)
        results = model.predict(source=img, save=True, project=IMAGE_DIR, name="predict")  # save plotted images
        
        # get predicted class names
        names = model.names
        for r in results:
            for c in r.boxes.cls:
                preds.append(names[int(c)])
        
    except Exception as e:
        print(e)
        return -1, -1

    return preds, results


if __name__ == "__main__":
    model = load_model()
    app.run(host='0.0.0.0', port=5000, debug=True)