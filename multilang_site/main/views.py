# main/views.py
from django.shortcuts import render
from .models import Article
from django.utils.translation import activate
import openai
from django.shortcuts import redirect
from django.conf import settings
from django.shortcuts import render, get_object_or_404
import os
from dotenv import load_dotenv


# Provide the path to the .env file
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

def chatbot(request):
    # Your view logic here
    prompt = "Your prompt text here"
    response = openai.Completion.create(
        engine="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=150
    )
    # Process and return response
    return render(request, 'chatbot.html', {'response': response.choices[0].text})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'main/article_detail.html', {'article': article})


def article_list(request):
    # Logique pour récupérer la liste des articles
    articles = Article.objects.all()  # Exemple hypothétique
    context = {
        'articles': articles,
    }
    return render(request, 'main/article_list.html', context)


def set_language(request):
    if request.method == 'POST':
        language = request.POST.get('language')
        activate(language)
        return redirect('article_list')
