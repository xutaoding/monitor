from django.views.generic import View
from django.shortcuts import redirect


class ProgramView(View):
    route = 'block_trade/'

    def get(self, request):
        return redirect(self.route)
