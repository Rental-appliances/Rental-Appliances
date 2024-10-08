from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Customer)
admin.site.register(models.Admin)
admin.site.register(models.AuthUser)
admin.site.register(models.DeliveryBoy)
admin.site.register(models.Area)
admin.site.register(models.City)
admin.site.register(models.State)
admin.site.register(models.AreaHasDeliveryBoy)
admin.site.register(models.Cart)
admin.site.register(models.Product)
admin.site.register(models.FeedbackRating)
admin.site.register(models.Brand)
admin.site.register(models.Image)
admin.site.register(models.Category)
admin.site.register(models.Offers)
admin.site.register(models.OrderStatus)
admin.site.register(models.ProductHasOffers)
# admin.site.register(models.ProductHasHardwares)
# admin.site.register(models.Hardwares)
# admin.site.register(models.CustomizeHasHardwares)
admin.site.register(models.Customize)
# admin.site.register(models.HardwareDetails)
admin.site.register(models.Order)
admin.site.register(models.Payment)
admin.site.register(models.DeliveryPickup)
admin.site.register(models.ProductHasOrder)
admin.site.register(models.PayBack)
admin.site.register(models.PaymentMethod)

