from docassemble.base.util import defined, value

def _fontawesome_classes(icon, size):
  """Return normalized Font Awesome classes for an icon name or class list."""
  icon_text = str(icon).strip()
  if not icon_text:
    return ""

  tokens = icon_text.split()
  has_fa_class = any(token == "fa" or token.startswith("fa-") for token in tokens)
  has_style_prefix = any(token in {"fas", "far", "fal", "fab", "fat"} for token in tokens)
  size_classes = {"fa-xs", "fa-sm", "fa-lg", "fa-xl", "fa-2xl", "fa-2x", "fa-3x", "fa-4x", "fa-5x", "fa-6x", "fa-7x", "fa-8x", "fa-9x", "fa-10x"}
  has_size_class = any(token in size_classes for token in tokens)

  if has_fa_class or has_style_prefix:
    classes = tokens
  else:
    classes = ["fa", f"fa-{icon_text}"]

  if size and not has_size_class:
    classes.append(f"fa-{size}")

  return " ".join(classes)

def fa_icon(icon, color="primary", color_css=None, size="sm"):
  """
  Return HTML for a font-awesome icon of the specified size and color. You can reference
  a CSS variable (such as Bootstrap theme color) or a true CSS color reference, such as 'blue' or 
  '#DDDDDD'. Defaults to Bootstrap theme color "primary".
  """
  classes = _fontawesome_classes(icon, size)

  if not color and not color_css:
    return ':' + str(icon) + ':' # Default to letting Docassemble handle it
  elif color_css:
    return '<i class="' + classes + '" style="color:' + color_css + ';"></i>'
  else:
    return '<i class="' + classes + '" style="color:var(--' + color + ');"></i>'

def sum_if_defined( *pargs ):
  """
  Return sum of all variables as a comma-separated list. Must put variable names in quotes.
  """
  sum = 0
  for var in pargs:
    if defined(var):
      sum += value(var)
  return sum