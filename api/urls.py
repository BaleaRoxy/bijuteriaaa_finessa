
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from api.register import RegisterViewSet
from api.bijuterii import BijuterieViewSet

router = DefaultRouter()
router.register(r'register', RegisterViewSet, basename='register')
router.register(r'bijuterii', BijuterieViewSet)


urlpatterns=[
    path('', include(router.urls)),
    path('browser-auth', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]