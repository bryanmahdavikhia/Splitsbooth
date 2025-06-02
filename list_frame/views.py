from django.shortcuts import render

def frame_view(request):
    activities = request.session.get('activities', [])
    selected_id = request.session.get('selected_activity_id')

    selected_activity = next((a for a in activities if str(a['id']) == selected_id), None)
    
    if not selected_activity:
        return redirect('list_activities:activities')

    return render(request, 'list_frame/frame.html', {'activity': selected_activity})
