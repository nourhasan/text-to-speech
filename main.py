# main.py

import argparse
import asyncio
from config import VOICE_MAP, DEFAULT_MODEL, DEFAULT_ACCENT, DEFAULT_RATE
from utils import read_text_file
from tts_engine import synthesize_speech
import os

def parse_arguments():
    parser = argparse.ArgumentParser(description="Convert text file to speech with selectable voice models.")
    # Set default file name to "speech.txt" if no file is passed
    parser.add_argument("file", nargs="?", default="speech.txt", help="Path to the input .txt file.")
    parser.add_argument("--model", choices=VOICE_MAP.keys(), default=DEFAULT_MODEL, help="Voice model to use.")
    parser.add_argument("--accent", choices=["us", "uk"], default=DEFAULT_ACCENT, help="Accent to use.")
    parser.add_argument("--rate", type=float, default=DEFAULT_RATE, help="Speech rate. Default is 0 (normal speed).")
    return parser.parse_args()

def main():
    args = parse_arguments()

    # Check if the default file exists
    if not os.path.exists(args.file):
        print(f"Warning: The file '{args.file}' does not exist. Please provide a valid .txt file.")
        return

    try:
        text = read_text_file(args.file)
        voice = VOICE_MAP[args.model][args.accent]
        asyncio.run(synthesize_speech(text, voice, args.rate))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
