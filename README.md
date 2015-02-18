LTSP-Cluster-Panel
==================

Just another LTSP-Cluster-control.
Its a project written in Django, and pretend be a alternative to ltsp-cluster-control software, who is part of LTSP-Cluster Project.

LTSP-Cluster is a set of LTSP plugins and client-side tools that allows you to deploy and centrally manage large numbers of thin-clients. It allows you to run thousands of thin-clients that are able to connect to a load-balanced cluster of GNU/Linux and-or Microsoft Windows terminal servers.
For more information go to https://www.ltsp-cluster.org

Desing
------
Entity Relationship Diagram (ERD):
![alt tag](https://github.com/mboscovich/LTSP-Cluster-Panel/blob/master/Diagrama-ER.png)
(Generated from: http://yuml.me/edit/1373b93a)

How to test
----------
1) Download a copy of code
2) Install django (on apt based systems, just run apt-get install python-django)
3) Go to into main directory of code
4) Execute on a terminal: python manage.py runserver
5) Open in a browser http://127.0.0.1:8000/
6) Join us :D
