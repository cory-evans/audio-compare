import wave
import numpy as np
import matplotlib.pyplot as plt

import sys


def average(a, b):
    return a + b / 2

average = np.vectorize(average)


def get_form(fname, offset=0, length=-1):
    with wave.open(fname, 'r') as wf:
        signal = wf.readframes(-1)
        wd = wf.getparams()

        num_channels = wd[0]

    signal = np.frombuffer(signal, np.int16)

    if length < 0:
        signal = signal[offset:]
    else:
        signal = signal[offset:offset + length * num_channels]

    offset = offset * num_channels

    channels = [signal[channel::num_channels] for channel in range(num_channels)]

    return average(*channels)


if len(sys.argv) == 1:
    print(f'Usage: {sys.argv[0]} <file1.wav> [file2.wav ...]')
    sys.exit(1)


plt.figure(1)
plt.title('compare')
c = 1
for fname in sys.argv[1:]:
    plt.subplot(3, 1, c)
    c += 1
    plt.plot(get_form(fname, 30_000, 50_000))

plt.show()
