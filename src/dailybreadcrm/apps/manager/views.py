from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.




class DashboardView(TemplateView):
    """
    class which handles the Dashboard operations
    """
    template_name =  "manager/dashboard.html"

    def get(self, request, *args, **kwargs):
        """
        view function which is loaded after successfull login of the admin
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return render(request, self.template_name)