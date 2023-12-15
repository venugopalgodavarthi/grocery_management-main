from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

# Create your models here.


class category_items(models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_name = models.CharField(max_length=50)
    cat_img = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.cat_name


class product_item(models.Model):
    cat_id = models.ForeignKey(category_items, on_delete=models.CASCADE)
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=50)
    item_desc = models.TextField()
    item_quantity = models.PositiveIntegerField()
    price = models.FloatField()
    img = models.ImageField(upload_to='items/')

    def __str__(self):
        return self.item_name

    def save(self, *args, **kwargs):
        if self.img:
            # Open the uploaded image
            img = Image.open(self.img)

            # Set the new resolution
            new_width = 500
            new_height = 500
            resized_img = img.resize((new_width, new_height), Image.LANCZOS)

            # Save the resized image back to the model's image field
            buffer = BytesIO()
            resized_img.save(buffer, format='JPEG')  # Change format as needed
            self.img.save(self.img.name, ContentFile(
                buffer.getvalue()), save=False)
        super(product_item, self).save(*args, **kwargs)
