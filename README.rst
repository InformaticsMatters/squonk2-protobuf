Informatics Matters cross-product protocol buffers
==================================================

.. image:: https://badge.fury.io/py/im-protobuf.svg
   :target: https://badge.fury.io/py/im-protobuf
   :alt: PyPI package (latest)

A library of python bindings for protocol buffer definitions used by one or
more products in the Informatics Matters product suite.

The protocol buffers are used across multiple components and languages.
At the outset we anticipate supporting Python, and Java. The root
of all packages is ``src/main`` as required by build tools like ``Gradle``.
From there the directory is ``proto/informaticsmatters`` followed by component
directories or a ``common`` directory. An example protocol message
file might be::

    src/main/proto/informaticsmatters/datamanager/PodMessage.proto

When transmitted on a topic-based messaging service the topic is
the lower-case dot-separated message name relative to ``informaticsmatters``
(excluding the ``Message`` suffix), e.g. ``datamanager.pod``.

Installation (Python)
=====================

The protocol buffers are published on `PyPI`_ and can be installed from
there::

    pip install im-protobuf

.. _PyPI: https://pypi.org/project/im-protobuf

Once installed you can access the protocol buffers with::

    >>> from informaticsmatters.protobuf.datamanager import PodMessage_pb2

Get in touch
============

- Report bugs, suggest features or view the source code `on GitLab`_.

.. _on GitLab: https://github.com/informaticsmatters/protobuf