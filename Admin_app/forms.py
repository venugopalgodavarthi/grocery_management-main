from typing import Any
from django import forms
from admin_app.models import product_item, category_items
from PIL import Image


def change_resolution(input_image_path, output_image_path, new_width=500, new_height=500):
    # Open the image
    image = Image.open(input_image_path)

    # Resize the image
    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    # Save the resized image
    resized_image.save(output_image_path)


class category_form(forms.ModelForm):
    class Meta:
        model = category_items
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['Job_role'].widget.attrs.update(
        #     {"rows": "4", "cols": "50"})
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control border-2 border-secondary w-75 py-2 px-4 rounded-pill'
            field.widget.attrs['placeholder'] = "Enter "+str(field.label)


class product_form(forms.ModelForm):
    class Meta:
        model = product_item
        fields = "__all__"
        widgets = {'item_desc': forms.Textarea(
            attrs={"rows": "4", "cols": "50"})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control border-2 border-secondary w-75 py-2 px-4 rounded-pill'
            field.widget.attrs['placeholder'] = "Enter "+str(field.label)
