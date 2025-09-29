# YouTube Video Summarizer 🎥📄

A Python-based web application that automatically summarizes YouTube videos using AI-powered text processing. Built with Streamlit for an intuitive user interface and LangChain for intelligent text summarization.

## 🌟 Features

- **Simple Interface**: Clean and user-friendly Streamlit web interface
- **YouTube Integration**: Direct video processing from YouTube URLs
- **AI-Powered Summarization**: Uses LangChain for intelligent content summarization
- **Real-time Processing**: Live feedback with loading indicators
- **Error Handling**: Robust error management for invalid URLs or processing issues

## 🚀 Demo

1. Enter a YouTube video URL
2. Click "Submit" to process the video
3. Get an AI-generated summary in seconds

## 📋 Prerequisites

Before running this application, make sure you have:

- Python 3.7 or higher
- pip package manager
- Internet connection for YouTube video access

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/sajinamatya/Youtube-Summarizer-.git
   cd Youtube-Summarizer-
   ```

2. **Install required dependencies**
   ```bash
   pip install streamlit
   pip install langchain
   pip install youtube-transcript-api
   pip install openai  # or your preferred LLM provider
   ```

3. **Set up environment variables** (if using OpenAI or other API services)
   ```bash
   export OPENAI_API_KEY="your-api-key-here"
   ```

## 🏃‍♂️ Usage

1. **Run the application**
   ```bash
   streamlit run user_interface_youtube.py
   ```

2. **Access the web interface**
   - Open your browser and navigate to `http://localhost:8501`
   - The Streamlit interface will load automatically

3. **Summarize a video**
   - Paste a YouTube video URL in the input field
   - Click the "Submit" button
   - Wait for the processing and summarization to complete
   - View the generated summary

## 📁 Project Structure

```
Youtube-Summarizer-/
│
├── user_interface_youtube.py    # Main Streamlit application
├── utils/                       # Utility modules
│   └── summary.py              # Core summarization logic
├── .gitignore                  # Git ignore file
└── README.md                   # Project documentation
```

## 🔧 Core Components

### Main Application (`user_interface_youtube.py`)
- Streamlit-based user interface
- Input handling for YouTube URLs
- Progress indicators and error management
- Display of summarized content

### Utils Module (`utils/summary.py`)
- `fetch_youtube_transcript()`: Extracts transcript from YouTube videos
- `generate_summary_with_chain()`: Processes transcript using LangChain for summarization

## 🤖 How It Works

1. **Input Processing**: User provides a YouTube video URL
2. **Transcript Extraction**: The application fetches the video's transcript
3. **Text Processing**: LangChain processes the transcript text
4. **Summarization**: AI generates a concise summary of the content
5. **Output Display**: Summary is presented in the web interface

## ⚙️ Configuration

The application can be configured by modifying the utility functions in the `utils/` directory:

- Adjust summarization parameters
- Modify transcript extraction settings
- Customize output formatting

## 🚨 Error Handling

The application includes comprehensive error handling for:
- Invalid YouTube URLs
- Videos without available transcripts
- Network connectivity issues
- API rate limiting
- Processing timeouts



1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request





## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the web framework
- [LangChain](https://langchain.com/) for AI text processing
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction

---

**Made with ❤️ by [sajinamatya](https://github.com/sajinamatya)**
