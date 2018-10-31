pgbackup
=======

CLI for backup remote PostgreSQL databse either locally or to S3

Preapring the Development
------------------------
1. Enusre ``pip`` and ``pipenv`` are installed.
2. Clone repository: ``git@github.com:pwinning1991/Python3PostgresBackup.git``
3. ``cd`` into the repositroy.
4. Fetch development dependices ``make install``
5. Activate virutalend: ``pipenv shell``

Usage
-----

Pass in a full databse URL, the storage driver, and the destination

S3 Example w/ bucket name:

::
    $ pgbackup postgre://bob@example.com:5432/db_one --driver s3 backups

Local Example w/ local path

::

    $ pgbackup postgre://bob@example.com:5432/db_one --driver local /var/local/db_one/backups/dump.sql

Running Tests
-------------

Run tests locally using ``make`` if virtualenv is active:

::

     $ make

If virtualend isn't active then use:

::

     4 pipenv run make


