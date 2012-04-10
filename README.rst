============================================
JSON/RPC 2.0 with Google App Engine (Python)
============================================

Library for JSON/RPC communication with the server interfaces
(http://groups.google.com/group/json-rpc/web/json-rpc-2-0).


Requirements
------------

* Python 2.5.2+ (3.x is not supported!)


Running Tests
-------------

In order to run all functional tests using buildout and nosetest enter the following command::

  $ bin/nosetests -v --with-gae --gae-application=parts/jsonrpc


Uploading and managing
----------------------

To upload application files, run::

  $ ./bin/appcfg update parts/jsonrpc

