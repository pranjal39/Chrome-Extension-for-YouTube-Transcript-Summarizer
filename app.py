from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
youtube_video = "https://www.youtube.com/watch?v=FfhZFRvmaVY" 
video_id = youtube_video.split("=")[1]
video_id
YouTubeTranscriptApi.get_transcript(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id)
transcript[0:5]
result = ""
for i in transcript:
    result += ' ' + i['text']
#print(result)
print(len(result))
summarizer = pipeline('summarization')
num_iters = int(len(result)/2000)
summarized_text = []
for i in range(0, num_iters + 1):
  start = 0
  start = i * 2000
  end = (i + 1) * 2000
  print("input text \n" + result[start:end])
  out = summarizer(result[start:end])
  out = out[0]
  out = out['summary_text']
  print("S U M M A R I Z E D - T E X T= \n"+out)
  summarized_text.append(out)

#print(summarized_text)

len(str(summarized_text))
str(summarized_text)
from transformers import pipeline

# using pipeline API for summarization task
summarization = pipeline("summarization")
original_text = ""
summary_text = summarization(original_text)[0]['summary_text']
print("Summary:", summary_text)
