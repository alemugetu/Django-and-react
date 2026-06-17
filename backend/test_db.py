#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.db import connection
from django.contrib.auth.models import User

try:
    # Test connection
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        print("✅ Database Connected Successfully!")
        print(f"\nConnection Details:")
        print(f"  Engine: {connection.settings_dict['ENGINE']}")
        print(f"  Database: {connection.settings_dict['NAME']}")
        
    # Test if tables exist
    user_count = User.objects.count()
    print(f"\n✅ Django ORM Working!")
    print(f"  Users in database: {user_count}")
    print(f"\n✅ All checks passed! Database is ready.")
    
except Exception as e:
    print(f"❌ Database Connection Failed!")
    print(f"Error: {e}")
