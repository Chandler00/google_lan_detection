# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 15:54:40 2018

@author: s1883483
"""

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=""
from google.cloud import translate

def detect_language(text):
    
    translate_client = translate.Client()

    text = text

    language = translate_client.detect_language(text)
   
    return language['language']