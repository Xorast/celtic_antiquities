{"filter":false,"title":"views.py","tooltip":"/products/views.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":1,"column":0},"end":{"row":6,"column":67},"action":"insert","lines":["from .models import Product","","# Create your views here.","def all_products(request):","    products = Product.objects.all()","    return render(request, \"products.html\", {\"products\": products})"],"id":2}],[{"start":{"row":7,"column":0},"end":{"row":7,"column":25},"action":"remove","lines":["# Create your views here."],"id":3}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":7,"column":0},"end":{"row":7,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1569205015646,"hash":"2316f4b84135db1f00486c0322066608e9b8de40"}