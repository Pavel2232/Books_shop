from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    def create_superuser(self, username, first_name, last_name, password=None):

        user = self.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                patronymic=None,
                birthday=None,
                password=password
            )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def create_user(self, username, first_name, last_name, patronymic, birthday, password=None):

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            patronymic=patronymic,
            birthday=birthday,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
