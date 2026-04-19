🧠 Beyin Tümörü Tespit Sistemi (Brain Tumor Detection)
Bu proje, MR (Manyetik Rezonans) görüntüleri üzerinden beyin tümörlerini yüksek doğrulukla tespit etmek amacıyla geliştirilmiş bir Derin Öğrenme (Deep Learning) web uygulamasıdır. Proje, sistem bağımlılıklarını ortadan kaldırmak ve her ortamda sorunsuz çalışabilmek için tamamen Docker altyapısı üzerine kurgulanmıştır.

🚀 Özellikler
Derin öğrenme modeli ile medikal görüntü analizi.

Kullanıcı dostu web arayüzü.

Docker sayesinde "benim bilgisayarımda çalışıyordu, sunucuda çalışmıyor" sorununa son veren, izole ve taşınabilir ortam.

Not: Bu projenin kodlama algoritmaları, mimari tasarımı ve Docker yapılandırma süreçlerinde yapay zeka asistanlarından destek alınarak geliştirme adımları hızlandırılmış ve optimize edilmiştir.

📦 Model Dosyaları Hakkında (ÖNEMLİ ADIM)
GitHub dosya boyutu sınırları (100 MB) nedeniyle, eğitilmiş model ağırlıkları (.h5 ve .keras dosyaları) bu repoya doğrudan dahil edilmemiştir. Projeyi çalıştırmadan önce sistemin hata vermemesi için şu adımları uygulamalısınız:

Klonladığınız veya indirdiğiniz bu projenin içindeki app klasörüne girin.

app klasörünün içine manuel olarak model adında yeni, boş bir klasör oluşturun.

GitHub ana sayfasındaki sağ tarafta bulunan Releases (Sürümler) sekmesinden model ağırlıklarını indirin.

İndirdiğiniz dosyaları, az önce oluşturduğunuz app/model/ klasörünün içine atın.

🛠️ Kurulum ve Çalıştırma (Docker Zorunludur)
Projeyi bilgisayarınızda çalıştırmak için Docker'ın kurulu ve çalışıyor olması gerekmektedir. Model dosyalarını yukarıdaki gibi ayarladıktan sonra şu adımları izleyin:

Terminal/Komut Satırını açın ve klasörlerin içine girmek için sırasıyla şu komutları yazın:

Bash
cd beyin-tumoru-tespiti
cd app
Docker imajını oluşturmak için aşağıdaki komutu çalıştırın:

Bash
docker build -t beyin-tumoru-app .
İmaj oluştuktan sonra konteyneri başlatın:

Bash
docker run -p 5000:5000 beyin-tumoru-app
Tarayıcınızı açın ve şu adrese gidin: http://127.0.0.1:5000
