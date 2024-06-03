#!/usr/bin/env python3
'''

    Generate views and templates from django models
'''
import os
import sys
import django

from django.apps import apps
from django.conf import settings

if len(sys.argv) < 3:
    print("Usage: pythony auto.py <your_project> <your_app>")
    exit()

# Define the app name and model name from command-line arguments
project_name = sys.argv[1]
app_name = sys.argv[2]

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'{project_name}.settings')
django.setup()
from utils import get_models, generate_views_content, generate_urls, generate_admin_content
from template_content import(
    list_content,
    create_content,
    delete_content,
    detail_content,
    update_content,
    base_content
)

# All Django models
model_names = get_models(app_name=app_name)

for model_name in model_names:

    # Check if the app and model exist
    try:
        apps.get_app_config(app_name)
    except LookupError:
        print(f"The app '{app_name}' does not exist.")
        exit()

    try:
        model = apps.get_model(app_name, model_name)
    except LookupError:
        print(f"The model '{model_name}' does not exist in the app '{app_name}'.")
        exit()

    # Define path to your app's views.py, urls.py and admin.py
    views_file_path = os.path.join(settings.BASE_DIR, app_name, 'views.py')
    urls_file_path = os.path.join(settings.BASE_DIR, app_name, 'urls.py')
    admin_file_path = os.path.join(settings.BASE_DIR, app_name, 'admin.py')

    # Define the CRUD operations
    crud_operations = ['List', 'Create', 'Detail', 'Update', 'Delete']

    # Define the template directory
    template_dir = os.path.join(settings.BASE_DIR, app_name, 'templates', f'{app_name}')


    # Get the views content
    if os.path.exists(views_file_path):
        # Check if the file is empty
        if (os.stat(views_file_path).st_size == 0):
            # Exists but empty
            views_content = generate_views_content(app_name, model_name, is_empty=True)
        else:
            # Exists and not empty
            views_content = generate_views_content(app_name, model_name, is_empty=False)
    else:
        # Does not exist
        views_content = generate_views_content(app_name, model_name, is_empty=True)


    # Get urls.py content
    if os.path.exists(urls_file_path):
        # Check if the file is empty
        if (os.stat(urls_file_path).st_size == 0):
            # Exists but empty
            urls_content = generate_urls(model_name)
        else:
            # Exists and not empty
            urls_content = generate_urls(model_name, False)
    else:
        # Does not exist
        urls_content = generate_urls(model_name)



    # Get admin.py content
    if os.path.exists(admin_file_path):
        # Check if the file is empty
        if (os.stat(admin_file_path).st_size == 0):
            # Exists but empty
            admin_content = generate_admin_content(model_name)
        else:
            # Exists and not empty
            admin_content = generate_admin_content(model_name, False)

    else:
        # Does not exist
        admin_content = generate_admin_content(model_name)


    # Create template directory if it doesn't exist
    os.makedirs(template_dir, exist_ok=True)

    list_template_content = list_content(app_name, model_name)
    create_template_content = create_content(app_name, model_name)
    detail_template_content = detail_content(app_name, model_name)
    delete_template_content = delete_content(app_name, model_name)
    update_template_content = update_content(app_name, model_name)
    base_template_content = base_content()
    # Generate templates for CRUD operations
    for operation in crud_operations:
        template_name = f"{model_name.lower()}_{operation.lower()}.html"
        template_file_path = os.path.join(template_dir, template_name)
        with open(template_file_path, 'w') as file:
            if operation == 'List':
                file.write(list_template_content)
            if operation == 'Create':
                file.write(create_template_content)
            elif operation == 'Detail':
                file.write(detail_template_content)
            elif operation == 'Update':
                file.write(update_template_content)
            elif operation == 'Delete':
                file.write(delete_template_content)
            print(f"Generated templates: {template_file_path}")

    # Generate base template
    template_name = "base.html"
    template_file_path = os.path.join(template_dir, template_name)
    with open(template_file_path, 'w') as file:
        file.write(base_template_content)
        print(f"Generated templates: {template_file_path}")


    # Write content to views.py and urls.py
    with open(views_file_path, 'a') as f:
        f.write(views_content)

    with open(urls_file_path, 'a') as f:
        f.write(urls_content)

    print("CRUD operations generated successfully!")


    # Write content to admin.py
    with open(admin_file_path, 'a') as f:
        f.write(admin_content)

    print("Admin site registration completed successfully!")