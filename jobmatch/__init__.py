from dotenv import load_dotenv
load_dotenv()  # take environment variables

import os
if not "TRUMPET_GEMINI_AK" in os.environ:
    print("No Gemini API key detected, AI features will return mock responses.")
    print("Please add a Gemini API key with the environment variable TRUMPET_GEMINI_AK to enable real AI responses.")

if "TRUMPET_MOCK_AI" in os.environ:
    print("Mock AI mode is enabled, AI features will return mock responses.")
    print("Please unset the environment variable TRUMPET_MOCK_AI to enable real AI responses.")

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)
