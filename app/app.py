from flask import Flask, render_template, request, redirect, url_for
import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from werkzeug.utils import secure_filename

# --- AYARLAR ---
app = Flask(__name__)

# Modelin ve dosyaların yolu
MODEL_PATH = 'model/beyin_tumoru_modeli.keras'
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Klasör yoksa oluştur (Hata almamak için)
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Modeli Yükle
print("Model yükleniyor, lütfen bekleyin...")
model = load_model(MODEL_PATH)
print("Model yüklendi!")

# Sınıf İsimleri (Alfabetik sıraya göre - Klasör isimlerinle aynı sırada olmalı)
# 0: glioma, 1: meningioma, 2: notumor, 3: pituitary
CLASS_NAMES = ['Glioma Tümörü', 'Meningioma Tümörü', 'Tümör Yok (Sağlıklı)', 'Hipofiz Tümörü']

def model_predict(img_path, model):
    # Resmi modele uygun hale getir (150x150 boyutuna küçült)
    img = image.load_img(img_path, target_size=(150, 150))
    
    # Resmi sayıya çevir (Array)
    x = image.img_to_array(img)
    x = x / 255.0  # Eğitimde yaptığımız gibi 0-1 arasına sıkıştır
    x = np.expand_dims(x, axis=0)  # Tek bir resim olduğu için boyut ekle

    # Tahmin yap
    preds = model.predict(x)
    pred_class = np.argmax(preds, axis=1) # En yüksek olasılıklı sınıfı bul
    return CLASS_NAMES[pred_class[0]]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Dosya yüklendi mi kontrol et
        f = request.files['file']
        if f.filename == '':
            return redirect(request.url)

        # Dosyayı kaydet
        filename = secure_filename(f.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)

        # Tahmin Yap
        sonuc = model_predict(file_path, model)

        return render_template('index.html', filename=filename, prediction=sonuc)
    
    return render_template('index.html')

# YENİ HALİ:
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)