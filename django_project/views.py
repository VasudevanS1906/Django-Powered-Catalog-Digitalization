from django.shortcuts import render, redirect, HttpResponse
from .forms import ProductForm
from .models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from gtts import gTTS
from playsound import playsound
import os
from .forms import InputForm
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
  return render(request, 'index.html')

def home1(request):
  if request.method == 'POST':
      form = ProductForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return HttpResponse(b'Product added successfully!')  # redirect to a new URL
  else:
      form = ProductForm()
  return render(request, 'index1.html', {'form': form})
  #return render(request, 'index1.html')


def home2(request):
    selected_language = request.session.get('language')
    form = None

    if request.method == 'POST':
        if 'language' in request.POST:
            # User has selected a language
            selected_language = request.POST['language']
            request.session['language'] = selected_language
        else:
            # User has submitted the product form
            form = ProductForm(request.POST, request.FILES, language=selected_language)
            if form.is_valid():
                form.save()
                #return render(request, 'success.html', {'message': 'Product added successfully!'})
                return HttpResponse(b'Product added successfully!')
                

    if not selected_language:
        # If no language is selected, show the language selection form
        return render(request, 'index2.html')

    # Render the product form with the selected language
    form = form or ProductForm(language=selected_language)
    return render(request, 'index2.html', {'form': form})

def product_form(request):
    selected_language = request.session.get('language')
    if not selected_language:
        return redirect('index2')

    form = ProductForm(language=selected_language)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, language=selected_language)
        if form.is_valid():
            form.save()
            return render(request, 'success.html', {'message': 'Product added successfully!'})

    return render(request, 'product_form.html', {'form': form})

def home3(request):
  form = ProductForm()
  if request.method == 'POST':
      form = ProductForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return HttpResponse(b'Product added successfully!')  # redirect to a new URL
  else:
      form = InputForm()
  return render(request, 'index3.html', {'form': form})
  

@csrf_exempt
def play_input_label_speech(request):
    if request.method == 'POST' and 'text' in request.POST:
        text = request.POST['text']
        tts = gTTS(text=text, lang='en')
        tts.save('speech.mp3')  # Save the speech as an MP3 file
        playsound('speech.mp3')  # Play the audio
        os.remove('speech.mp3')  # Clean up: remove the generated MP3 file
        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def home4(request):
  selected_language = request.session.get('language')
  form = ProductForm()
  
  if request.method == 'POST':
      form = ProductForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return HttpResponse(b'Product added successfully!')  # redirect to a new URL
  else:
      form = InputForm()
    
  return render(request, 'index4.html', {'form': form})



@csrf_exempt
def perform_ocr(request):
    if request.method == 'POST':
        username = 'your username here'
        api_password = 'your password here'
        ocr_api_url = 'https://www.ocrwebservice.com/restservices/processDocument?gettext=true'

        image_file = request.FILES['image']

        try:
            data = {
                'file': image_file
            }
            auth = (username, api_password)

            response = requests.post(ocr_api_url, files=data, auth=auth)

            if response.ok:
                recognized_text = response.text
                return JsonResponse({'recognized_text': recognized_text})
            else:
                return JsonResponse({'error': 'Failed to perform OCR'}, status=500)
        except requests.RequestException as e:
            return JsonResponse({'error': f'Error performing OCR: {e}'}, status=500)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
  
def home5(request):
  form = ProductForm()
  if request.method == 'POST':
      form = ProductForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return HttpResponse(b'Product added successfully!')  # redirect to a new URL
  else:
      form = InputForm()
  return render(request, 'index5.html', {'form': form})

def home6(request):
  form = ProductForm()
  if request.method == 'POST':
      form = ProductForm(request.POST, request.FILES)
      if form.is_valid():
          form.save()
          return HttpResponse(b'Product added successfully!')  # redirect to a new URL
  else:
      form = InputForm()
  return render(request, 'index6.html', {'form': form})
  #return render(request, 'index6.html')

def home7(request):
  emps = Product.objects.all()
  context = {
    'emps': emps
  }
  print(context)
  return render(request, 'index7.html',context)




def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # redirect to a new URL
    else:
        form = ProductForm()
    return render(request, 'index1.html', {'form': form})
  
