from django.contrib import admin
from home.models import book,author,genre,customer


#admin.site.register(book)
#admin.site.register(author)
#admin.site.register(genre)


@admin.register(book)
class bookadmin(admin.ModelAdmin):
    search_fields=('id','name')
    #fields=[('book_name','date')]
    #note: RelatedFieldListFilter=> applicable only when some fields are related to other tables.
    list_filters=('name','date',('author',admin.RelatedOnlyFieldListFilter))
    list_filters=('name','date','author') 


@admin.register(author)
class authoradmin(admin.ModelAdmin):
    pass 


@admin.register(genre)
class genreadmin(admin.ModelAdmin):
    pass 


@admin.register(customer)
class customeradmin(admin.ModelAdmin):
    pass 