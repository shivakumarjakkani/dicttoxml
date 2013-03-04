from distutils.core import setup

version = '0.91'

setup(
    name = 'dicttoxml',
    version = version,
    description = 'Converts a native Python dictionary into an XML string.',
    long_description = """* Supports item (`int`, `float`, `bool`, `str`, `unicode`, `datetime`, `none`) and collection (`list`, `set`, `tuple` and `dict`) data types with arbitrary nesting for the collections. Items with a `datetime` type are converted to ISO format strings. Items with a `none` type become empty XML elements.

* The root object passed into the `dicttoxml` function can be any of the supported data types.

* To satisfy XML syntax, the method wraps all the dict keys/elements and values in a `<root> ... </root>` element. However, this can be disabled to create XML snippets.

* For lists of items, if each item is also a collection data type (`lists`, `dict`), the elements of that item are wrapped in a generic `<item> ... </item>` element.

* Elements with an item data type (`int`, `float`, `bool`, `str`, `datetime`, `unicode`) include a `type` attribute with the data type. Note: `datetime` data types are converted into ISO format strings, and `unicode` and `datetime` data types get a `str` attribute.

* Elements with an unsupported data type raise a TypeError exception.
    """,
    author = 'Ryan McGreal',
    author_email = 'ryan@quandyfactory.com',
    license = 'GNU General Public Licence, Version 2',
    url = 'https://github.com/quandyfactory/dict2xml',
    py_modules = ['dicttoxml'],
    download_url = 'https://github.com/quandyfactory/dict2xml/blob/master/dist/dicttoxml-%s.tar.gz?raw=true' % (version),
)
