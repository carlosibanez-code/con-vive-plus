from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]

        widgets = {
            "name": forms.TextInput(attrs={
                "style": """
                    width: 100%;
                    padding: 12px;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    font-size: 16px;
                    box-sizing: border-box;
                """,
                "placeholder": "Tu nombre"
            }),
            "email": forms.EmailInput(attrs={
                "style": """
                    width: 100%;
                    padding: 12px;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    font-size: 16px;
                    box-sizing: border-box;
                """,
                "placeholder": "Tu email"
            }),
            "message": forms.Textarea(attrs={
                "style": """
                    width: 100%;
                    padding: 12px;
                    border: 1px solid #ccc;
                    border-radius: 8px;
                    font-size: 16px;
                    box-sizing: border-box;
                    min-height: 140px;
                    resize: vertical;
                """,
                "placeholder": "Escribe tu mensaje"
            }),
        }