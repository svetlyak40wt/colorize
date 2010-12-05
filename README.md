Don't read me, just use it!
===========================

Colorizer has no configuration options. It's simple. It reads from stdin, 
and writes to the stdout. In the middle, it finds matches
for each given pattern and paint them using some color.

For example, you have python log and want to highlight ERRORS and WARNINGS:

    my-program | colorize ERROR WARNING

That is it!

Also, colorizer understands Python regexps:

    my-program | colorize '(ERROR|CRITICAL)' WARNING '(INFO|DEBUG)'
