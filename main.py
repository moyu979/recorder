import pyaudio
import wave

CHUNK=1024
FORMAT=pyaudio.paInt16
CHANNELS=1
RATE=16000
delays=5

p_in=pyaudio.PyAudio()
p_out=pyaudio.PyAudio()
stream_in=p_in.open(format=FORMAT,
              channels=CHANNELS,
              rate=RATE,
              frames_per_buffer=CHUNK,
              input=True)

stream_out=p_out.open(format=FORMAT,
                   channels=CHANNELS,
              rate=RATE,
              frames_per_buffer=CHUNK,
              output=True)


frames=[]

for i in range(0,int(RATE/CHUNK*delays+5)):
    data=stream_in.read(CHUNK)
    frames.append(data)

i=0
while(True):
    
    stream_out.write(frames[i])
    frames[i]=stream_in.read(CHUNK)
    i=i+1
    i=int(i%(RATE/CHUNK*delays))

