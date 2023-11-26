import hashlib
from django.db import models

class HashField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = kwargs.get('max_length', 64)
        kwargs['editable'] = False
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        value = getattr(model_instance, self.attname, None)
        if value:
            hashed_value = hashlib.sha256(value.encode()).hexdigest()
            setattr(model_instance, self.attname, hashed_value)
            return hashed_value
        return super().pre_save(model_instance, add)