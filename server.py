from flask import Flask, request, jsonify, send_from_directory
import time, os, subprocess

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AUDIO_OUTPUT = "output_audio.mp3"  # the file your Python TTS generates

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(BASE_DIR, 'favicon.ico')

@app.route("/")
def serve_index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/convert", methods=["POST"])
def convert_text():
    data = request.json
    text = data["text"]
    model = data["model"]
    accent = data["accent"]
    rate = str(data["rate"])

    # 1. Save incoming text to timestamped file
    ts = str(int(time.time()))
    #filename = f"speech_{ts}.txt"
    filename = f"speech.txt"
    filepath = os.path.join(BASE_DIR, filename)

    with open(filepath, "w", encoding="utf8") as f:
        f.write(text)

    # 2. Run your existing Python program
    cmd = [
        "python",
        "main.py",
        filename,
        "--model", model,
        "--accent", accent,
        "--rate", rate,
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)

    print("----- MAIN.PY STDOUT -----")
    print(result.stdout)

    print("----- MAIN.PY STDERR -----")
    print(result.stderr)

    if result.returncode != 0:
        raise Exception(
            f"main.py failed with code {result.returncode}\n"
            f"STDERR:\n{result.stderr}"
        )


    # Return the audio filename
    return jsonify({
        "audio": AUDIO_OUTPUT
    })

@app.route('/<path:filename>')
def serve_audio(filename):
    return send_from_directory(BASE_DIR, filename)
    
if __name__ == "__main__":
    app.run(debug=True)
