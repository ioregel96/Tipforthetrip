from django.urls import path, include
from .views import SignUpView, LoginView, CurrentUserView, LogoutView,AllUsersView,UserView,SignupAndLoginView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from .contact_views import ContactCRUDManager

# from .views import current_user
# from .jwt_token_views import LoginView, SignUpView

urlpatterns = [
    path('signup/', SignUpView.as_view(),name="signup"),
    path('signup/login/', SignupAndLoginView.as_view(), name='signup_login'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('<slug:uuid_str>/', UserView.as_view(), name="user"),
    path('', AllUsersView.as_view(), name="users"),
    # path('validate/token/', LoginView.as_view(), name='login'),
    # path('token/refresh/', TokenRefreshView.as_view(), name="token_refresh"),

    path('contact/manage/<slug:user_id>', ContactCRUDManager.as_view(), name="contactCRUD"),
    # path('contact/get-contact/', ContactCRUDManager.as_view(), name="getContact"),
    # # path('contact/all/', GetAllContactsView.as_view(), name="getAllContacts"),
    # path('contact/update-contact/<slug:uuid_str>/', ContactCRUDManager.as_view(), name="updateContact"),
    # path('contact/delete-contact/<slug:uuid_str>/', ContactCRUDManager.as_view(), name="deleteContact")# Fetch all users




]

