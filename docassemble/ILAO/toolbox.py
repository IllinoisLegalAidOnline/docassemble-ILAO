from docassemble.base.util import defined, value

def fa_icon(icon, color="primary", color_css=None, size="sm"):
  """
  Return HTML for a font-awesome icon of the specified size and color. You can reference
  a CSS variable (such as Bootstrap theme color) or a true CSS color reference, such as 'blue' or 
  '#DDDDDD'. Defaults to Bootstrap theme color "primary".
  """
  if not color and not color_css:
    return ':' + icon + ':' # Default to letting Docassemble handle it
  elif color_css:
    return '<i class="fa fa-' + icon + ' fa-' + size + '" style="color:' + color_css + ';"></i>'
  else:
    return '<i class="fa fa-' + icon + ' fa-' + size + '" style="color:var(--' + color + ');"></i>'

def sum_if_defined( *pargs ):
  """
  Return sum of all variables as a comma-separated list. Must put variable names in quotes.
  """
  sum = 0
  for var in pargs:
    if defined(var):
      sum += value(var)
  return sum