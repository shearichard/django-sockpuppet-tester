# Using django-sockpuppet with Django

Building a Django app which uses django-sockpuppet in place of a conventional react / angular / ember front end.

## Development Notes

### Pipenv/Virtualenv

This project makes use of pipenv so the virtualenv needs to be started in the pipenv way (`pipenv shell`) and there is no `requirements.txt`.


### Running backend locally 

Don't forget when running the dev server you have to enable access from outside the VM by modifying the default binding.

Here's an example of doing that.

```
python manage.py runserver 0.0.0.0:8000
```

