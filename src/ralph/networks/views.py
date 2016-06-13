from django.utils.translation import ugettext_lazy as _

from ralph.admin import RalphTabularInline
from ralph.admin.m2m import RalphTabularM2MInline
from ralph.admin.views.extra import RalphDetailViewAdmin
from ralph.assets.models.components import Ethernet
from ralph.networks.forms import NetworkForm, NetworkInlineFormset
from ralph.networks.models import Network


class NetworkInline(RalphTabularInline):
    form = NetworkForm
    formset = NetworkInlineFormset
    model = Ethernet
    exclude = ['model']


class NetworkTerminatorReadOnlyInline(RalphTabularM2MInline):
    model = Network
    extra = 0
    show_change_link = True
    verbose_name_plural = _('Terminators of')
    fields = [
        'name', 'address',
    ]

    def get_readonly_fields(self, request, obj=None):
        return self.get_fields(request, obj)

    def has_add_permission(self, request):
        return False


class NetworkView(RalphDetailViewAdmin):
    icon = 'chain'
    name = 'network'
    label = 'Network'
    url_name = 'network'

    inlines = [
        NetworkInline,
    ]


class NetworkWithTerminatorsView(NetworkView):
    inlines = [
        NetworkInline,
        NetworkTerminatorReadOnlyInline,
    ]
