import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import os

# --- 1. AYARLAR ---
VERI_YOLU = 'data'  # Senin oluşturduğun resim klasörü
HEDEF_BOYUT = (150, 150) # Resimleri bu boyuta eşitleyeceğiz
BATCH_SIZE = 32 # Her seferinde kaç resme bakarak öğrensin

# --- 2. VERİYİ YÜKLEME ---
# Resimleri sayısal verilere çeviriyoruz (0-255 arası renkleri 0-1 arasına sıkıştırıyoruz)
train_datagen = ImageDataGenerator(
    rescale=1./255,       
    validation_split=0.2  # Verinin %20'sini test (doğrulama) için ayırıyoruz
)

print("Eğitim verileri yükleniyor...")
train_generator = train_datagen.flow_from_directory(
    VERI_YOLU,
    target_size=HEDEF_BOYUT,
    batch_size=BATCH_SIZE,
    class_mode='categorical', # 4 farklı sınıfımız olduğu için 'categorical'
    subset='training'
)

print("Test verileri yükleniyor...")
validation_generator = train_datagen.flow_from_directory(
    VERI_YOLU,
    target_size=HEDEF_BOYUT,
    batch_size=BATCH_SIZE,
    class_mode='categorical',
    subset='validation'
)

# --- 3. MODELİ KURMA (Yapay Zeka Mimarisi) ---
model = Sequential([
    # 1. Katman: Resimdeki özellikleri (kenar, köşe) yakalar
    Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    MaxPooling2D(2, 2),

    # 2. Katman: Daha detaylı özellikleri yakalar
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    # 3. Katman: Karmaşık desenleri öğrenir
    Conv2D(128, (3, 3), activation='relu'),
    MaxPooling2D(2, 2),

    # Düzleştirme ve Karar Verme Katmanı
    Flatten(),
    Dense(512, activation='relu'),
    Dropout(0.5), # Aşırı ezberlemeyi (overfitting) engeller
    Dense(4, activation='softmax') # ÇIKIŞ: 4 sınıfımız var (glioma, meningioma, no, pituitary)
])

# --- 4. DERLEME ---
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# --- 5. EĞİTİMİ BAŞLATMA ---
print("Eğitim başlıyor... (Bu işlem bilgisayar hızına göre 5-10 dk sürebilir)")
history = model.fit(
    train_generator,
    epochs=10, # Veri setinin üzerinden 10 kere geçecek
    validation_data=validation_generator
)

# --- 6. MODELİ KAYDETME ---
if not os.path.exists('model'):
    os.makedirs('model')

# DEĞİŞTİRDİĞİMİZ KISIM BURASI:
model.save('model/beyin_tumoru_modeli.keras') 
print("Tebrikler Kerem! Model eğitildi ve 'model' klasörüne kaydedildi.")