from .models import Profile


def get_user(request):
    # if request.user.is_authenticated:
    #     profile = Profile.objects.get(user=request.user)
    # if request.method =='POST':
    #     profile = Profile.objects.get(user=request.user)
    
    profile = Profile.objects.last()
    return {'profile':profile}