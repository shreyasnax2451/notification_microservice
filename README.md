
# Welcome to Notification Microservice 

To manually create a virtualenv on MacOS and Linux:  
 
```  
$ python3 -m venv .venv
```
 
After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```
 
If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```
```
$ python3 -m pip install --upgrade -r requirements.txt
```

```
pip3 freeze > requirements.txt

```
```
To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

```

## Start Celery

```
$ celery -A celery_worker.celery worker -B --concurrency 6 --loglevel=info -Q order_confirmed,order_out_for_delivery,order_shipped,order_delivered,order_returned,order_refunded

```

## Start Flower

```
$ celery -A celery_worker.celery flower --port=5555

```
