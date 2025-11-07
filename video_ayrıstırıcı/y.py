import yt_dlp
import os

# Video URL'si
url = "https://www.youtube.com/watch?v=NfYX1MWUHYs"

# yt-dlp seçenekleri - ses ve video ayrı indirip birleştir
ydl_opts = {
    'format': 'best[height<=720]',  # 720p veya altı
    'outtmpl': 'video.%(ext)s',  # Dosya adı
    'merge_output_format': 'mp4',  # Çıktı formatı
}

# Video indirme
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        ydl.download([url])
        print("Video başarıyla indirildi!")
    except Exception as e:
        print(f"Hata oluştu: {e}")
        
        # Daha basit format deneyelim
        print("\nDaha basit format deneniyor...")
        simple_opts = {
            'format': '232+233',  # 720p video + ses
            'outtmpl': 'video.%(ext)s',
            'merge_output_format': 'mp4',
        }
        
        with yt_dlp.YoutubeDL(simple_opts) as ydl_simple:
            try:
                ydl_simple.download([url])
                print("Video basit format ile indirildi!")
            except Exception as simple_error:
                print(f"Basit format da çalışmadı: {simple_error}")
