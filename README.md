# specialDjango

## Like a article

    from django.http import JsonResponse
    from . import models
    from graphql_relay import from_global_id
    from django.contrib.auth.models import User

    def like(request):
        mylike =''
        mydislike=''
        message =''
        statut = False

        article = request.POST.get('article')
        user = request.POST.get('user')


        articleid = from_global_id(article)
        userid = from_global_id(user)
        articleid = articleid[1]
        userid = userid[1]

        try:
            myuser = User.objects.get(pk=int(userid))
            mylike = models.Likes.objects.get(user = myuser , article__id = articleid )
        except Exception as e:
            mylike = ''

        print("mylike =", mylike)
        try:
            myuser = User.objects.get(pk=int(userid))
            mydislike = models.Dislike.objects.get(user = myuser, article__id = articleid )
        except Exception as e:
            mydislike =''


        if not(mylike):
            try:

                myuser = User.objects.get(pk=int(userid))
                article = models.Articles.objects.get(pk=articleid)
                mylike = models.Likes(user=myuser, article=article)
                mylike.save()
                message ='Ajouté aux articles "J\'aime"'
                statut = True
                if not(not(mydislike )):
                    mydislike.delete()  
            except: 
                pass

        else:
            try:
                mylike.delete()
                message ='Supprimé aux articles "J\'aime"'
                statut = False
            except:
                pass

        data = {
            'statut' : statut,
            'message' : message
        }

        return JsonResponse(data, safe=False)
