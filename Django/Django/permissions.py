from rest_framework.permissions import BasePermission
from datetime import datetime, timedelta

class RegistedMoreThanAWeekUser(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False
        return bool(user.join_data < (datetime.now().date() - timedelta(days = 7)))

class three_days(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        join_date = user.join_date
        now = datetime.today()
        return now - join_date >= datetime.timedelta(days = 3)