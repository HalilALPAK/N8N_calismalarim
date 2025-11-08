from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi
import requests

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "YouTube Transcript API",
        "usage": "GET /transcript?id=VIDEO_ID",
        "example": "http://127.0.0.1:5000/transcript?id=NfYX1MWUHYs",
        "supported_languages": ["tr", "en"],
        "proxy_support": "Add &proxy=true for proxy usage"
    })

@app.route("/transcript", methods=["GET"])
def get_transcript():
    video_id = request.args.get("id")
    use_proxy = request.args.get("proxy", "false").lower() == "true"
    
    if not video_id:
        return jsonify({"error": "Video ID is required"}), 400
    
    # Proxy ayarları (isteğe bağlı)
    proxies = None
    if use_proxy:
        # Ücretsiz proxy servisleri (çalışmayabilir, kendi proxy'nizi kullanın)
        proxies = {
            'http': 'http://proxy-server:port',
            'https': 'http://proxy-server:port'
        }
    
    try:
        # Proxy ile transcript alma
        if proxies:
            transcript = YouTubeTranscriptApi.get_transcript(
                video_id, 
                languages=["tr", "en"],
                proxies=proxies
            )
        else:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=["tr", "en"])
            
        return jsonify({
            "success": True,
            "video_id": video_id,
            "transcript_count": len(transcript),
            "transcript": transcript,
            "used_proxy": use_proxy
        })
    except Exception as e:
        error_message = str(e)
        
        # IP blok kontrolü
        if "IP" in error_message or "block" in error_message.lower():
            return jsonify({
                "error": "IP blocked by YouTube",
                "video_id": video_id,
                "suggestion": "Try using proxy with ?proxy=true parameter",
                "details": error_message
            }), 429
        elif "VideoUnavailable" in error_message:
            return jsonify({
                "error": "Video is unavailable or does not exist",
                "video_id": video_id
            }), 404
        elif "TranscriptsDisabled" in error_message:
            return jsonify({
                "error": "Transcripts are disabled for this video",
                "video_id": video_id
            }), 404
        elif "NoTranscriptFound" in error_message:
            return jsonify({
                "error": "No transcript found in Turkish or English for this video",
                "video_id": video_id
            }), 404
        else:
            return jsonify({
                "error": f"An unexpected error occurred: {error_message}",
                "video_id": video_id
            }), 500

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5001, debug=False)
