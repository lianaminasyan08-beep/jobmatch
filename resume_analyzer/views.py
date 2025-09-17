from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def analyze_resume(request):
    uploaded = request.FILES.get("resume")
    if not uploaded:
        return Response({"error": "No resume uploaded"}, status=400)


    text = uploaded.read().decode("utf-8", errors="ignore")


    result = {
        "score": 85,
        "strengths": ["Ясная структура", "Хороший список навыков"],
        "weaknesses": ["Нет конкретных метрик в опыте"],
        "recommendations": ["Добавить KPI/цифры", "Развернуть описание проектов"],
        "keywords": ["Python", "Django", "REST"]
    }

    return Response(result)


# Create your views here.
