
from product.models import Category
from contact.models import Contactinfo

def subject_renderer(request):
    context = {
        'context_categories': Category.objects.filter(is_parent=True),
        "context_contact": Contactinfo.objects.first()
    }
    return context