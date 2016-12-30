from django import forms
import django_couch


class testForm(forms.Form):
    car = forms.CharField(max_length=100)


class postForm(forms.Form):
    author = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=1000)
    type = forms.CharField(max_length=10, widget=forms.HiddenInput(), initial="title")

    def clean_title(self):
        title = self.cleaned_data.get('title')
        view = django_couch.db('db').view('validate/title_validate', key=title).rows

        if view:
            raise forms.ValidationError('This title already exists.')
        else:
            return title


class postEdit(forms.Form):
    author = forms.CharField(max_length=100)
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=1000)
    type = forms.CharField(max_length=10, widget=forms.HiddenInput(), initial="title")


class commentForm(forms.Form):
    #post_id = forms.CharField(max_length=100)
    author = forms.CharField(max_length=100)
    comment = forms.CharField(max_length=1000)
    type = forms.CharField(widget=forms.HiddenInput(), initial="comment")
