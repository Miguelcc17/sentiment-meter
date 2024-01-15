from .models import User, Data
from .serializers import UserSerializer, DataSerializer

from rest_framework.parsers import MultiPartParser

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from django.http import Http404

from django.contrib.auth.hashers import check_password
# from django.contrib.auth.models import User

import re
import csv
import pandas as pd

import requests
import time  # Import the time module for adding a delay
from dotenv import load_dotenv
load_dotenv()
import os

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

    def get_queryset(self):
        # Get the 'email' parameter from the request
        email = self.request.query_params.get('email', None)
        password = self.request.query_params.get('password', None)

        # Validate the email format using a simple regular expression
        if email and not re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email):
            # Handle the error for an invalid email format
            raise Http404("Invalid email format")

        # If 'email' parameter is present, use the filter method of Django ORM
        if email:
            users = User.objects.filter(email=email, password=password)

            if not users.exists():
                raise Http404("User not found")
            
            return users
            
            # # If 'password' parameter is present, check if it matches the stored password
            # if password:
            #     users = [user for user in users if check_password(password, user.password)]
            #     if not users:
            #         raise Http404("Incorrect password")
            
            # return users

        # If there is no 'email' parameter, return all users
        return User.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status': 'User deactivated'}, status=status.HTTP_204_NO_CONTENT)

    def perform_destroy(self, instance):
        instance.status = False
        instance.save()
    
class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DataSerializer


    def comment_category_emotion(self, text: str = None, both: int = 0):
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

        if both == 0:
            result_category = comment_category(text)
            result_emotion = comment_emotion(text)
            return [result_category[0][0], result_emotion[0][0]]
        elif both == 1:
            return comment_category(text)
        elif both == 2:
            return comment_emotion(text)
    


    def create(self, request, *args, **kwargs):
        csv_file = request.data.get('csv_file')
        if csv_file:
            # Lee el contenido del archivo CSV utilizando pandas
            try:
                df = pd.read_csv(csv_file)
                # Itera sobre los registros y envíalos al frontend de manera asíncrona
                finish_resul = []
                for row in df.iloc[0:].values:
                    finish_resul.append([{'text': str(row[0])}, self.comment_category_emotion(row)])
                return Response({'result': finish_resul}, status=200)    
                    # Aquí puedes enviar data_row al frontend de alguna manera (puede ser una llamada a una API, WebSockets, etc.)
            except pd.errors.EmptyDataError:
                return Response({'error': 'El archivo CSV está vacío'}, status=400)
            except pd.errors.ParserError:
                return Response({'error': 'Error al procesar el archivo CSV'}, status=400)
        else:
            return Response({'error': 'No se proporcionó un archivo CSV'}, status=400)