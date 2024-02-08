from django.contrib import admin
from catalog.models import Profile, Plant, Scape, Fish, Invertebrate, TankSize, TankVolume, TankFilter, TankLight, TankCo2, TankSoil, TankHardscape

# Register your models here.

admin.site.register(Profile)
admin.site.register(Plant)
admin.site.register(Scape)
admin.site.register(Fish)
admin.site.register(Invertebrate)
admin.site.register(TankSize)
admin.site.register(TankVolume)
admin.site.register(TankFilter)
admin.site.register(TankLight)
admin.site.register(TankCo2)
admin.site.register(TankSoil)
admin.site.register(TankHardscape)
