from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Generator(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    generator_company_name_text = models.CharField(max_length=200)
    generator_first_name_text = models.CharField(max_length=200)
    generator_last_name_text = models.CharField(max_length=200)
    generator_address_text = models.CharField(max_length=200)
    generator_city_text = models.CharField(max_length=200)
    generator_zip_text = models.CharField(max_length=200)
    generator_state_text = models.CharField(max_length=200)
    generator_email_text = models.EmailField(max_length=200)
    generator_epaid_text = models.CharField(max_length=200, blank=True, null=True)
    generator_sic_text = models.CharField(max_length=200, blank=True, null=True)
    generator_permit_number_text = models.CharField(max_length=200, blank=True, null=True)
    generator_resposible_party_name_text = models.CharField(max_length=200, blank=True, null=True)
    generator_resposible_party_phone_text = models.CharField(max_length=200, blank=True, null=True)
    generator_discription_text = models.CharField(max_length=200)

    def __str__(self):
        return self.generator_company_name_text





class Prequal(models.Model):
    generator = models.ForeignKey(Generator, on_delete=models.CASCADE)
    generator_process_information = models.CharField(max_length=200)
    profile_submit_date = models.DateTimeField('date received')
    sample = models.CharField(max_length=200, blank=True, null=True)
    generator_location_type = models.CharField(max_length=200)
    physical_characteristics = models.CharField(max_length=200)
    water_concentration = models.CharField(max_length=200)
    mud_concentration = models.CharField(max_length=200, blank=True, null=True)
    other_concentration = models.CharField(max_length=200, blank=True, null=True)
    extra_other_concentration = models.CharField(max_length=200, blank=True, null=True)
    properties_pH = models.CharField(max_length=200)
    properties_odor = models.CharField(max_length=200)
    properties_color = models.CharField(max_length=200)
    properties_explosive = models.CharField(max_length=200)
    properties_reactive = models.CharField(max_length=200)
    properties_pyrophoric = models.CharField(max_length=200)

    metals_arsenic = models.CharField(max_length=200)
    metals_cadmium = models.CharField(max_length=200)
    metals_chromium = models.CharField(max_length=200)
    metals_copper = models.CharField(max_length=200)
    metals_lead = models.CharField(max_length=200)
    metals_mercury = models.CharField(max_length=200)
    metals_nickel = models.CharField(max_length=200)
    metals_silver = models.CharField(max_length=200)
    metals_zinc = models.CharField(max_length=200)
    metals_cyanide = models.CharField(max_length=200)

    chlorinated = models.CharField(max_length=200)
    toxic_organic = models.CharField(max_length=200)
    sulfides = models.CharField(max_length=200)

    analytical_upload = models.FileField(blank=True, null=True)
    approved = models.CharField(max_length=200, blank=True, null=True)

    profile_number = models.IntegerField(default=10000)

    def __str__(self):
        return self.generator_process_information






class Manifest(models.Model):
    manifest = models.ForeignKey(User, on_delete=models.CASCADE)
    manifest_number = models.CharField(max_length=200)
    manifest_first_name_text = models.CharField(max_length=200)
    manifest_last_name_text = models.CharField(max_length=200)
    manifest_delivery_date = models.DateTimeField('date received')
    manifest_upload = models.FileField(blank=True, null=True)

    def __str__(self):
        return self.manifest_number
