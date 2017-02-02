from django.template import Template, Library
register = Library()
from profile.models import UserProfile,Event
from datetime import datetime, date , timedelta


@register.inclusion_tag("shared/birthday_aniversary.html" )
def birthday_aniversary_today():
    month = date.today().month
    day = date.today().day
    birthdays = UserProfile.objects.filter(dob__month=month,dob__day=day)
    upcomming_bdays = UserProfile.objects.filter(dob__month=month,dob__day__in=range(day+1,day+30))
    anniversaries = UserProfile.objects.filter(doa__month=month,doa__day=day)
    upcomming_anniversaries = UserProfile.objects.filter(doa__month=month,doa__day__in=range(day+1,day+30))
    ctx = {
            'birthdays':birthdays,
            'upcomming_bdays':upcomming_bdays,
            'anniversaries':anniversaries,
            'upcomming_anniversaries':upcomming_anniversaries
        }
    return ctx

@register.inclusion_tag("shared/events.html" )
def events():
    events = Event.objects.all()
    return {'events':events}