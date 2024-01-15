from rest_framework import serializers
from .models import User, Data

import re


class UserSerializer(serializers.ModelSerializer):

    def validate(self, data):
        SQL_INJECTION_REGEX_NAME = re.compile(r'[\'\"]?([\w\._%+-]+)[\'\"]?(\W|\.|\*|\+|\-|\||\&|\(|\))')
        SQL_INJECTION_REGEX_EMAIL = re.compile(r'[\'\"]?([\w\._%+-]+@[\w\._%+-]+)[\'\"]?')
        SQL_INJECTION_REGEX_PASSWORD = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[@#$%^&*()_+|~-]).{8,}$')

        name = data.get('name', '')
        email = data.get('email', '')
        password = data.get('password', '')

        for field in ['id', 'created_at']:
            if field in data and data[field] is not None:
                raise serializers.ValidationError({field: 'This field is not mutable.'})
            
        for field in ['name', 'email', 'password']:
            if not data.get(field, ''):
                raise serializers.ValidationError({field: 'This field is required.'})
            
        if SQL_INJECTION_REGEX_NAME.search(data.get('name', '')):
            raise serializers.ValidationError({'name': 'This field cannot contain malicious code.'})

        # Validación del campo email
        if not SQL_INJECTION_REGEX_EMAIL.search(data.get('email', '')):
            raise serializers.ValidationError({'email': 'This field cannot contain malicious code.'})

        # Validación del campo password
        if not SQL_INJECTION_REGEX_PASSWORD.search(data.get('password', '')):
            raise serializers.ValidationError({'password': 'The password must have at least 8 characters, a capital letter, a number and a special character.'})
        # for field in ['name', 'email', 'password']:
        #     if SQL_INJECTION_REGEX.search(data.get(field, '')):
        #         raise serializers.ValidationError({field: 'This field cannot contain malicious code.'})
            

        return data
    
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password', 'created_at', 'status')

        # # Validate name is only text
        # if not isinstance(name, str):
        #     raise serializers.ValidationError({'name': 'This field must be a string.'})

        # # Validate email is in a valid format
        # if not EMAIL_REGEX.match(email):
        #     raise serializers.ValidationError({'email': 'This field must be a valid email address.'})

        # # Validate id and created_at are not mutable
        # if id is not None:
        #     raise serializers.ValidationError({'id': 'This field is not mutable.'})
        # if created_at is not None:
        #     raise serializers.ValidationError({'created_at': 'This field is not mutable.'})

        # # Validate name is only letters and spaces
        # if not name.isalpha():
        #     raise serializers.ValidationError({'name': 'This field must only contain letters and spaces.'})
        

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'text', 'sentiment', 'emotion', 'user', 'status')