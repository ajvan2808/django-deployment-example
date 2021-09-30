# CUSTOM TEMPLATE FILTER

from django import template

register = template.Library()

@register.filter 
def cut(value,arg):
	return value.replace(arg, '')
	# This cut out all values of "arg" from the string

# register.filter('cut', cut)