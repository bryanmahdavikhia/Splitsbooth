from django.shortcuts import render, redirect
import requests

def input_view(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        token_response = requests.post(
            'https://www.strava.com/oauth/token',
            data={
                'client_id': 'YOUR_CLIENT_ID',
                'client_secret': 'YOUR_CLIENT_SECRET',
                'code': code,
                'grant_type': 'authorization_code'
            }
        )

        token_data = token_response.json()
        access_token = token_data.get('access_token')

        if access_token:
            request.session['access_token'] = access_token
            return redirect('list_activities:activities')

    return render(request, 'home/input.html')
