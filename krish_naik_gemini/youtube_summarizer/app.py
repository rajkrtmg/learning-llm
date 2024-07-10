from dotenv import load_dotenv
load_dotenv() # load all the environment variable from the .env file

import os
import streamlit as st
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# model = genai.GenerativeModel('gemini-1.0-pro-latest')

video_url = "https://www.youtube.com/watch?v=1K5HbbJUT2k"

def get_transcript_text(video_url):
    try:
        video_id = video_url.split("=")[1]
        transcript_raw_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_final = ""
        for i in transcript_raw_text:
            transcript_final += " " + i['text']
        return transcript_final.strip()
    except Exception as e:
        raise e
    



