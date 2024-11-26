
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.llm import LLMChain
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from dotenv import load_dotenv
from langchain.docstore.document import Document
load_dotenv()


def fetch_youtube_transcript(video_url):
    try:
        yt = YouTube(video_url)
        video_id = yt.video_id
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return transcript
    except Exception as e:
        print(f"Error: {e}")
        return None


def split_the_text_chunk(text):
    """ Split the transcript into chunks in case of longer video the token is limited"""
    transcript_text = " ".join([entry["text"] for entry in text])
    document = Document(page_content=transcript_text)

    # Initialize the text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=0)
    
    # Split the document into chunks
    text_chunks = text_splitter.split_documents([document])

    return text_chunks

    # Intialization of the Gemini model
def intialize_model():
    """ Intializing the gemini model to generate the response for user inputs"""
    try:
        
        gemini_model = ChatGoogleGenerativeAI(model="gemini-pro",
                                temperature=0.4)
    except Exception as e:
        print("An error has occured in initalization of the gemini model", str(e))
    return gemini_model

def load_prompt():
    try:
        with open("utils//prompt.txt", "r") as prompt_read:
            prompt = prompt_read.read()
    except FileNotFoundError:
        print("Error: 'prompt.txt' file not found.")
    except PermissionError:
        print("Error: Permission denied when accessing file  'prompt.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
    return prompt



def generate_summary_with_chain(transcript_text):
   
    text = split_the_text_chunk(transcript_text)
    prompt = load_prompt()
    prompt_template = PromptTemplate(
        template=prompt,
        input_variables=["text"]
    )
    # Initialization of  the Gemini model
    gemini_model = intialize_model()
    chain = LLMChain(llm=gemini_model,prompt=prompt_template)
    final_summary = ""
    
    for i, chunk in enumerate(text):
        result = chain.run({"text": chunk.page_content})
        final_summary += f"### Summary {i + 1}:\n{result}\n\n"
    
    return final_summary

