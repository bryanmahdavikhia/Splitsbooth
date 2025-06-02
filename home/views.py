import requests
from django.shortcuts import render

def oauth_input(request):
    activities = []

    if request.method == 'POST':
        code = request.POST.get('code')

        # Step 1: Exchange code for access token
        token_response = requests.post(
            url='https://www.strava.com/oauth/token',
            data={
                'client_id': 158407,
                'client_secret': '7f6e0466537832b70757c9b3e19868e34ca4189c',
                'code': code,
                'grant_type': 'authorization_code'
            }
        )
        print(token_response)
        if token_response.status_code == 200:
            access_token = token_response.json().get('access_token')
            
            # Step 2: Use access token to get activities
            activities_response = requests.get(
                'https://www.strava.com/api/v3/athlete/activities',
                headers={'Authorization': f'Bearer {access_token}'}
            )

            if activities_response.status_code == 200:
                raw_activities = activities_response.json()
                activities = [{
                    'name': a['name'],
                    'distance': round(a['distance'] / 1000, 2),  # meters to km
                    'pace': get_pace(a['moving_time'], a['distance'])  # custom function
                } for a in raw_activities[:5]]  # just return latest 5
    print(activities)
    return render(request, 'home/input.html', {'activities': activities})


def get_pace(moving_time, distance_m):
    if distance_m == 0:
        return "-"
    pace_seconds = moving_time / (distance_m / 1000)
    minutes = int(pace_seconds // 60)
    seconds = int(pace_seconds % 60)
    return f"{minutes}:{seconds:02}"
