# 🤖 Hackathon-Etkinlik Bildirim Botu (n8n)

Bu proje, **n8n** üzerinde kurulu bir otomasyon akışıdır.  
Amaç, yazılım dünyasındaki **hackathon**, **bootcamp**, **ideathon**, **zirve** ve benzeri etkinlikleri web scraping ile toplayıp, yeni bir etkinlik tespit edildiğinde **Telegram** üzerinden otomatik bildirim göndermektir.

---

## 🚀 Özellikler

- 🌐 Web Scraping ile farklı sitelerden etkinliklerin çekilmesi
- 📅 Tarihi geçmiş etkinliklerin filtrelenmesi
- 🧩 JSON verilerinin birleştirilip temizlenmesi
- 📤 Yeni etkinlikler eklendiğinde **Telegram’a otomatik mesaj gönderimi**
- 📓 Opsiyonel olarak verilerin Google Sheets veya veritabanına kaydedilmesi

---

## ⚙️ Kullanılan Teknolojiler

- [n8n](https://n8n.io/) (Workflow otomasyonu)
- Telegram Bot API
- Web Scraping (HTML verilerinden div/span seçimi)
- JSON Data Parsing

---

## 🧠 Çalışma Mantığı

1. n8n **HTTP Request** veya **Function** node’u ile HTML verisini çeker
2. **HTML Extract / Code** node’u ile başlık, tarih ve tür gibi alanlar ayrıştırılır
3. **Filter** node’u bugünden sonraki etkinlikleri seçer
4. Yeni kayıtlar **Telegram Send Message** node’u ile bildirilir
![N8N Flow](n8n.png)

