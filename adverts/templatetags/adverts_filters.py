from django import template

register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
    """
        Add new css classes to form field
    """
    class_old = field.field.widget.attrs.get('class', None)
    class_new = class_old + ' ' + css if class_old else css
    return field.as_widget(attrs={"class": class_new})


@register.filter(name='error')
def add_field_warning(field, css='form-control-error'):
    """
    :param field: Form field
    :param css: class name
    :return: Adds css class name to field, if field has errors
    """
    class_ = field.field.widget.attrs.get('class', None)
    if field.errors:
        class_ = class_ + ' ' + css if class_ else css
    return field.as_widget(attrs={'class': class_})
