from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import google.generativeai as genai
import os
import retry
from grpc._channel import _InactiveRpcError
from django.http import JsonResponse
from PIL import Image
from django.http import HttpResponse


# Create your views here.

genai.configure(api_key=os.environ['API_KEY'])



@retry.retry(exceptions=_InactiveRpcError, tries=9, delay=2, backoff=2)
@login_required
def chat(request):
    # Initialize the models
    model_text = genai.GenerativeModel('gemini-pro')
    model_image = genai.GenerativeModel('gemini-pro-vision')
    
    if request.method == 'POST':
        if 'user_input' in request.POST:
            # Get user input from the form
            user_input = request.POST['user_input']
            
            # Generate a response using Gemini AI
            response = model_text.generate_content(user_input)
            
            # Pass the response to the template
            return JsonResponse({'user_input': user_input, 'response': response.text})
        
        elif 'imageUpload' in request.FILES:
            # Handle image form submission
            image_file = request.FILES['imageUpload']
            
            # Preprocess the image if necessary
            pil_image = Image.open(image_file)
            pil_image = pil_image.convert('RGB')
            
            # Pass the processed image to the model
            response_image = model_image.generate_content(pil_image)
            
            # Extract the relevant information from the response
            response_text_from_image = response_image.text
            
            return render(request, './chat/chat.html', {'response_text_from_image': response_text_from_image})
    
    # If it's a GET request or if the request does not match any condition above,
    # just render the empty form
    return render(request, './chat/chat.html')