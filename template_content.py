# Define the template content for the list view
def list_content(app_name,model_name):
    list_content = f"""
{{% extends '{app_name}/base.html' %}}

{{% block title %}}
    { model_name } List - Your Website
{{% endblock %}}

{{% block content %}}
    <h1>{ model_name } List</h1>
    <div class="row">
    {{% for data in fields_data %}}
        <div class="col-md-4 mb-3">
            <div class="card">
                <div class="card-body">
                    <h5 class="card-title">{{{{ item.name|title }}}}</h5>
                    {{% for key, value in data.items %}}
                        {{%if key != "id"%}}
                        <p class="card-text"><strong>{{{{ key|title }}}}:</strong> {{{{ value|title }}}} </p>
                        {{%endif%}}
                    {{% endfor %}}
                    <a href="{{% url '{model_name.lower()}_detail' data.id %}}" class="btn btn-primary">Details</a>
                </div>
            </div>
        </div>
    {{% empty %}}
        <div class="col">
            <p>No {{{{ {model_name}|title }}}} found.</p>
        </div>
    {{% endfor %}}
    </div>
{{% endblock %}}
"""
    return list_content

# Define the template content for the create view
def create_content(app_name, model_name):
    create_content = f"""
{{% extends '{app_name}/base.html' %}}

{{% block title %}}
    Create {model_name} - Your Website
{{% endblock %}}

{{% block content %}}
    <h1>Create {model_name}</h1>
    <form method="post">
        {{% csrf_token %}}
        {{% for field in form %}}
            <div class="form-group">
                {{{{ field.label_tag }}}}
                {{{{ field }}}}
                {{% if field.help_text %}}
                    <small>{{ field.help_text }}</small>
                {{% endif %}}
                {{% for error in field.errors %}}
                    <div class="alert alert-danger">{{ error }}</div>
                {{% endfor %}}
            </div>
        {{% endfor %}}
        <button type="submit" class="btn btn-primary">Create</button>
    </form>
{{% endblock %}}
"""
    return create_content

# Define the template content for the detail view
def detail_content(app_name, model_name):
    detail_content = f"""
{{% extends '{app_name}/base.html' %}}

{{% block title %}}
    {{ {model_name}.name }} - Your Website
{{% endblock %}}

{{% block content %}}
    <h1>{{{{ {model_name}.name }}}}</h1>
    <p><strong>Description:</strong> {{{{ {model_name}.description }}}}</p>
    <p><a href="{{% url '{model_name.lower()}_update' {model_name.lower()}.pk %}}" class="btn btn-primary">Edit</a></p>
    <form action="{{% url '{model_name.lower()}_delete' {model_name.lower()}.pk %}}" method="post" style="display: inline;">
        {{% csrf_token %}}
        <button type="submit" class="btn btn-danger">Delete</button>
    </form>
{{% endblock %}}
"""
    return detail_content


# Define the template content for the update view
def update_content(app_name, model_name):
    update_content = f"""
{{% extends '{app_name}/base.html' %}}

{{% block title %}}
    Update {{{{ model_name }}}} - Your Website
{{% endblock %}}

{{% block content %}}
    <h1>Update { model_name }</h1>
    <form method="post">
        {{% csrf_token %}}
        {{% for field in form %}}
            <div class="form-group">
                {{{{ field.label_tag }}}}
                {{{{ field }}}}
                {{% if field.help_text %}}
                    <small>{{{{ field.help_text }}}}</small>
                {{% endif %}}
                {{% for error in field.errors %}}
                    <div class="alert alert-danger">{{{{ error }}}}</div>
                {{% endfor %}}
            </div>
        {{% endfor %}}
        <button type="submit" class="btn btn-primary">Update</button>
    </form>
{{% endblock %}}
"""
    return update_content


# Define the template content for the delete view
def delete_content(app_name, model_name):
    delete_content = f"""
{{% extends '{app_name}/base.html' %}}

{{% block title %}}
    Delete { model_name } - Your Website
{{% endblock %}}

{{% block content %}}
    <h1>Delete { model_name }</h1>
    <p>Are you sure you want to delete this {{{{ {model_name}|lower }}}}? This action cannot be undone.</p>
    <form method="post">
        {{% csrf_token %}}
        <button type="submit" class="btn btn-danger">Confirm Delete</button>
        <a href="{{{{ cancel_url }}}}" class="btn btn-secondary">Cancel</a>
    </form>
{{% endblock %}}
"""
    return delete_content


def base_content():
    base_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{% block title %}}Top Seller {{% endblock %}}</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <!-- jQuery -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <!-- Bootstrap JS -->
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</head>
<body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
        <a class="navbar-brand" href="#">Your Website</a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                </li>
                <!-- Add more navigation items as needed -->
            </ul>
            <!-- Add additional elements to the right side of the navbar -->
        </div>
    </nav>

    <div class="container mt-4">
        {{% block content %}}
        {{% endblock %}}
    </div>
</body>
</html>
"""
    return base_content
