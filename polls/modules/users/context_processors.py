from .forms import UserProfileForm


def vars(request):
    return {
        'user_profile_form': UserProfileForm()
    }
