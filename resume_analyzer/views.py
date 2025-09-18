from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
# Create your views here.


def logout_view(request):
    logout(request)
    return redirect('login')

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Неверные данные'})
    return render(request, 'login.html')


from google import genai
from google.genai.types import GenerateContentConfig, HttpOptions
from os import environ, path
from .ai import RESUME_SYS
from .mock import MOCK_RESPONSE

def analyze_resume_with_gemini(fpath, job):
    return MOCK_RESPONSE
    # Set the model to Gemini 1.5 Pro.
    client = genai.Client(api_key=environ["GEMINI_AK"])

    # Upload the file
    sample_file = client.files.upload(file=fpath)

    print(f"Uploaded file '{sample_file.display_name}' as: {sample_file.uri}")
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[job, sample_file],
        config=GenerateContentConfig(
            system_instruction=RESUME_SYS.split("\n"),
            response_mime_type = "application/json",
            response_schema = {
                "type": "object",
                "properties": {
                    "score": {"type": "integer"},
                    "reason": {"type": "string"},
                    "details": {"type":"array","items":{"type": "object",
                        "properties": {
                            "subscore": {"type": "integer"},
                            "reason": {"type":"array","items":{"type": "string"}},
                            "suggestions": {"type":"array","items":{"type": "string"}}
                        }
                    }},
                    "error": {"type": "boolean"},
                    "recommendations": {"type":"array","items":{"type": "string"}}
                },
            },
            temperature = 0.2
        ),
    )
    return response.text

def analyze_resume(request):
    sample_cv = {
        "name": "John Doe",
        "skills": ["Python", "Django", "Git"],
        "experience": 3
    }
    result = {
        "match_to_standard": "75%",
        "missing_skills": ["REST APIs", "SQL"]
    }
    return JsonResponse({"cv": sample_cv, "analysis": result})

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
# password change
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

from django.contrib.auth.decorators import login_required

JOB = """
Senior Android Developer
Full-time, Nice, no remote option
Ganiio

We're searching for a senior Android developer to join Ganiio, a company at the forefront of AI innovation.
Ganiio has a dynamic team that values respect and creativity. Our head office is in Nice, and we have
branches in major cities like Berlin, Tokyo and Madrid.

As part of your position, you will work on Gani Chat, our flagship product providing a robust AI chatbot
to over a million users. You will also develop new apps that bring cutting edge technologies to the masses.
You will get a competitive salary, as well as health insurance coverage.

Requirements:
- 5-10 years of experience building Android apps
- Familiarity with Jetpack Compose, Coil, Kotlin coroutines and Modern Android Development
- Experience with model-view-viewmodel (MVVM) practices
- Ability to work in a team

Optional, but encouraged:
- Familiarity with AI software development assistants
- Experience building VR/AR apps
- Strong time management skills

Apply by September 26.
"""

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def analyzer_ui(request):
    result = analyze_resume_with_gemini(
        "/home/meow/Documents/test_resume.pdf",
        JOB
    )
    print(result)
    return render(request, 'resume.html', {"result": result})

