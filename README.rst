==========================
rst2pdf.net Client Library
==========================

:Author: Shinya Okano <tokibito@gmail.com>
:PyPI: https://pypi.python.org/pypi/rst2pdf-net-client
:GitHub: https://github.com/tokibito/rst2pdf-net-client

Overview
========

rst2pdf-net-client is a client library for `rst2pdf.net <http://www.rst2pdf.net/>`_ .

The rst2pdf.net is an online service it convert reStructuredText to PDF document using `rst2pdf <https://code.google.com/p/rst2pdf/>`_ .

rst2pdf-net-client includes command line utility. It run without rst2pdf and these dependencies.

Require
=======

* Support Python version is 2.6, 2.7, 3.3, 3.4.
* `requests <https://pypi.python.org/pypi/requests>`_

Install
=======

Install with pip::

  pip install rst2pdf-net-client

Usage
=====

::

  rst2pdf-net < spam.rst > spam.pdf

License
=======

* MIT License
