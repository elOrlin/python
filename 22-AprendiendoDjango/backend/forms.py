from django import forms
from django.core import validators

class FormArticle(forms.Form):
    
    title = forms.CharField(
        label = 'Titulo',
        max_length=20,
        required=True,
        widget=forms.TextInput(
            attrs={
                'Placeholder': 'Agregar titulo',
                'class': 'titulo_form_article',
                
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El titulo es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9 ]*$', 'El titulo esta mal formado', 'invalid_title')
        ]
    )
    
    content = forms.CharField(
        label = 'Contenido',
        widget=forms.Textarea,
        validators= [   
                validators.MaxLengthValidator(20, 'Te has pasado, el texto es demasiado grande'), 
            ]
            #attrs={
               # 'Placeholder': 'Agregar contentido',
                #'class': 'contentido_form_article',
                
           #}
    )
    
    content.widget.attrs.update({
        'Placeholder': 'Agregar titulo yaa',
        'class': 'titulo_form_article',
        'id': 'contenido_form'
    })
    
    public_options = [
        (1, 'Si'),
        (0, 'No')
    ]
    
    public = forms.TypedChoiceField(
        label = 'Publicado?',
        choices = public_options
    )