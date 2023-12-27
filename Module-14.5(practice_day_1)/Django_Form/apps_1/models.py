from django.db import models
from datetime import timedelta


class Testmodel(models.Model):
    roll = models.AutoField(primary_key=True)
    big_integer_field = models.BigIntegerField(default=7556485636333)
    num = models.BinaryField(default=b'\x00')
    boolean_field = models.BooleanField(default=False)
    name = models.CharField(max_length=255, default='sakib')
    date_field = models.DateField(default='2023-01-01')
    date_time_field = models.DateTimeField(default='2023-01-01T00:00:00')
    decimal_field = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00)
    duration_field = models.DurationField(default=timedelta(days=1))
    email_field = models.EmailField(default='')
    file_field = models.FileField(upload_to='files/', default='')
    file_path_field = models.FilePathField(path='/path/to/files/', default='')
    float_field = models.FloatField(default=0.0)
    generic_ip_address_field = models.GenericIPAddressField(default='0.0.0.0')
    image_field = models.ImageField(upload_to='images/', default='')
    integer_field = models.IntegerField(default=0)
    json_field = models.JSONField(default=dict)
    slug_field = models.SlugField(default='')
    small_integer_field = models.SmallIntegerField(default=0)
    text_field = models.TextField(default='')
    time_field = models.TimeField(default='00:00:00')
    url_field = models.URLField(default='')
    # uuid_field = models.UUIDField(default=uuid.uuid4)

    # ... Add more fields as needed

    def __str__(self):
        return f"Roll : {self.roll} - {self.name}"


test_model_instance = Testmodel()
test_model_instance.save()
