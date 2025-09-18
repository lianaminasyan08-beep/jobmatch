from dotenv import load_dotenv
load_dotenv()  # take environment variables

import os
if not "GEMINI_AK" in os.environ:
    print("No Gemini API key detected, AI features will return mock responses.")
    print("Please add a Gemini API key with the environment variable GEMINI_AK to enable AI features.")

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)
