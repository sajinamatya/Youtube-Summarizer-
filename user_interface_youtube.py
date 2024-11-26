import streamlit as st
from utils.summary import generate_summary_with_chain,fetch_youtube_transcript



def main() : 
    
    st.title("Youtube video summarizer ")
    youtube_link = st.text_input("Enter YouTube Video Link:")

    if st.button("Submit"):
        with st.spinner("Processing"):
            transcript = fetch_youtube_transcript(youtube_link)

        if transcript:
            with st.spinner("Summarizing..."):
                # Generate the youtube  summary using LangChain
                final_summary = generate_summary_with_chain(transcript)
                
                st.markdown("Summary")
                st.markdown(final_summary)
        else:
            st.error("Error fetching video.")

if __name__=="__main__":
    main()