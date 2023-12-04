from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password, is_active=True, is_staff=False, is_admin=False, is_confirmed=False):
        if not email:
            raise ValueError('Her Ulynyjynyn Hökman Bir E-Poçta Addresi Bolmalydyr.')
        if not password:
            raise ValueError('Her Ulynyjyn Hökman Bir Paroly Bolmalydyr.')

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.confirmed = is_confirmed
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, username, password):
        user = self.create_user(email, username, password=password, is_staff=True, is_confirmed=True)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(email, username, password=password, is_staff=True, is_admin=True, is_confirmed=True)
        return user
