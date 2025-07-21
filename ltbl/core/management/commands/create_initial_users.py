from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Group, Permission


class Command(BaseCommand):
    help = "Create initial users and assign them to groups with permissions"

    def handle(self, *args, **kwargs):
        users = [
            {
                "username": "adminuser",
                "password": "adminpass123",
                "email": "admin@example.com",
                "group": "Admin",
                "is_staff": True,
                "is_superuser": True,
            },
            {
                "username": "securityuser",
                "password": "securitypass123",
                "email": "security@example.com",
                "group": "Security",
                "is_staff": True,
                "is_superuser": False,
            },
            {
                "username": "developeruser",
                "password": "devpass123",
                "email": "developer@example.com",
                "group": "Developer",
                "is_staff": True,
                "is_superuser": False,
            },
            {
                "username": "editoruser",
                "password": "editorpass123",
                "email": "editor@example.com",
                "group": "Editor",
                "is_staff": True,
                "is_superuser": False,
            },
            {
                "username": "vieweruser",
                "password": "viewerpass123",
                "email": "viewer@example.com",
                "group": "Viewer",
                "is_staff": False,
                "is_superuser": False,
            },
        ]

        # Assign permissions to groups
        for group_name in ["Security", "Developer", "Editor", "Viewer"]:
            group, _ = Group.objects.get_or_create(name=group_name)
            if group_name == "Security":
                # Can view and change users/groups
                perms = Permission.objects.filter(
                    content_type__app_label="auth",
                    codename__in=[
                        "view_user",
                        "change_user",
                        "view_group",
                        "change_group",
                    ],
                )
                group.permissions.set(perms)
            elif group_name == "Developer":
                # Can add, change, and view all models
                perms = (
                    Permission.objects.filter(codename__startswith="add_") |
                    Permission.objects.filter(codename__startswith="change_") |
                    Permission.objects.filter(codename__startswith="view_")
                )
                group.permissions.set(perms)
            elif group_name == "Editor":
                # Can change and view all models
                perms = Permission.objects.filter(
                    codename__startswith="change_"
                ) | Permission.objects.filter(
                    codename__startswith="view_"
                )
                group.permissions.set(perms)
            elif group_name == "Viewer":
                # Can only view all models
                perms = Permission.objects.filter(codename__startswith="view_")
                group.permissions.set(perms)

        for u in users:
            if not User.objects.filter(username=u["username"]).exists():
                user = User.objects.create_user(
                    username=u["username"],
                    password=u["password"],
                    email=u["email"],
                )
                user.is_staff = u["is_staff"]
                user.is_superuser = u["is_superuser"]
                user.save()
                group, _ = Group.objects.get_or_create(name=u["group"])
                user.groups.add(group)
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Created user {u['username']} and added to "
                        f"group {u['group']}"
                    )
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f"User {u['username']} already exists")
                )

        # To grant permissions to existing users/groups, add logic below.
        # For example:
        # for group in Group.objects.all():
        #     # Ensure group has correct permissions
        #     pass
        #     pass
        #     # Ensure group has correct permissions
        #     pass
        #     pass
        #     pass
