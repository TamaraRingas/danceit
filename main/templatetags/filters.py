from django import template

register = template.Library()

def addstuff(value):
  return value + 'stuff'

register.filter('addstuff', addstuff)

def embedurl(url):
  identifier = str(url.split('=')[1])
  embedurl = f'https://www.youtube.com/embed/{identifier}'
  return embedurl

register.filter('embedurl', embedurl)
