import requests
import time  # Import the time module for adding a delay
from dotenv import load_dotenv
load_dotenv()
import os

def comment_category_emotion(text: str = None, both: int = 0):
    """
    Analyzes sentiment and emotion of the given text using Hugging Face APIs.

    Parameters:
    - text (str): The input text for analysis.
    - both (int): Determines the type of analysis to perform.
        - 0: Analyze both sentiment and emotion.
        - 1: Analyze only sentiment.
        - 2: Analyze only emotion.

    Returns:
    - If both == 0: List containing sentiment and emotion analysis results.
    - If both == 1: Sentiment analysis result.
    - If both == 2: Emotion analysis result.
    """
    text = f"""{text}"""
    # Check input types
    if type(text) != str or type(both) != int:
        raise ValueError('Invalid input types')  # Raise an error with an informative message
    
    # Check the validity of the 'both' parameter
    if both not in [0, 1, 2]:
        raise ValueError('Invalid value for "both" parameter')  # Raise an error with an informative message
    
    # Retrieve Hugging Face API token from environment variables
    KEY_FACE = os.environ.get('TOKEN_HUGGINGFACE')

    if KEY_FACE == None or KEY_FACE == '':
        raise ValueError('Need token')
    
    def comment_category(text: str = None):
        """
        Analyzes sentiment of the given text using Hugging Face sentiment analysis API.

        Parameters:
        - text (str): The input text for sentiment analysis.

        Returns:
        - Sentiment analysis result in JSON format.
        """
        API_URL = "https://api-inference.huggingface.co/models/finiteautomata/beto-sentiment-analysis"
        headers = {"Authorization": f"Bearer {KEY_FACE}"}

        # Function to make a request to the API with retry logic
        def query_with_retry(payload, max_retries=3, delay_seconds=2):
            for _ in range(max_retries):
                response = requests.post(API_URL, headers=headers, json=payload)
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 503:  # HTTP 503 Service Unavailable (model loading)
                    print("Model is currently loading. Retrying in {} seconds...".format(delay_seconds))
                    time.sleep(delay_seconds)
                else:
                    print(f"Unexpected response: {response.status_code}. Retrying in {delay_seconds} seconds...")
                    time.sleep(delay_seconds)
            print("Max retries reached. Unable to get a valid response.")
            return {"error": "Max retries reached. Unable to get a valid response."}

        return query_with_retry({"inputs": text})

    # Function to analyze emotion using Hugging Face API
    def comment_emotion(text: str = None):
        """
        Analyzes emotion of the given text using Hugging Face emotion analysis API.

        Parameters:
        - text (str): The input text for emotion analysis.

        Returns:
        - Emotion analysis result in JSON format.
        """
        API_URL = "https://api-inference.huggingface.co/models/finiteautomata/beto-emotion-analysis"
        headers = {"Authorization": f"Bearer {KEY_FACE}"}

        # Function to make a request to the API with retry logic
        def query_with_retry(payload, max_retries=3, delay_seconds=2):
            for _ in range(max_retries):
                response = requests.post(API_URL, headers=headers, json=payload)
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 503:  # HTTP 503 Service Unavailable (model loading)
                    print("Model is currently loading. Retrying in {} seconds...".format(delay_seconds))
                    time.sleep(delay_seconds)
                else:
                    print(f"Unexpected response: {response.status_code}. Retrying in {delay_seconds} seconds...")
                    time.sleep(delay_seconds)
            print("Max retries reached. Unable to get a valid response.")
            return {"error": "Max retries reached. Unable to get a valid response."}

        return query_with_retry({"inputs": text})
    
    # Decide which analysis to perform based on the 'both' parameter
    if both == 0:
        return [comment_category(text), comment_emotion(text)]
    elif both == 1:
        return comment_category(text)
    elif both == 2:
        return comment_emotion(text)
    
