from django import forms
from admin_app.models import product_item, category_items


class category_form(forms.ModelForm):
    class Meta:
        model = category_items
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(self.fields)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control border-2 border-secondary w-75 py-2 px-4 rounded-pill'
            field.widget.attrs['placeholder'] = "Enter "+str(field.label)


class product_form(forms.ModelForm):
    class Meta:
        model = product_item
        fields = "__all__"
