# -*- coding: utf-8 -*-

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""
from google.cloud import translate

def detect_language(text):
    
    translate_client = translate.Client()

    text = text

    language = translate_client.detect_language(text)
   
    return language['language']
