from celery import shared_task
import requests
from django.http import JsonResponse

@shared_task
def generate_images(prompt):
    prompt = 'A red flying dog'
    headers = {
        "authorization": "Bearer Your API Key",
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
        image_filename = f"{prompt.replace(' ', '-').lower()}.webp"
        with open(image_filename, 'wb') as file:
            file.write(response.content)
        return JsonResponse(f"Image for {prompt} generated successfully", safe=False)
    else:
        raise Exception(str(response.json()))
