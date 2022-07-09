from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from church_site.views import AdminListView, BaseDetailView, BaseCreateView, BaseUpdateView
from forms.forms import FormCreateForm, TranslationCreateForm
from forms.models import Form, Translation
from shared.views import MgView


class FormsDetailView(View):
    model = Form
    template_name = 'forms/forms-detail.html'
    context_object_name = 'form'
    current_page = 'forms'
    current_translation = None
    translation = None

    def get(self, request, *args, **kwargs):
        form = self.model.objects.filter(slug=kwargs['slug']).first()
        if form:
            if not form.is_active:
                context = {
                    'page_title': f'{form.name} form',
                    'current_page': self.current_page,
                    'form': form,
                }
                if request.htmx:
                    return render(request, 'forms/partials/form-inactive-partial.html', context)
                return render(request, 'forms/form_inactive.html', context)

            if request.GET.get('lang'):
                if request.GET.get('lang') == form.language:
                    self.translation = None
                else:
                    self.translation = form.translations.filter(language=request.GET.get('lang')).first()
                self.current_translation = request.GET.get('lang')

            context = {
                'form': form,
                'translation': self.translation,
                'current_translation': self.current_translation,
                'page_title': f'{form.name} form',
                'current_page': self.current_page,
            }

            if request.htmx:
                return render(request, 'forms/partials/form-card-body-partial.html', context)

            return render(request, self.template_name, context)

        if request.htmx:
            return render(request, 'forms/partials/404-partial.html')
        return render(request, 'forms/404-form.html', {})


class AdminFormListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'forms.view_forms'
    template_name = 'forms/admin-forms-list.html'
    model = Form
    context_object_name = 'forms'
    queryset = Form.objects.all()
    ordering = ['-created_at']
    page_title = 'Forms - Admin'
    current_page = 'admin_forms'
    btn_add_href = reverse_lazy('forms:admin-forms-create')


class AdminFormCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'forms.add_forms'
    model = Form
    template_name = 'admin-form-view.html'
    form_class = FormCreateForm
    page_title = 'New Form - Admin'
    current_page = 'admin_forms'
    btn_back_href = reverse_lazy('forms:admin-forms-list')
    success_url = reverse_lazy('forms:admin-forms-list')


class AdminFormUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'forms.change_forms'
    model = Form
    template_name = 'admin-form-view.html'
    form_class = FormCreateForm
    page_title = 'Update Form - Admin'
    current_page = 'admin_forms'
    btn_back_href = reverse_lazy('forms:admin-forms-list')
    success_url = reverse_lazy('forms:admin-forms-list')


class AdminTranslationListView(PermissionRequiredMixin, AdminListView):
    permission_required = 'forms.view_translation'
    template_name = 'forms/admin-translations-list.html'
    model = Translation
    context_object_name = 'translations'
    ordering = ['-created_at']
    btn_back_href = reverse_lazy('forms:admin-forms-list')
    page_title = 'Translations - Admin'
    current_page = 'admin_forms'

    def get_queryset(self):
        return Translation.objects.filter(form__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Form.objects.filter(slug=self.kwargs['slug']).first()
        context['btn_add_href'] = reverse_lazy('forms:admin-translation-create', kwargs={'slug': self.kwargs['slug']})
        return context


class AdminTranslationCreateView(PermissionRequiredMixin, BaseCreateView):
    permission_required = 'forms.add_translation'
    model = Translation
    template_name = 'admin-form-view.html'
    form_class = TranslationCreateForm
    page_title = 'New Translation - Admin'
    current_page = 'admin_forms'
    btn_back_href = reverse_lazy('forms:admin-forms-list')

    def get_success_url(self):
        return reverse_lazy('forms:admin-forms-detail', kwargs={'slug': self.kwargs['slug']})

    def form_valid(self, form):
        form.instance.form = Form.objects.filter(slug=self.kwargs['slug']).first()
        return super().form_valid(form)


class AdminTranslationUpdateView(PermissionRequiredMixin, BaseUpdateView):
    permission_required = 'forms.change_translation'
    model = Translation
    template_name = 'admin-form-view.html'
    form_class = TranslationCreateForm
    page_title = 'Update Translation - Admin'
    current_page = 'admin_forms'

    def get_success_url(self):
        return reverse_lazy('forms:admin-forms-detail', kwargs={'slug': self.kwargs['slug']})

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['btn_back_href'] = reverse_lazy('forms:admin-forms-detail', kwargs={'slug': self.kwargs['slug']})
        return context
