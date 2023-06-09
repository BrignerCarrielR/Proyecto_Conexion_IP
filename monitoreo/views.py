from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DeleteView, UpdateView

from monitoreo.forms import Switchform
from monitoreo.models import Switch
import ping3


# Create your views here.


class InicioTemplateView(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get("query") or ""
        return context


class List_swicth_View(ListView):
    template_name = "switchs/list_switch.html"
    context_object_name = 'list_swicth'
    model = Switch

    def get_queryset(self):
        queryset = super().get_queryset()
        nombre = self.request.GET.get('nombre')
        ip = self.request.GET.get('ip')
        bloque = self.request.GET.get('bloque')
        estado = self.request.GET.get('estado')
        if nombre:
            queryset = queryset.filter(nombre=nombre)
        if ip:
            queryset = queryset.filter(ip__contains=ip)
        if bloque:
            queryset = queryset.filter(bloque__contains=bloque)
        if estado:
            queryset = queryset.filter(estado__contains=estado)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get("query") or ""
        switch = Switch.objects.all()
        for i in switch:
            resultado = ping3.ping(i.ip)
            if resultado is not None:
                i.estado = True
                print(i.ip, 'Esta disponible...')
            else:
                i.estado = False
                print(i.ip, 'No esta disponible...')
            i.save()
        return context


class New_swicth_View(CreateView):
    template_name = 'switchs/form_switch.html'
    model = Switch
    success_url = reverse_lazy('list_swicth_View')
    form_class = Switchform

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = 'new_swicth_View'
        context['cancelar_url'] = 'list_swicth_View'
        context['data'] = 'Ingresar Nuevo Dispositivo'
        context['action'] = 'add'
        return context


class Update_Switch_View(UpdateView):
    model = Switch
    template_name = "switchs/form_switch.html"
    success_url = reverse_lazy('list_swicth_View')
    form_class = Switchform

    # queryset = Cliente.objects.get(pk=request.GET.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['cancelar_url'] = '/list_swicth_View'
        context['data'] = 'Modificar Dispositivo'
        return context

class Delete_Switch_View(DeleteView):
    model = Switch
    template_name = "switchs/delete_switch.html"
    success_url = reverse_lazy('list_swicth_View')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['action_save'] = self.request.path
        context['cancelar_url'] = '/list_swicth_View'
        return context
