import os
import uuid
from wordcloud import WordCloud
import google.generativeai as genai
from dotenv import load_dotenv
from io import BytesIO

# Load environment variables
load_dotenv()

# Access API key from environment
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Configure the Generative AI client
genai.configure(api_key=GOOGLE_API_KEY)

# Function to derive key insights (Summarization)
def extract_key_findings(input_text):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-8b")

        chat_session = model.start_chat(
            history=[{
                "role": "user",
                "parts": [f"Derive key insights in bullet points from the below text:\n\n{input_text}"]
            }]
        )

        response = chat_session.send_message("Please summarize the above insights further if necessary.")
        return response.text.strip()
    
    except Exception as e:
        return f"Error extracting key findings: {str(e)}"

# Function for generating the wordcloud
def generate_wordcloud(text):
    try:
        # Create a unique filename for the wordcloud image
        unique_filename = f"wordcloud_{uuid.uuid4().hex}.png"
        
        # Create and generate a word cloud image
        wordcloud = WordCloud(width=800, height=800, background_color='black', min_font_size=10).generate(text)
        
        # Save the wordcloud image to a local directory
        output_directory = "generated_images"
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)

        image_path = os.path.join(output_directory, unique_filename)
        wordcloud.to_file(image_path)
        
        return image_path  # Return the local path of the generated wordcloud image
    except Exception as e:
        return f"Error generating wordcloud: {str(e)}"

# Function for sentiment analysis
def sentiment_analysis(input_text):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-8b")

        chat_session = model.start_chat(
            history=[{
                "role": "user",
                "parts": [f"Perform sentiment analysis on the following text:\n\n{input_text}"]
            }]
        )

        response = chat_session.send_message("Please analyze the sentiment and provide feedback.")
        return response.text.strip()
    
    except Exception as e:
        return f"Error performing sentiment analysis: {str(e)}"

# Function to extract most positive words
def most_positive_words(input_text):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-8b")

        chat_session = model.start_chat(
            history=[{
                "role": "user",
                "parts": [f"Please extract the most positive keywords from the below text\n\n{input_text}"]
            }]
        )

        response = chat_session.send_message("Provide additional context or refine the keywords further if necessary.")
        return response.text.strip()
    
    except Exception as e:
        return f"Error extracting positive words: {str(e)}"

# Function for summarization
def summarization(input_text):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-8b")

        chat_session = model.start_chat(
            history=[{
                "role": "user",
                "parts": [f"Provide a short summary of the following text:\n\n{input_text}"]
            }]
        )

        response = chat_session.send_message("Please provide a more concise summary if necessary.")
        return response.text.strip()
    
    except Exception as e:
        return f"Error generating summary: {str(e)}"
