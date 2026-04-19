# 🧠 Beyin Tümörü Tespit Sistemi (Brain Tumor Detection)

Bu proje, MR (Manyetik Rezonans) görüntüleri üzerinden beyin tümörlerini yüksek doğrulukla tespit etmek amacıyla geliştirilmiş bir Derin Öğrenme (Deep Learning) web uygulamasıdır. Proje, sistem bağımlılıklarını ortadan kaldırmak ve her ortamda sorunsuz çalışabilmek için tamamen **Docker** altyapısı üzerine kurgulanmıştır.

## 🚀 Özellikler
- Derin öğrenme modeli ile medikal görüntü analizi.
- Kullanıcı dostu web arayüzü (Flask).
- Docker sayesinde izole, taşınabilir ve hızlı kurulum.
- **Yapay Zeka Desteği:** Bu projenin kodlama algoritmaları, mimari tasarımı ve Docker yapılandırma süreçlerinde yapay zeka asistanlarından destek alınarak geliştirme süreçleri optimize edilmiştir.

## 📦 1. Adım: Model Dosyalarını Hazırlama
GitHub dosya boyutu sınırları (100 MB) nedeniyle, eğitilmiş model ağırlıkları (`.h5` ve `.keras`) bu repoya doğrudan dahil edilmemiştir. Sistemi çalıştırmadan önce:

1. Proje içindeki `app` klasörüne girin ve manuel olarak **`model`** adında yeni bir klasör oluşturun.
2. Sağ taraftaki **Releases (Sürümler)** sekmesine gidin ve `v1.0` sürümündeki model dosyalarını indirin.
3. İndirdiğiniz dosyaları oluşturduğunuz `app/model/` klasörünün içine yerleştirin.

## 🔍 2. Adım: Test İçin Görsel Bulma
Sistemi test etmek için elinizde beyin MR görüntüleri olması gerekir. Eğer elinizde hazır veri seti yoksa, aşağıdaki yöntemlerle test görseli temin edebilirsiniz:
- **Kaggle:** [Brain Tumor Classification Dataset](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri) üzerinden binlerce görsele ulaşabilirsiniz.
- **Google Görseller:** "Brain MRI Tumor" veya "Healthy Brain MRI" aramaları yaparak rastgele örnekler indirebilirsiniz.

## 🛠️ 3. Adım: Kurulum ve Çalıştırma (Docker)

Projeyi çalıştırmak için bilgisayarınızda Docker'ın kurulu olması gerekir. Model dosyalarını yerleştirdikten sonra şu komutları uygulayın:

1. Terminali açın ve `app` dizinine girin:
```bash
cd beyin-tumoru-tespiti/app
