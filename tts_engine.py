# tts_engine.py

import edge_tts


async def synthesize_speech(text, voice, rate=0, output_path="output_audio.mp3"):
    communicator = edge_tts.Communicate(text, voice)

    # Apply the speech rate if it's not the default (0)
    if rate != 0:
        communicator.rate = rate

    await communicator.save(output_path)
    print(f"Speech saved to '{output_path}' using voice: {voice} with rate: {rate}")
