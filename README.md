FetchNovel
==========

Fetch novels from internet.

A renewed version.


Usage
-----

    usage: fetchnovel.py [-h] [-V] [-u | -l] [-v] [-r] [-p PROXY | -n]
                         [source] [tid [tid ...]]

    Fetch novels from Internet, and write into file.

    Available sources:
      bgif2, biquge, dzxsw, feizw, haxtxt, klxsw, lwxs, lwxs520, lwxsw,
      piaotian, piaotiancc, ranwen, shu69, shushu8, sto, ttshuba,
      ttzw, ttzw5, uks5, wodexiaoshuo, xs365, yfzww, yq33, zhaishu8,
      cool18, sdragon, sis, doubangroup, ...

    positional arguments:
      source                download source
      tid                   id for novels to download

    optional arguments:
      -h, --help            show this help message and exit
      -V, --version         show program's version number and exit
      -u, --update          update novels in the database
      -l, --list            list novels in the database
      -v, --verbose         show in more detail
      -r, --refresh         refresh novel in the database
      -p PROXY, --proxy PROXY
                            use specific proxy
      -n, --no-proxy        do not use any proxies


TODO
----

* [ ] Fix cli for SingleNovel
* [x] Use cache in SingleNovel
* [ ] use peewee or sqlalchemy