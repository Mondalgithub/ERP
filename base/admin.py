from django.contrib import admin
from .models import CustomUser,Gender,Room, Block, Sharing
# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Gender)
admin.site.register(Room)
admin.site.register(Block)
admin.site.register(Sharing)
