=============================
django-minibugs
=============================

Minimalistic bugtracker for your django project.

Just add minibugs to your project and debug yor work together with your customer.

No need to add any complex bugtracker and force a non-technician to learn and use it.


Screenshot
-------------

.. image:: https://github.com/mariosgn/django-minibugs/raw/master/minibugs.png
    :alt: Main view
    :align: center

.. image:: https://github.com/mariosgn/django-minibugs/raw/master/minibugs_det.png
    :alt: Single ticket view
    :align: center


.. image:: https://github.com/mariosgn/django-minibugs/raw/master/minibugs.png
    :alt: New ticket form
    :align: center


Documentation
-------------

To be done..

Quickstart
----------

Install and see it running::

    $ virtualenv mbvenv
    $ source mbvenv/bin/activate
    (mbvenv)$ git clone https://github.com/mariosgn/django-minibugs.git
    (mbvenv)$ pip install -r django-minibugs/requirements.txt
    (mbvenv)$ cd django-minibugs/demo
    (mbvenv)$ ./manage.py syncdb
        [..create a superuser too..]
    (mbvenv)$ ./manage.py runserver
    
Use it in your project
----------------------

1. Install it ::

    $ pip install -r django-minibugs/requirements.txt

2. Add ``minibugs`` to ``INSTALLED_APPS``.

3. Add also minibugs urls :: 

    urlpatterns = patterns('',
        #...
        url(r'^bugs/', include('minibugs.urls')),
        #...
    )

Requiremets
-----------

django-bootstrap-form

Tested only on Django 1.7 but it should work also with older versions.


TODO
--------

* add minibugs to pypi
* Add projects groups and permissions
* Recap of the last description while updating a ticket
* Orders and colors in the main table
* Use a different database if needed
