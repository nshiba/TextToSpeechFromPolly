from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys


def request_speech(conversion_text):
    session = Session(profile_name="default")
    polly = session.client("polly")

    try:
        return polly.synthesize_speech(
            Text=conversion_text, OutputFormat="mp3", VoiceId="Mizuki")
    except (BotoCoreError, ClientError) as error:
        print(error)
        sys.exit(-1)


def get_audio_stream(polly_response):
    if "AudioStream" in polly_response:
        with closing(polly_response["AudioStream"]) as stream:
            try:
                return stream.read()
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("Could not stream audio")
        sys.exit(-1)


def split_str(s, n):
    length = len(s)
    return [s[i:i + n] for i in range(0, length, n)]


args = sys.argv
if len(args) <= 1:
    print('音声に変換するテキストのファイル名が必要です')
    sys.exit(-1)

filename = args[1]

f = open(filename)
text = f.read()
f.close()
texts = split_str(text, 1000)

print('分割数: ' + str(len(texts)))

basename = os.path.basename(filename)
dirname = os.path.dirname(filename)
name, ext = os.path.splitext(basename)
out_name = dirname + '/mp3/' + name + '_out.mp3'

if os.path.isdir(os.path.dirname(out_name)) is False:
    os.mkdir(os.path.dirname(out_name))

out = open(out_name, 'wb')
for i in range(len(texts)):
    print(basename + ' ' + str(i + 1) + '/' + str(len(texts)))
    response = request_speech(texts[i])
    stream = get_audio_stream(response)
    out.write(stream)

out.close()
