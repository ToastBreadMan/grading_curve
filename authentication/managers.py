from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, password, **kwargs):
        user = self.model(email=email, username=username, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, email, password, **kwargs):
        user = self.create_user(email=email, username=username, password=password)
        user.is_admin = True
        user.save()
        return user