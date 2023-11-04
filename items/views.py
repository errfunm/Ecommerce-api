from rest_framework import permissions
from rest_framework import status



from rest_framework.reverse import reverse

from rest_framework.decorators import api_view, permission_classes

from rest_framework.authentication import TokenAuthentication

# from rest_framework_simplejwt import A
from .permissions import IsCostumer
from .serializers import *
import markdown
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, get_user
from django.conf import settings
from datetime import datetime, timedelta


@api_view(["GET"])
def api_root(request, format=None):
    sessions = request.session

    return Response(
        {
            "users": reverse("api-root", request=request, format=format),
            "product": reverse("product-list", request=request, format=format),
        }
    )























