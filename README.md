# TextAnalyticsPro

TextAnalyticsPro is an advanced text analysis tool designed to extract insights, generate visualizations, and provide downloadable results. The application allows users to upload a PDF file, enter a URL, or provide direct text for analysis. It supports sentiment analysis, summarization, key findings extraction, word cloud generation, positive word identification, and named entity recognition (NER). Results are available for download in TXT or DOCX formats, including the generated word cloud image.

## Features

- **Text Extraction**: Extract text from PDF files, URLs, or direct input.
- **Key Findings**: Derive key insights in bullet points from the provided text.
- **Summarization**: Generate a concise summary of the provided text.
- **Word Cloud**: Generate and visualize a word cloud from the text.
- **Sentiment Analysis**: Analyze and classify the sentiment of the text.
- **Positive Words**: Extract the most positive words in the text.
- **NER Visualization**: Display named entities from the text using SpaCy.
- **Download Options**: Download results in TXT or DOCX format, with the WordCloud image included in the DOCX file.

## Installation

### Prerequisites

- Python 3.10 or higher.

### Setup

1. Clone this repository:

    ```bash
    git clone https://github.com/PriyanshuDey23/TextAnalyticsPro.git
    cd TextAnalyticsPro
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python3.10 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables for the Google API key:

    - Create a `.env` file and add the following:

    ```env
    GOOGLE_API_KEY=<your-google-api-key>
    ```

5. Run the application:

    ```bash
    streamlit run app.py
    ```

## Usage

- **Upload PDF**: Upload a PDF file to extract and analyze text.
- **Enter URL**: Provide a URL to extract and analyze text from the page.
- **Text Input**: Paste or type text directly to analyze it.

After processing, the results will be displayed with options to download them as a TXT or DOCX file.

## Libraries Used

- **Streamlit**: For creating the web interface.
- **SpaCy**: For Named Entity Recognition (NER).
- **WordCloud**: For generating the word cloud image.
- **PyMuPDF**: For PDF text extraction.
- **Google Generative AI**: For summarizing key insights and extracting positive words.
- **Requests**: For making HTTP requests to fetch content from URLs.
- **Python-dotenv**: For managing environment variables.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
