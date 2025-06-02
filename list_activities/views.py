from django.shortcuts import render, redirect
import requests

def activities_view(request):
    access_token = request.session.get('access_token')
    if not access_token:
        return redirect('home:input')  # if session expired

    response = requests.get(
        'https://www.strava.com/api/v3/athlete/activities',
        headers={'Authorization': f'Bearer {access_token}'}
    )
    data = response.json()[:5]  # limit to 5 recent activities
    request.session['activities'] = data  # save to session to persist

    return render(request, 'list_activities/activities.html', {'activities': data})


def select_activity(request):
    if request.method == 'POST':
        activity_id = request.POST.get('activity_id')
        request.session['selected_activity_id'] = activity_id
        return redirect('list_frame:frames')  # go to frame overlay

    return redirect('list_activities:activities')
