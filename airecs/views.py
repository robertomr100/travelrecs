from django.shortcuts import render
from django.http import JsonResponse
from .forms import TripForm
from django.views.decorators.csrf import csrf_exempt
import environ
import os
import openai
env = environ.Env(
)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

openai.organization = env('OPENAI_ORGANIZATION')
openai.api_key = env('OPENAI_API_KEY')
openai.Model.list()

def index(request):
    form = TripForm()
    maps = "https://maps.google.com/maps/api/js?key="+env('GMAPS_API_KEY')+"&libraries=places"
    print(maps)
    return render(request, 'airecs/index.html', {'form': form,'maps':maps})

@csrf_exempt
def recs(request):
    if request.method == 'POST':
        print("a")
        form = TripForm(request.POST)
        print(form)
        if form.is_valid():
            location = form.cleaned_data['location']
            interests = form.cleaned_data['interests']
            num_of_days = form.cleaned_data['number_of_days']
            prompt = "I am going to "+location+" for "+str(num_of_days)+" days.. My interest are: "+interests+". What should I do? Can you create an schedule with the best activities to do in the time frame of my trip and an explanation of why do the activity ? Print out only the schedule without any disclaimers"
            print(prompt)
            completion = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "user", "content":prompt }
                ]
            )
            print(completion.choices[0].message.content)
            return JsonResponse({"places": completion.choices[0].message.content})
        else:
            return JsonResponse({"error": "Invalid form data"}, status=400)
    else:
        return JsonResponse({"error": "Invalid request method"}, status=400)
