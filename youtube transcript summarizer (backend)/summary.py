from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi
from calculaterogue import calculate_rouge
youtube_video = input("Enter the YouTube video URL: ")
video_id = youtube_video.split("=")[1]
video_id
# from IPython.display import YouTubeVideo
# YouTubeVideo(video_id)
YouTubeTranscriptApi.get_transcript(video_id)
transcript = YouTubeTranscriptApi.get_transcript(video_id)
#transcript[0:5]
print("\n")
print('Original Transcript:')
print("\n")
full_transcript = " ".join([segment["text"] for segment in transcript])
print(full_transcript)
result = ""
for i in transcript:
    result += ' ' + i['text']
#print(result)
print("\n")
print("Original Transcript Length:")
print(len(result))
summarization_model = "sshleifer/distilbart-cnn-12-6"
summarization_revision = "a4f8f3e"
summarizer = pipeline('summarization',model=summarization_model, revision=summarization_revision)
num_iters = int(len(result)/1000)
summarized_text = []
for i in range(0, num_iters + 1):
  start = 0
  start = i * 1000
  end = (i + 1) * 1000
  print("\ninput text \n" + result[start:end])
  out = summarizer(result[start:end])
  out = out[0]
  out = out['summary_text']
  print("Summarized text\n"+out)
  summarized_text.append(out)

#print(summarized_text)
print("\n")
print("Summarized Text Length:")
print(len(str(summarized_text)))
print("\n")
print("The Summarized Text is Shown Below:")
print("\n")
print(str(summarized_text))
print("\n")
print("Rogue Score Is:")
rogue_score=calculate_rouge(str(full_transcript),str(summarized_text))
print(rogue_score)
# choice = input("Do you want to check another video summary? (yes/no): ")
# if choice.lower() != "yes":
#   print("Exiting the program. Thank you!")
#   break

