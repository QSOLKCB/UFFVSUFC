# UFFVSUFC Repository

This repository contains the source material for the **“Dial‑Up Cosmology”** diss track — a creative roast that transforms cosmological residuals into the shriek of a dial‑up modem.  The project grew out of a tongue‑in‑cheek challenge: turn a questionable cosmological model into music and expose its flaws with humor.

## Contents

| File | Description |
| --- | --- |
| `dialup_cosmology.wav` | A short audio clip of modem‑like screeches used as the backbone of the diss track. |
| `generate_modem_sound.py` | A Python script to regenerate the `dialup_cosmology.wav` file using sine‑wave segments. |
| `PROMPT.md` | The full Producer.ai prompt with lyrics and instructions for generating the track using the audio file. |

## Usage

1. Ensure you have Python 3 and NumPy installed.  On most systems you can install NumPy via `pip install numpy`.
2. Run `python generate_modem_sound.py` from the repository root to regenerate `dialup_cosmology.wav`.  The script synthesises several high‑pitch tones to mimic a modem handshake.
3. Use the contents of `PROMPT.md` as your input to Producer.ai (or a similar generative music tool), and upload the generated `dialup_cosmology.wav` as described.

Feel free to expand this project by adding scripts to sonify real cosmological data or by remixing the audio in your DAW of choice.
