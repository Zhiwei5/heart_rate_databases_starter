# heart_rate_databases_starter

  This is a back-end server project which using FLASK API. In total, it could achieve two GET and two POST requests. The patients could post thier heartrate monitor on to the web server, get the time when they do the heartrate measurements, get the average heartrate and recerive the heartrate readings from a certain time. The patients are stored in the MangoDB database for later use.
 
 # How to get started

To get started with this sample code, you first need to get the mongodb program running. To do this, simply run 
```
docker run -v $PWD/db:/data/db -p 27017:27017 mongo
```

either on your local machine (if you have docker installed there) or on a virtual machine you have access to where you can first install docker.

:eyes: if you are running your mongodb database on a virtual machine, you need to replace the `connect` URI string in `main.py`. Replace `localhost` with a VM address, like so:

```py
connect("mongodb://vcm-0000.vm.duke.edu:27017/heart_rate_app") # open up connection to db
```

once your database is running and your connection string is set, you can run the starter program by running `heartrate_datebase.py` after activating your `virtualenv` and installing all the dependencies listed in `requirements.txt`.

```
heartrate_datebase.py
```
