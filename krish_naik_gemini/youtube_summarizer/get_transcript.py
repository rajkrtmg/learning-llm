import base64
import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, VideoUnavailable

# Function to fetch transcript from YouTube video URL
def get_transcript_text(video_url):
    try:
        video_id = video_url.split("=")[1]
        transcript_raw_text = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_final = "\n\n".join([sentence['text'] for sentence in transcript_raw_text])
        return transcript_final
    except TranscriptsDisabled:
        return "Transcripts are disabled for this video."
    except VideoUnavailable:
        return "Video is unavailable."

def get_download_link(text, filename):
    """Generates a link to download the text file."""
    b64 = base64.b64encode(text.encode()).decode()
    return f'<a href="data:file/txt;base64,{b64}" download="{filename}">Download Transcript</a>'

# Main function to create Streamlit app
def main():
    st.title('YouTube Video Transcript Viewer')

    # Input box for entering YouTube video URL
    video_url = st.text_input('Enter YouTube Video URL:', '')

    if st.button('Submit'):
        if video_url:
            transcript = get_transcript_text(video_url)
            st.subheader('Transcript:')
            transcript_area = st.text_area('Transcript Output', transcript, height=400)

            # Download button
            st.markdown(get_download_link(transcript, "transcript.txt"), unsafe_allow_html=True)

if __name__ == '__main__':
    main()