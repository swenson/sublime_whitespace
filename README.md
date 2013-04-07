sublime_whitespace
==================

Only trim trailing whitespace on lines that have been edited or are new.

If any string from the `trim_if_present` preferences key is present in a file,
it will strip all white space instead.
For example, I have:

    	"trim_if_present": ["swenson@simple.com", "chris@caswenson.com"],

The easiest way to install this: go to Tools -> New Plugin,
copy the text from the Python file into that new plugin and save it as whatever
you want.

License
-------

All code in this repository, unless otherwise specified, is hereby
licensed under the MIT Public License:

Copyright (c) 2012-2013 Christopher Swenson.

 Permission is hereby granted, free of charge, to any person
 obtaining a copy of this software and associated documentation
 files (the "Software"), to deal in the Software without
 restriction, including without limitation the rights to use,
 copy, modify, merge, publish, distribute, sublicense, and/or sell
 copies of the Software, and to permit persons to whom the
 Software is furnished to do so, subject to the following
 conditions:

 The above copyright notice and this permission notice shall be
 included in all copies or substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
 EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
 OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
 HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
 WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
 FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
 OTHER DEALINGS IN THE SOFTWARE.
