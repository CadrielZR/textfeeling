import os
import pysrt


def downloadyoutubesrt(link):
    video_id = link[link.find('?v=') + 3:]
    import subprocess
    subprocess.call(['youtube-dl',
                     # for sub
                     '--sub-lang', 'en',
                     '--write-sub',
                     '--convert-subs', 'srt',
                     # for filename
                     '--output', './' + video_id + '.%(ext)s',
                     link,
                     ])

    srt_path = os.path.abspath(os.path.dirname(__file__) + '/{}.en.srt'.format(video_id))

    subs = pysrt.open(srt_path)
    for sub in subs:
        print(sub.start)
        print(sub.end)
        print(sub.text)
