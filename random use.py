import sys
from threading import Thread
import time

lyrics = [
    ("just trust me, you'll be fine", 0.09),
    ("and when i'm back in chicago, i feel it", 0.09),
    ("Another version of me i was in it", 0.09),
    ("i wave goodbye to the end of beginning", 0.08),
    ("goodbye, goodbye, goodbye, goodbye", 0.06)
]
delays = [0, 1.3, 2.2, 2.4, 3.2]

def animate_text(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def sing_lyric(lyric, delay, speed):
    time.sleep(delay)
    animate_text(lyric, speed)

def sing_song():
    Threads = []
    for i in range(len(lyrics)):
        lyric, speed = lyrics[i]
        t = Thread(target=sing_lyric, args=(lyric, delays[i], speed))
        Threads.append(t)
        t.start()
        for thread in Threads:
            thread.join()

if __name__=="__main__":
    sing_song()        