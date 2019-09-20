

#15.434e0.0578x
#notes = [C, C+, D, D+, E, F, F+, G, G+, A, A+, B]
#         1, 2,  3, 4,  5, 6, 7,  8, 9, 10, 11, 12

import winsound, time, math, threading, numpy, simpleaudio
C = 1 #todo: put these in a dictionary? 
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

def playNote(note, duration): # Using winsound (requires no extra libraries)
    winsound.Beep(math.floor(15.434 * math.exp(0.0578 * (note + 12 * Octave))), duration)

def playFrequency(freq, duration): # Using winsound (requires no extra libraries)
    winsound.Beep(freq, duration)

def playNote2(note, duration): # Using simpleaudio library
    t = numpy.linspace(0, duration, duration * 44100, False)
    freq = 15.434 * math.exp(0.0578 * (note + 12 * Octave))
    n = numpy.sin(freq * t * 2 * numpy.pi)
    audio = n * (2**15 - 1) / numpy.max(numpy.abs(n))
    audio = audio.astype(numpy.int16)
    play = simpleaudio.play_buffer(audio, 1, 2, 44100)
    play.wait_done()

def playFrequency2(freq, duration): # Using simpleaudio library
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





