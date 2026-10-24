# **TMinusTwelve Architecture**

This file specifies the desired implementation architecture for the TMinusTwelve web application.

## Tech stack

* Client-side language: Typescript.
* Client-side framework: None.
* Server-side language: Python.
* Server-side framework: [Flask](https://flask.palletsprojects.com/en/stable/) and [Jinja](https://jinja.palletsprojects.com/en/stable/templates/).  
* Hosting service: [Google Cloud Run](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service?_gl=1*1ifl6zq*_up*MQ..*_gs*MQ..&gclid=CjwKCAjwxeHWBhBPEiwAiqtQ-WjvmC6p3rp8QPSgz12z-MrA7fBBpJZH1giRiYxndyFrNPL7lUV1JRoCuKEQAvD_BwE&gclsrc=aw.ds).
* Database type: [Google Cloud NDB](https://docs.cloud.google.com/appengine/docs/standard/services/ndb?tab=python).
* API type: RESTful API specified in @openapi/api.yaml.
* Authentication: [Google Sign-in](https://developers.google.com/identity/sign-in/web/sign-in).

## Services

* webserver: Responds to requests for web pages in the UI and serves client-side assets.  
* apiserver: Responds to API requests.

## Authentication

* Each user is identified by their email address.  
* The user's email address is provided by "Google Sign-in" and stored in the flask session cookie.

