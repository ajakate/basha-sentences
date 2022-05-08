from IPython import embed
import re
import os

me_matcher = r"I'|\bI\b|\bme\b|\bmy\b|\bmine\b|mysel"
ye_matcher = r"\byou"
we_matcher = r"\bwe\b|\bus\b|\bour"

start = []
with open('speechling/beginner_3.txt') as f:
    for line in f:
        start.append(line.strip())

finish = []

for sentence in start:
    matches = False
    temp = [sentence]
    if re.search(me_matcher, sentence, re.IGNORECASE):
        news = []
        for s in temp:
            news.extend([f"(male speaker) {s}", f"(female speaker) {s}"])
        temp = news
    if re.search(ye_matcher, sentence, re.IGNORECASE):
        news = []
        for s in temp:
            news.extend([f"(formal) {s}", f"(informal) {s}"])
        temp = news
    if re.search(we_matcher, sentence, re.IGNORECASE):
        news = []
        for s in temp:
            news.extend([f"(me and you) {s}", f"(me and someone else) {s}"])
        temp = news
    finish.extend(temp)

with open('test.txt', 'w') as f:
    f.write('\n'.join(finish))
