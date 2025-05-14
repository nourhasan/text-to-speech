# Text-to-Speech (TTS) Converter

A simple, modular **Text-to-Speech** (TTS) converter written in Python that reads text from a `.txt` file and converts it into speech using Microsoft's **Edge TTS** API. The script allows you to control key parameters such as:

* **Voice models** (e.g., Adam, Evelyn, Derek, Lola)
* **Accent selection** (US or UK)
* **Speech speed control** (rate of speech)

This project provides flexibility and easy-to-use functionality for converting text into lifelike speech with custom configurations.

---

### Features

* **Voice Selection**: Choose from a variety of voices (Adam, Evelyn, Derek, Lola).
* **Accent Options**: US or UK accent for each voice model.
* **Speech Speed Control**: Adjust the speech speed using the `--rate` parameter (positive values speed up, negative values slow down).
* **Default File Handling**: The default `.txt` file is `speech.txt`. You can specify a different file if needed.
* **Easy Customization**: Modular design with multiple Python files, making it easy to extend or modify.
* **Audio Output**: Speech is saved as an `MP3` file, or you can modify it to play the audio directly.

---

### Requirements

* Python 3.7+
* `edge-tts` Python library: for speech synthesis.

Install the required dependencies using:

```bash
pip install edge-tts
```

---

### How to Use

1. **Clone the repository**:

   ```bash
   git clone https://github.com/nourhasan/text-to-speech.git
   cd text-to-speech
   ```

2. **Run the script** with the default file (`speech.txt`):

   ```bash
   python main.py
   ```

3. **Run with custom file, voice model, accent, and rate**:

   ```bash
   python main.py my_text_file.txt --model adam --accent uk --rate 1.0
   ```

   * **`--model`**: Choose the voice model (e.g., `adam`, `evelyn`, `derek`, `lola`).
   * **`--accent`**: Choose the accent (e.g., `us`, `uk`).
   * **`--rate`**: Adjust the speed of the speech (default is `0`, positive values for faster speech, negative for slower).

---

### Example Output

* The generated speech will be saved as `output_audio.mp3`.
* You can adjust the **speech rate** with the `--rate` argument (e.g., `--rate 1.0` for faster speech).

---

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Contributing

Feel free to fork this repo, contribute with improvements, or report issues via GitHub issues.