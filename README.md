Don't read me, just use it!
===========================

Colorizer have no any configuration options. It is very simple. It accepts some
strings on stdin, and outputs them to the stdout. In the middle, it finds matches
for each given pattern and paint them using some color.

For example, you have python log and want to highlight ERRORS and WARNINGS:

    my-program | colorize ERROR WARNING

That is it!

Also, colorizer understands a python's regexp in the params:

    my-program | colorize '(ERROR|CRITICAL)' WARNING '(INFO|DEBUG)'
