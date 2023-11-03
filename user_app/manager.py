from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True
    def create_user(self,phone,password=None,**extrafields):
        user = self.model(phone=phone,**extrafields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self,phone,password,**extrafields):
        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('is_active',True)
        return self.create_user(phone,password,**extrafields)
