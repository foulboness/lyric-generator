import time
import re

# Colors
PINK = "\033[95m"
PURPLE = "\033[35m"
RESET = "\033[0m"

lrc_data = """
[00:00.00](Do I wanna know?)
[00:02.50]If this feeling flows both ways
[00:05.80](Sad to see you go)
[00:08.30]Was sorta hoping that you'd stay
[00:11.10](Baby we both know)
[00:13.80]That the nights were mainly made for saying
[00:17.50]Things that you can't say tomorrow day
[00:21.80]Crawlin' back to you
[00:24.60]Ever thought of calling when you've had a few?
[00:30.70]'Cause I always do
[00:33.90]Maybe I'm too busy being yours to fall for somebody new
[00:37.20]Now I've thought it through
[00:40.50]Crawling back to you
"""

def to_seconds(timestamp):
    minutes, seconds = timestamp.split(":")
    return int(minutes) * 60 + float(seconds)

def load_lyrics():
    pattern = r"\[(\d{2}:\d{2}\.\d{2})\](.*)"
    return [
        (to_seconds(t), text.strip())
        for t, text in re.findall(pattern, lrc_data)
    ]

lyrics = load_lyrics()

print(f"{PINK}˗ˏˋ Do i wanna know - Arctic Monkeys ˎˊ˗{RESET}")
input("Press ENTER to start...\n")

start = time.perf_counter()

for i, (timestamp, line) in enumerate(lyrics):

    while (time.perf_counter() - start) < timestamp:
        time.sleep(0.001)

    # Alternate pink and purple lines
    color = PINK if i % 2 == 0 else PURPLE

    print(f"{color} ♥ {line} {RESET}")

print(f"\n{PURPLE}🎵 SONG FINISHED 🎵{RESET}")