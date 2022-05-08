from IPython import embed
import re
import os

me_matcher = r"I'|\bI\b|\bme\b|\bmy\b|\bmine\b|mysel"
ye_matcher = r"\byou"
we_matcher = r"\bwe\b|\bus\b|\bour"

#### pull together speechlings:
# files = os.listdir('./speechling')
# sent_files = filter(lambda file: [e for e in file if e in "123"], files)
# start = []
# for f in sent_files:
#     with open(f'speechling/{f}') as fi:
#         for line in fi:
#             start.append(line.split("\t")[0])
####


# INDIVIDUAL FIILE
start = []
with open('speechling/beg2.txt') as f:
    for line in f:
        start.append(line.split("\t")[0])
# embed()



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


# embed()



        # a,b = [f"(male speaker) {sentence}", f"(female speaker) {sentence}"]
        # finish.extend([a,b])
