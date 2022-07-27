from django.template import Library
from django.utils.html import format_html

register = Library()

@register.filter
def author_details(author, current_user):
    # if not isinstance(author, user_model):
    #     # return empty string as safe default
    #     return ""

    if author == current_user:
        return format_html("<strong>me</strong>")

    if author.first_name and author.last_name:
        name = f"{author.first_name} {author.last_name}"
    else:
        name = f"{author.username}"

    if author.email:
        email = author.email
    else:
        email = ""

    html_text = format_html('<a href="mailto:{}">{}</a>', email, name) if email else name

    return html_text

