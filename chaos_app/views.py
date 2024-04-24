from celery import shared_task
import requests
from django.http import JsonResponse
from .models import Image
from .serializers import ImageSerializer

@shared_task
def generate_images(prompt):
    queryset = Image.objects.all()
    
    prompt = 'A red flying dog'
    headers = {
        "authorization": "Bearer MY API KEY",
        "accept": "image/*"
    }

    output_format = "webp"

    response = requests.post(
        "https://api.stability.ai/v2beta/stable-image/generate/core",
        headers=headers,
        files={"none": ''},
        data={
            "prompt": prompt,
            "output_format": output_format,
        },
    )

    if response.status_code == 200:
        image_data = response.content
        image_filename = f"{prompt.replace(' ', '-').lower()}.webp"
        
        # Save the image data to the database
        serializer = ImageSerializer(data={'prompt': prompt, 'url': image_filename})
        if serializer.is_valid():
            serializer.save()
        else:
            return JsonResponse(serializer.errors, status=400)
        
        with open(image_filename, 'wb') as file:
            file.write(image_data)
        return JsonResponse(f"Image for {prompt} generated successfully and saved in the database", safe=False)
    else:
        raise Exception(str(response.json()))
