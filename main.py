import wave
import numpy as np
import matplotlib.pyplot as plt

import sys


def average(a1, a2):
    return a1 + a2 / 2
average = np.vectorize(average)

# def normalise(x, imin, imax, omin, omax):
#     # output = output_start + ((output_end - output_start) / (input_end - input_start)) * (input - input_start)
#     return imin + ((omax - omin) / (imax - imin)) * (x - imin)
# normalise = np.vectorize(normalise)

def get_form(fname):
    with wave.open(fname, 'r') as wf:
        signal = wf.readframes(-1)
        wd = wf.getparams()
        print(fname, wd)
        num_channels = wd[0]
        assert num_channels == 2

    signal = np.frombuffer(signal, np.int16)

    offset = 97_000 * num_channels
    offset = 30_000 * num_channels
    # if '2' in fname:
    #     offset -= 7_510 * num_channels
    signal = signal[offset:offset + 60_000 * num_channels]
    # print(signal[20_000:])


    channels = [signal[channel::num_channels] for channel in range(num_channels)]
    # print(channels)

    return average(*channels)

    # return single

if len(sys.argv) == 1:
    print(f'Usage: {sys.argv[0]} <file1.wav> [file2.wav ...]')
    sys.exit(1)


plt.figure(1)
plt.title('compare')
c = 1
for fname in sys.argv[1:]:
    plt.subplot(3, 1, c)
    c += 1
    plt.plot(get_form(fname))

plt.show()
