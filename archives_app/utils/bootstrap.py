from django import forms

class BootStrapModelForm(forms.ModelForm):
    # 重写 __init__ 方法，为每个字段添加样式
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段,给每个字段的插件设置
        for _, field in self.fields.items():
            # 字段中有属性,保留原来的属性,没有属性,才增加
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
            else:
                field.widget.attrs = {
                    "class": "form-control",
                }