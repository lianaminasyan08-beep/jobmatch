from django.http import JsonResponse

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
