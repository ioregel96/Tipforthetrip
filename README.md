# TipForTheTriTip API Reference
- - -

![salmon](https://user-images.githubusercontent.com/80246961/205195117-03d2da30-4e07-4f3c-b49a-05dafd7a1ce1.jpg)

## Synopsis
Our client, a local entrepreneur named Jesse Baker, is in need of an online platform to help him reach customers and market new products for his ready-to-eat Tri-Tip business. To this end, we are developing an e-commerce web application that will allow potential customers to view products, place orders, read about the history of the business, and learn what makes this particular cut of meat so great. To ensure Jesse can continue to grow his business and benefit from our application long after we have finished it, we are also adding admin functionality to the website. This will allow Jesse to add and adjust product listings and give him access to an owner's panel with tabulated metrics on product sales and an interactive graphing tool to help visualize the popularity of specific products.
- - -

## Developer Instructions:
#### Setup Project Locally
Read the [PROJECTSETUPGUIDE.md](https://github.com/Jaredmbenitez/Tipforthetrip/blob/init-redesign/PROJECTSETUPGUIDE.md) file and follow the steps listed in the document

#### Run Server
 ```python ./manage.py runserver```
 
#### New Django App
```django-admin startapp```

#### New Django Project
```django-admin startproject```

#### Sync Database and Models 
```python ./manage.py makemigrations```
> Note: remember to apply migrations after making them

#### Apply Migrations
```python ./manage.py migrate```
- - -

## Testing
> [Python unittest module](https://docs.djangoproject.com/en/4.1/topics/testing/)
- - -

## Deployment
Deployed on Heroku
- 2 Dyno instances - Hobby tier - 512MB RAM
- 1 PostgreSQL instance - Hobby tier - 10M rows
- - -

### ERD Diagram
![ERD](https://user-images.githubusercontent.com/48226633/205527444-9d7b573e-d024-4de3-8637-10b8ae988e14.png)
- - -
