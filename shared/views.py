from django.views import View


class MgView(View):
    page_title: str = None
    current_page: str = None
    btn_back_href: str = None
    btn_add_href: str = None
