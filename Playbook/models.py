from django.db import models

# Create your models here.
class SME(models.Model):
    key = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, null=False, verbose_name=_("User name"))
    email_address = models.EmailField(max_length=255, null=False, verbose_name=_("Email Address"))
    phone_regex = RegexValidator(regex=r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$')
    phone_number = models.CharField(max_length=20, null=False,blank=False,validators=[phone_regex])
    given_name = models.CharField(max_length=255, null=False, blank=False)
    surname = models.CharField(max_length=255, null=False, blank=False)
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.SME

    class Meta:
        '''
        Meta class for the model.
        '''
        verbose_name = _('Subject Matter Expert')
       	verbose_name_plural = _('Subject Matter Experts')
