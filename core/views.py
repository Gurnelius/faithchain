from django.shortcuts import render

def home(request):
    """
    Renders the home page.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'core/home.html')
