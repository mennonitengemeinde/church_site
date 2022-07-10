from django.views import View


class CoreView(View):
    template_name: str = None
    current_page: str = None
    btn_back_href: str = None
    btn_add_href: str = None

    def get_template_name(self):
        return self.template_name

    def get_current_page(self):
        return self.current_page

    def get_btn_back_href(self):
        return self.btn_back_href

    def get_btn_add_href(self):
        return self.btn_add_href

    def get_context_data(self, **kwargs):
        context = {
            'template_name': self.get_template_name(),
            'current_page': self.get_current_page(),
            'btn_back_href': self.get_btn_back_href(),
            'btn_add_href': self.get_btn_add_href(),
        }
        return context
