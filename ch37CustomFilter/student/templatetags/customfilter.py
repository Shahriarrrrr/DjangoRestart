from django import template
register = template.Library()

# #Without Decorator
# def myreplace(value, arg):
#     return value.replace(arg, 'We are')

# register.filter('iamToweare', myreplace)

#Without Decorator
@register.filter(name='iamToweare')
def myreplace(value, arg):
    return value.replace(arg, 'We are')