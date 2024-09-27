from django.http import JsonResponse
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from django.views.decorators.csrf import csrf_exempt
import json
from .models import URL  # Import the URL model

SLACK_BOT_TOKEN = 'api token for'  
slack_client = WebClient(token=SLACK_BOT_TOKEN)

@csrf_exempt
def slack_shortener(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        long_url = data['text']
        url_obj, created = URL.objects.get_or_create(long_url=long_url)
        short_url = request.build_absolute_uri(url_obj.short_code)

        try:
            slack_client.chat_postMessage(channel=data['channel_id'], text=f'Shortened URL: {short_url}')
        except SlackApiError as e:
            return JsonResponse({'error': str(e)})

        return JsonResponse({'message': 'URL shortened successfully'})

