from wave import open
from struct import Struct
from math import floor

frame_rate = 11025


def encode(x):
    """Encode float x between - 1 and 1 as two bytes."""
    i = int(16384 * x)
    return Struct("h").pack(i)


def play(sampler, name="song.wav", seconeds=2):
    """Wirte the output of a sampler functions as a wav file."""
    out = open(name, "wb")
