from django.contrib import admin
from .models import Profile, Result

# Register your models here.

# admin.site.register(Profile)
# admin.site.register(Result)


"""Uporer method sudhi single data show kortesilo but amr pura table
er sob e jodi delhte chai, seijnno ami class declare kore ki ki chacchi seta tuple akare deye
tarpor dekhacchi"""
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'roll', 'city')


#Decorator use koreo register kora jayh
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('course', 'marks')


admin.site.register(Profile, ProfileAdmin)