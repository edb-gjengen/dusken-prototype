#D.U.S.K.E.N

Dårlig Utrustet Studentsystem som Kommer til å Endre Norge.

[![Build Status](https://api.travis-ci.org/neuf/dusken.png)](https://travis-ci.org/neuf/dusken)

You can find the documentation at [dusken.readthedocs.org](http://dusken.readthedocs.org/).

## Installation

### Manual install:
    sudo apt-get install python-virtualenv python-dev postgresql libpq-dev pgadmin3
    cd dusken
    virtualenv --distribute venv
    . venv/bin/activate
    pip install -r requirements.txt
    cd dusken
    cp settings-sample.py settings.py
    # Edit database settings (sqlite3 is easiest to setup, but postgresql is recommended)
    cd ..
    ./manage.py syncdb
    ./manage.py runserver


See [the EDB wiki](http://edb.neuf.no/wiki/index.php/DUSKEN) for more info.

### TODO Vagrant install:

Download latest version of Vagrant from [downloads.vagrantup.com](http://downloads.vagrantup.com/) and then do:

    vagrant plugin install vagrant-salt
    vagrant up
    vagrant ssh


## Generate Fixtures for Test
    python manage.py dumpdata dusken.<model> -n --indent=4 > dusken/fixtures/<model>.json

## Database Diagram Generation

    sudo apt-get install graphviz libgraphviz-dev 
    pip install pygraphviz django-extensions
    python manage.py graph_models -o diagramfile.png dusken


## Design References
A similar data model might allready [exist](http://www.databaseanswers.org/data_models/generic_foundation/index.htm) [out](http://www.databaseanswers.org/data_models/organisations_and_people_and_transactions/index.htm) [there](http://www.databaseanswers.org/data_models/organisations_and_people/index.htm).

## Developer References

* [Tastypie](https://django-tastypie.readthedocs.org/)

