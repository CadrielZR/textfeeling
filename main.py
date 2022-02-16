from youtube_transcript_api import YouTubeTranscriptApi
import sklearn.model_selection
from sklearn.model_selection import train_test_split
import pandas as pd

link_tans = YouTubeTranscriptApi.get_transcript('QRk9d6c6ERk')

with open('str_file.txt', 'w', encoding="utf-8") as f:
    for i in link_tans:
        f.write('%s\n' % i['text'])