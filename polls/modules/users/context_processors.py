from .forms import UserProfileForm


def context_vars(request):
    return {
        'user_profile_form': UserProfileForm()
    }
