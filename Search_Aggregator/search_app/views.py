from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.http import JsonResponse,HttpResponse
import json
import random 
from search_app.models import *
import threading 
import json
import requests
import math
import concurrent.futures
import time
from django.core.paginator import Paginator ,PageNotAnInteger ,EmptyPage
    

class SearchData(View):
    template_name = 'index.html'

    def get(self, request, page=1, search=None):
        search = request.GET.get('search')
        def shop_cluse(search,page): 
            # page_count = requests.get('http://api.shopclues.com/api/v11/search?q={}&z=1&key=d12121c70dda5edfgd1df6633fdb36c0&page'.format(search)) 
            # page_count =  json.loads(page_count.text)
            # for page in range(1,math.ceil(page_count['products_count']/10)):
            search_data = requests.get('http://api.shopclues.com/api/v11/search?q={}&z=1&key=d12121c70dda5edfgd1df6633fdb36c0&page={}'.format(search, page))
            
            search_data =  json.loads(search_data.text)
            for data in search_data['products']:
                try:
                    product , created = ShopCluesProduct.objects.get_or_create(name = data['product'])
                except ShopCluesProduct.MultipleObjectsReturned:
                    ShopCluesProduct.objects.filter(name = data['product'])[0].delete()
                
                if created:
                    product.url = data['product_url']
                    product.image = data['image_url']
                    product.price = data['price']
                    product.save()
                else:
                    any_update = False
                    product.url = data['product_url'] if product.url == data['product_url'] else not any_update
                    product.image = data['image_url'] if product.image == data['image_url'] else not any_update
                    product.price = data['price'] if product.price == data['price'] else not any_update
                    product.save() if any_update else None
                
  
        def paytm_api(search,page):  
            # page_count = requests.get('https://search.paytm.com/v2/search?userQuery={}&page'.format(search)) 
            # page_count =  json.loads(page_count.text)
            # for page in range(1,math.ceil(page_count['total_count']/10)):   
            search_data = requests.post('https://search.paytm.com/v2/search?userQuery={}&page={}'.format(search,page))
            search_data =  json.loads(search_data.text)
            for data in search_data['grid_layout']:
                product , created = PaytmProduct.objects.get_or_create(name = data['name'])
                if created:
                    product.url = data['url']
                    product.image = data['image_url']
                    product.price = data['actual_price']
                    product.save()
                else:
                    any_update = False
                    product.url = data['url'] if product.url == data['url'] else not any_update
                    product.image = data['image_url'] if product.image == data['image_url'] else not any_update
                    product.price = data['actual_price'] if product.price == data['actual_price'] else not any_update
                    product.save() if any_update else None

        # def tata(): 
        #     search_data = requests.get('https://www.tatacliq.com/marketplacewebservices/v2/mpl/products/serpsearch?type=category&channel=mobile&pageSize=20&typeID=al&page=1&searchText=Micromax+TV&isFilter=false&isTextSearch=true',headers = {"Content-Type":"application/json"})
        #     print(search_data)
        #     search_data =  json.loads(search_data.text)
        #     for data in search_data['products']:
                
        #         product , created = TataProduct.objects.get_or_create(name = data['product'])
        #         if created:
        #             product.url = data['product_url']
        #             product.image = data['image_url']
        #             product.price = data['price']
        #             product.save()
        #         else:
        #             product.url = data['product_url']
        #             product.image = data['image_url']
        #             product.price = data['price']
        #             product.save()

        shop_cluse_response = threading.Thread(target = shop_cluse(search,page)) 
        paytm_api__response = threading.Thread(target=paytm_api(search,page)) 
        shop_cluse_response.Daemon= True
        paytm_api__response.Daemon= True
        shop_cluse_response.start()
        paytm_api__response.start()
        paytm = shopclus = ""

        if search is not None:    
            shop_cluse_response.join()
            paytm_api__response.join()
            paytm = PaytmProduct.objects.filter(name__icontains=search)
            shopclus = ShopCluesProduct.objects.filter(name__icontains=search)

        products = []
        for data in paytm:
            products.append(data)
        for data in shopclus:
            products.append(data)
        products = products[:1250]
        paginator = Paginator(products, 50)
        total_pages = paginator.num_pages
        previoue_page =1 if (page-1 if page <= total_pages and  page>=1 else 1) == 0 else page-1 if page<=total_pages and page>=1  else 1
        next_page = page+1 if page < total_pages else total_pages
        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            products = paginator.page(1)
        except EmptyPage:
            products = paginator.page(paginator.num_pages)
        pagination_obj = {'total_pages': range(1, total_pages+1), 'previoue_page': previoue_page,'next_page': next_page}
        return render(request, self.template_name, {"demo": products, "pagination_obj":pagination_obj})





























    # def post(self, request, page=1):
    #     print("post hit..")
    #     search = request.POST.get('search')
    #     paytm = PaytmProduct.objects.filter(name__icontains=search)
    #     shopclus = ShopCluesProduct.objects.filter(name__icontains=search)  
    #     products = []
    #     for data in paytm:
    #         products.append(data)
    #     for data in shopclus:
    #         products.append(data)
    #     paginator = Paginator(products, 50)
    #     total_pages = paginator.num_pages
    #     previoue_page =1 if (page-1 if page <= total_pages and  page>=1 else 1) == 0 else page-1 if page<=total_pages and page>=1  else 1
    #     next_page = page+1 if page < total_pages else total_pages
    #     try:
    #         products = paginator.page(page)
    #     except PageNotAnInteger:
    #         products = paginator.page(1)
    #     except EmptyPage:
    #         products = paginator.page(paginator.num_pages)
    #     pagination_obj = {'total_pages': range(1, total_pages+1), 'previoue_page': previoue_page,'next_page': next_page}
    #     return render(request, self.template_name, {"demo": products, "pagination_obj":pagination_obj})