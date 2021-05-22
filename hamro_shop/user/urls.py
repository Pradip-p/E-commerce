from django.urls import path,include
from user.views import  register, dashboard


urlpatterns = [
    path('dashboard/', dashboard, name="dashboard"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", register, name="register"),

]



# That will give you access to all of the following URLs:

# accounts/login/ is used to log a user into your application. Refer to it by the name "login".

# accounts/logout/ is used to log a user out of your application. Refer to it by the name "logout".

# accounts/password_change/ is used to change a password. Refer to it by the name "password_change".

# accounts/password_change/done/ is used to show a confirmation that a password was changed. Refer to it by the name "password_change_done".

# accounts/password_reset/ is used to request an email with a password reset link. Refer to it by the name "password_reset".

# accounts/password_reset/done/ is used to show a confirmation that a password reset email was sent. Refer to it by the name "password_reset_done".

# accounts/reset/<uidb64>/<token>/ is used to set a new password using a password reset link. Refer to it by the name "password_reset_confirm".

# accounts/reset/done/ is used to show a confirmation that a password was reset. Refer to it by the name "password_reset_complete".