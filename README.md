# specialDjango

## Context processors

1- Créer la fichier context_processor.py dans le projet
    
    #context_processor.py
    def getdata(self):
        ...
        return data
        
 2- Configuraton
 
    //setting.py
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...

                    'context_processor.getdata',

                ],
            },
        },
    ]
    
  3 - VIEWS.PY
  
    ...
    from django.template import RequestContext
    
    def context(request):
        return render('page.html', context=RequestContext(request))
        
        
4 - Affichage dans page.html







    
  
  
  
