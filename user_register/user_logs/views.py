from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import UserRegistrationForm, UserProfileForm
from django.contrib.auth.models import User



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
                    'image': profile.image.url if profile.image else None
                }, status=201)
            except Exception as e:
                return JsonResponse({'error': str(e)}, status=500)
        else:
            return JsonResponse({
                'user_errors': user_form.errors,
                'profile_errors': profile_form.errors
            }, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def getusers(request):
    if request.method == "GET":
        users = User.objects.all()

        users_data = [{
            'id': user.id,
            'username': user.username,
            'email': user.email,
        } for user in users]

        return JsonResponse(users_data, safe=False, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def update_user(request, user_id):
    if request.method == "PATCH":
        try:   
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'user not found'})
        
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        
        user.save()
        
        return JsonResponse({
            'id': user.id,
            'username': user.username,
            'email': user.email,
        }, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete(request, user_id):
    if request.method == "DELETE":
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return JsonResponse({'error': 'user nod found'}, status=404)
        
        user.delete()
        return JsonResponse({'message': 'User deleted successfully'}, status=200)
    
    return JsonResponse({'error': 'Invalid request method'}, status=405)