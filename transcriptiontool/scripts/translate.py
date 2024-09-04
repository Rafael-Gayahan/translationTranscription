import os
from openai import OpenAI
import sys

client = OpenAI(
    api_key = os.environ['OPENAI_API_KEY']
)

video_id = sys.argv[1]
#current_working_directory = os.getcwd()
#get the audio file from the tmp folder where we downlload it
#audio_file = os.path.join(os.getcwd(), 'tmp', video_id + '.m4a')

#print(audio_file)

audio_file_location = os.path.join(os.getcwd(), 'tmp', video_id + '.m4a')

audio_file = open(audio_file_location, "rb")

#straight from the documentation
translation = client.audio.translations.create(
    model="whisper-1",
    file=audio_file,
    response_format="text"
)

print(translation)