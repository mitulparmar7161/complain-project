from django.db import models
# from user_app.models import CustomUser
# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    office_reg_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    help_line = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='organization_logo/', null=True, blank=True)
    district = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Organizations"
        db_table = "organization"

    def _str_(self):
        return self.name

class Department(models.Model):
    fk_organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    office_no = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.IntegerField(max_length=100) 
    website = models.CharField(max_length=100)  
    help_line = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='department_logo/', null=True, blank=True)
    district = models.CharField(max_length=100)
    taluka = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)
    state = models.CharField(max_length=100)  
    created_at = models.DateTimeField(auto_now_add=True) 

    class Meta:
        verbose_name_plural = "Departments"
        db_table = "department"

    def _str_(self):
        return self.name

class Complain_category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Complain Categories"
        db_table = "complain_category"

    def _str_(self):
        return self.name

class Before_complain_resolved_file(models.Model):
    before_complain_resolve_file = models.FileField(upload_to='before_complain_resolved_file/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Before Complain Resolved Files"
        db_table = "before_complain_resolved_file"

    def _str_(self):
        return str(self.id)

class After_complain_resolved_file(models.Model):
    after_complain_resolve_file = models.FileField(upload_to='after_complain_resolved_file/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "After Complain Resolved Files"
        db_table = "after_complain_resolved_file"

    def _str_(self):
        if self.after_complain_resolve_file:
            return self.after_complain_resolve_file.name
        return str(self.id)

class Complain(models.Model):
    customer_account_no = models.CharField(max_length=100)
    fk_complain_category = models.ForeignKey(Complain_category, on_delete=models.CASCADE)
    complain_title = models.CharField(max_length=100)
    complain_description = models.TextField()
    before_complain_resolved_file = models.ManyToManyField(Before_complain_resolved_file,null=True, blank=True)
    after_complain_resolved_file = models.ManyToManyField(After_complain_resolved_file, null=True, blank=True)
    fk_consumer = models.ForeignKey("user_app.CustomUser", on_delete=models.CASCADE)
    fk_organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    fk_department = models.ForeignKey(Department, on_delete=models.CASCADE)
    fk_staff = models.ForeignKey("user_app.StaffUser", on_delete=models.CASCADE , null=True, blank=True)
    complain_status = models.CharField(max_length=100, choices=(
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Re opened', 'Re opened'),
    ), default='Pending')
    complain_priority = models.CharField(max_length=100, choices=(
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ), default='Low')
    is_public = models.BooleanField(default=False)
    is_valid = models.BooleanField(default=False)
    is_edited = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta: 
        verbose_name_plural = "Complains"
        db_table = "complain"

    def _str_(self):
        return self.complain_title

class Complain_traking(models.Model):
    fk_complain_id = models.ForeignKey(Complain, on_delete=models.CASCADE)
    complain_status = models.options = (
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
        ('Re opened', 'Re opened'),
    )
    assigned_date = models.DateTimeField(null=True, blank=True)
    reviewed_date = models.DateTimeField(null=True, blank=True)
    expected_resolve_date = models.DateTimeField(null=True, blank=True)
    work_start_date = models.DateTimeField(null=True, blank=True)
    work_end_date = models.DateTimeField(null=True, blank=True)
    complain_closed_date = models.DateTimeField(null=True, blank=True)
    complain_reopened_date = models.DateTimeField(null=True, blank=True)
    staff_complain_close_status = models.BooleanField(default=False)
    user_complain_close_status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)