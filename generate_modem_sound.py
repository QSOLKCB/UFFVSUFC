"""Generate a dial-up style modem sound.

This script synthesizes a short audio clip made up of multiple sine-wave segments
at different frequencies. The resulting file, `dialup_cosmology.wav`,
is meant to evoke the ear‑piercing squeal of a dial‑up modem – a playful nod
to the cosmological residuals that inspired the diss track.

To regenerate the audio, run this script with Python 3. It requires only
the standard library (`wave`, `struct`, and `numpy`).
"""

import numpy as np
import wave
import os


def generate_modem_sound(
    filename: str = "dialup_cosmology.wav",
    sample_rate: int = 44100,
    segments: list[tuple[float, float]] | None = None,
) -> None:
    """Create a WAV file consisting of concatenated sine‑wave segments.

    Args:
        filename: Name of the file to generate.
        sample_rate: Sampling rate of the audio in Hz.
        segments: A list of `(frequency, duration)` tuples. Each tuple
            defines a sine tone segment with the given frequency in Hz
            and duration in seconds. If `None`, a default pattern is used.

    The generated audio is normalised to fit within the int16 range.
    """
    # Default pattern reminiscent of a chaotic dial‑up handshake
    if segments is None:
        segments = [
            (800, 0.5),
            (1400, 0.3),
            (600, 0.4),
            (1600, 0.4),
            (1000, 0.6),
        ]

    audio = np.array([], dtype=np.float32)
    for freq, duration in segments:
        t = np.linspace(0, duration, int(duration * sample_rate), endpoint=False)
        tone = 0.5 * np.sin(2 * np.pi * freq * t)
        audio = np.concatenate((audio, tone))

    # Normalize to int16 and write the file
    audio_int16 = np.int16(audio * 32767)
    with wave.open(filename, "w") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)  # 16 bits per sample
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(audio_int16.tobytes())


if __name__ == "__main__":
    out_path = os.path.join(os.path.dirname(__file__), "dialup_cosmology.wav")
    generate_modem_sound(filename=out_path)
    print(f"Generated {out_path}")