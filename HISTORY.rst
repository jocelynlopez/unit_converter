Release History
-----------------

0.0.1 (2016-09-21)
+++++++++++++++++++

**Bugfixes**

- Fixed a bug when using ``iter_content`` with ``decode_unicode=True`` for
  streamed bodies would raise ``AttributeError``. This bug was introduced in
  2.11.
- Strip Content-Type and Transfer-Encoding headers from the header block when
  following a redirect that transforms the verb from POST/PUT to GET.*


**Improvements**

- Added support for the ``ALL_PROXY`` environment variable.
- Reject header values that contain leading whitespace or newline characters to
  reduce risk of header smuggling.


**Miscellaneous**

- Updated bundled urllib3 to 1.16.
- Some previous releases accidentally accepted non-strings as acceptable header values. This release does not.

**New Features**

- SOCKS Proxy Support! (requires PySocks; $ pip install requests[socks])

