# 🧠 Beyin Tümörü Tespit Sistemi (Brain Tumor Detection)

Bu proje, MR (Manyetik Rezonans) görüntüleri üzerinden beyin tümörlerini yüksek doğrulukla tespit etmek amacıyla geliştirilmiş bir Derin Öğrenme (Deep Learning) web uygulamasıdır. Proje, sistem bağımlılıklarını ortadan kaldırmak ve her ortamda sorunsuz çalışabilmek için tamamen **Docker** altyapısı üzerine kurgulanmıştır.

## 🚀 Özellikler
- Derin öğrenme modeli ile medikal görüntü analizi.
- Kullanıcı dostu web arayüzü.
- Docker sayesinde "benim bilgisayarımda çalışıyordu, sunucuda çalışmıyor" sorununa son veren, izole ve taşınabilir ortam.
- *Not: Bu projenin kodlama algoritmaları, mimari tasarımı ve Docker yapılandırma süreçlerinde yapay zeka asistanlarından destek alınarak geliştirme adımları hızlandırılmış ve optimize edilmiştir.*

## 🛠️ Kurulum ve Çalıştırma (Docker Zorunludur)

Projeyi bilgisayarınızda çalıştırmak için Docker'ın kurulu ve çalışıyor olması gerekmektedir.

1. Repoyu bilgisayarınıza klonlayın veya zip olarak indirin.
2. Terminal/Komut Satırından `app` klasörünün (Dockerfile'ın bulunduğu dizin) içine girin.
3. Docker imajını oluşturmak için aşağıdaki komutu çalıştırın:
   ```bash
   docker build -t beyin-tumoru-app .