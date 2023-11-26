from django import forms
from archives_app.utils.bootstrap import BootStrapModelForm
from .models import Archives

class ArchiveModelForm(BootStrapModelForm):
    # 为每个字段单独定义 CharField 实例
    characteristic = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '4', 'class': 'form-control'})
    )
    effect = forms.CharField(
        widget=forms.Textarea(attrs={'rows': '4', 'class': 'form-control'})
    )

    class Meta:
        model = Archives
        fields = '__all__'
