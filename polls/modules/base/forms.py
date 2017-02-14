from django import forms


class PollsFormMixin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PollsFormMixin, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if isinstance(field.widget, forms.widgets.TextInput):
                classes = set()

                widget_class = field.widget.attrs.get('class')
                if widget_class:
                    classes = {widget_class.split(' ')}

                classes.add('form-control')
                field.widget.attrs['class'] = ' '.join(classes)
