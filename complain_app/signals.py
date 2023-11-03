from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Complain, Complain_traking
from datetime import timedelta

@receiver(pre_save, sender=Complain)
def update_complain_tracking(sender, instance, **kwargs):
    
    # Check if the status field is being changed
    if instance.pk is not None:
        original_complain = Complain.objects.get(pk=instance.pk)
        tracking = Complain_traking.objects.get(fk_complain_id=instance)
        # Check if is_varify has been changed to True
        if not original_complain.is_varify and instance.is_varify:
            # Add review date when is_varify is changed to True
            tracking.reviewed_date = instance.updated_at

            # Add expected resolve date as today + 2 days
            tracking.expected_resolve_date = instance.updated_at + timedelta(days=2)

        # Check if fk_staff has been assigned
        if original_complain.fk_staff is None and instance.fk_staff is not None:
            # Update the assign date
            tracking.assigned_date = instance.updated_at

        if original_complain.complain_status != instance.complain_status:
            # Update the assign date
            tracking.assigned_date = instance.updated_at