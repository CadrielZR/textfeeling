from youtube_transcript_api import YouTubeTranscriptApi

link_tans = YouTubeTranscriptApi.get_transcript('BO9IwsvP7xM')

with open('str_file.txt', 'w') as f:
    for i in link_tans:
        f.write('%s\n' % i)