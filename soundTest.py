

#15.434e0.0578x
#notes = [C, C+, D, D+, E, F, F+, G, G+, A, A+, B]
#         1, 2,  3, 4,  5, 6, 7,  8, 9, 10, 11, 12

import winsound, time, math, threading, numpy, simpleaudio
C = 1
Cs = 2
D = 3
Ds = 4
E = 5
F = 6
Fs = 7
G = 8
Gs = 9
A = 10
As = 11
B = 12

Octave = 2

def playNote(note, duration):
    winsound.Beep(math.floor(15.434 * math.exp(0.0578 * (note + 12 * Octave))), duration)

def playNote2(note, duration):
    t = numpy.linspace(0, duration, duration * 44100, False)
    freq = 15.434 * math.exp(0.0578 * (note + 12 * Octave))
    n = numpy.sin(freq * t * 2 * numpy.pi)
    audio = n * (2**15 - 1) / numpy.max(numpy.abs(n))
    audio = audio.astype(numpy.int16)
    play = simpleaudio.play_buffer(audio, 1, 2, 44100)
    play.wait_done()

def playFrequency(freq, duration):
    t = numpy.linspace(0, duration, duration * 44100, False)
    n = numpy.sin(freq * t * 2 * numpy.pi)
    audio = n * (2**15 - 1) / numpy.max(numpy.abs(n))
    audio = audio.astype(numpy.int16)
    play = simpleaudio.play_buffer(audio, 1, 2, 44100)
    play.wait_done()


playNote2(C, 1)



"""
for i in range(37, 32000):
    playFrequency(i, 0.1)
    time.sleep(0.05)



"""





Notes = []

Notes.append([98, 20])
Notes.append([110, 10])
Notes.append([87, 20])
Notes.append([98, 50])
Notes.append([32767, 50]) # rest

Notes.append([116, 20])
Notes.append([110, 10])
Notes.append([87, 20])
Notes.append([98, 50])
Notes.append([32767, 60]) # rest

Notes.append([98, 20])
Notes.append([110, 10])
Notes.append([87, 20])
Notes.append([98, 50])
Notes.append([32767, 50]) # rest

Notes.append([116, 20])
Notes.append([110, 10])
Notes.append([87, 20])
Notes.append([98, 50])
Notes.append([32767, 60]) # rest


for i in Notes:
    if i[0] == 32767:
        time.sleep(i[1])
    else:
        playFrequency(i[0], i[1]/100)


