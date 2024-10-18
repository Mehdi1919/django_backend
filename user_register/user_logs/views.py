from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegistrationForm, UserProfileForm

@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

        user_form = UserRegistrationForm(data)
        profile_form = UserProfileForm(data)

        if user_form.is_valid() and profile_form.is_valid():
            try:
                user = user_form.save()
                profile = profile_form.save(commit=False)
                profile.user = user
                profile.save()
                
                return JsonResponse({
                    'username': user.username,
                    'email': user.email,
                    'address': profile.address,
                    'agreement': profile.agreement,
                    'city': profile.city,
                    'cnic': profile.cnic,
                    'comment': profile.comment,
                    'dob': profile.dob,
                    'gender': profile.gender,
                    'hobby': profile.hobby,
                    'phone': profile.phone,
                    'postalCode': profile.postalCode,
                }, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({
                'user_errors': user_form.errors,
                'profile_errors': profile_form.errors
            }, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
