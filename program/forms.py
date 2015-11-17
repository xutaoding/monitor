from django import forms


class BlockTradeForm(forms.Form):
    # define yourself Form must associative with `request.GET` or 'request.POST'.
    # to not good for `request.GET`, because of key-value of `GET` method,
    # form fields not match, raise error.
    secu = forms.CharField(max_length=12)
    y = forms.CharField(max_length=10)
    typ = forms.CharField()
    crt = forms.DateTimeField()

    def __init__(self, data=None):
        keys = ['secu', 'y', 'typ', 'crt']
        new_data = {} if data is None else data.copy()

        [new_data.pop(key) for key in data or {} if key not in keys]
        super(BlockTradeForm, self).__init__(new_data)
