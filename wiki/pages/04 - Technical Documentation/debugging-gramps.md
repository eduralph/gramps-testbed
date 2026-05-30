---
title: Debugging Gramps
categories:
- Developers/General
- Developers/Reference
- Developers/Tutorials
managed: false
source: wiki-scrape
wiki_revid: 118689
wiki_fetched_at: '2026-05-30T18:10:52Z'
---

An overview on how to debug Gramps.

## Hard crash

When a hard crash occurs, you typically have no idea where the crash occurs. It is important to know the line where the crash occurs. So if you are able to reproduce the crash, restart Gramps with the command:

`python -m trace -t Gramps.py`

This will usually generate vast terminal output and slow the system down for that, so redirecting output to a file is usually good:

`python -m trace -t Gramps.py >/tmp/trace.out`

Then check the file "`/tmp/trace.out`" and save if needed, or redirect to somewhere else in the earlier step.

## Add debug statements

Gramps is run with the optimize flag.

`python -O Gramps.py`

This gives you the option of adding debug statements. You can use the \_\_debug\_\_ variable or the assert statement for this. This allows us to add code to Gramps that will be printed out when Gramps runs without the optimize flag:

`python Gramps.py`

More info: [1](http://docs.python.org/reference/simple_stmts.html#the-assert-statement)

## Use the log infrastructure

Gramps has built in the python log infrastructure. Gramps runs with logging level logging.DEBUG to stderrh.

More info: [Logging system](wiki:Logging_system)

Short: in your code add data to the logger with: log.warning(), log.error(), log.info()...

Start Gramps with the --debug flag:

`python Gramps.py --debug="name_of_the_logger"`

This is useful when working in different parts, adding info output, and selecting on the command line with --debug the logger you want to see output with.

## Use profiling

Gramps has a convenience hook to allow you to do profiling. Profiling gives an overview how many times methods are called in a code fragment and how long each one took. It helps to find performance bottlenecks.

An example usage:

Add at the top of the file you want to use profiling:

`from gramps.gen.utils.debug import profile`

Then, suppose you want to profile a save function on one of the editors. The save is called due to a connect done in the method \_connect_signals. So, change the connect to save to a new method testsave you make:

`#self.define_ok_button(self.top.get_widget("ok"), self.save)`  
`self.define_ok_button(self.top.get_widget("ok"), self.testsave)`

Now add the testsave function as follows, where you use the profile convenience function:

`   def testsave(self, *obj):`  
`       profile(self.save, *obj)`

Then run Gramps, every time you save, the profiler kicks in and prints to command line a report with the time for each function.

So in short: replace the call to a function/method to calling profile with as first parameter the function/method, and other parameters the parameters of the function/method.

That's it.

See also [GEPS_016:_Enhancing_Gramps_Processing_Speed](wiki:GEPS_016:_Enhancing_Gramps_Processing_Speed) for a sample of Profile Analysis.

## Python debugging module

For debugging python code itself you can use the [builtin python debugger (pdb)](https://docs.python.org/3/library/pdb.html)

Include it as a module during startup...

` python3 -m pdb Gramps.py`

This lets you place breakpoint() calls in the code, which then gives you interactive debugging command line in the terminal session.

When it first starts you might need to issue a *c(ontinue)* command to run the code.

## Use the winpdb python debugger

[Winpdb](https://pypi.org/project/winpdb-reborn/) (Ubuntu: sudo apt-get install winpdb) is a graphical interface for the python debugger. Start it with:

`winpdb Gramps.py`

![[_media/Winpdb.png|Winpdb with Gramps loaded]]

Now, in File menu, select 'Open Source', and open the source file you want to debug. Now all debug options are possible. Eg, go to a line in the file with the cursor, and click the *run to line* button. The debugger will run to that point, and left show you all defined local variables with their value, as well as the stack frame.

Try it!

{{-}}

## Use gdb C debugger

With GObject introspection, much more can go wrong on a lower level, causing C errors. For these gdb can be used. You should install some debug libraries like libglib2.0-0-dbg, python-gobject-dbg, ... .

Then, you start in a terminal gdb in the directory where Gramps.py is stored with

`gdb python`

You should see something like:

     GNU gdb (Ubuntu/Linaro 7.2-1ubuntu11) 7.2
     Copyright (C) 2010 Free Software Foundation, Inc.
     License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
     This is free software: you are free to change and redistribute it.
     There is NO WARRANTY, to the extent permitted by law.  Type "show copying"
     and "show warranty" for details.
     This GDB was configured as "x86_64-linux-gnu".
     For bug reporting instructions, please see:
     <http://www.gnu.org/software/gdb/bugs/>...
     Reading symbols from /usr/bin/python...Reading symbols from /usr/lib/debug/usr/bin/python2.7...done.
     done.
     (gdb) 

You just type now:

`run Gramps.py`

and then navigate gramps to the **segmentation fault**. After that, you see something like

`Program received signal SIGSEGV, Segmentation fault.`  
`0x00007ffff5e7226b in g_type_check_value () from /usr/lib/x86_64-linux-gnu/libgobject-2.0.so.0`  
`(gdb)`

Now you request the backtrace, to see the code that leads to the error:

`(gdb) bt`

which will print the backtrace. You are now ready to use your C knowledge to fix the bug!

### Trace GObject/GTK warnings

GTK has several possible warning levels, which might pop up on the terminal, without visible problems in Gramps. To trace these, do the following in the :

`gdb python`

and at the gdb prompt indicate to stop on log output:

`b g_log if log level < 32`  
`r Gramps.py`

Now Gramps will stop on serious messages, and you can use

`bt`

to get a backtrace of the C stack showing where the message originated and what called the function, etc.

You can force a hard crash on warnings by setting G_DEBUG.

For example:

` LC_ALL=C G_DEBUG=fatal-warnings python -m trace -t Gramps.py`

Different values possible: [2](https://developer.gnome.org/glib/2.60/glib-running.html)

### Learn More

To learn more about debugging python and C debugging with gdb, see [3](https://web.archive.org/web/20180806035308/http://grapsus.net:80/blog/post/Low-level-Python-debugging-with-GDB) and [4](https://www.sourceware.org/gdb/onlinedocs/gdb.html).

Learning C tutorials  

The Python language implementation is written in the C programming language.

- [Learn C the free interactive C tutorial.](http://www.learn-c.org/)
- [Learn C The Hard Way](https://learncodethehardway.org/c/) (\$)

[Category:Developers/Reference](wiki:Category:Developers/Reference) [Category:Developers/Tutorials](wiki:Category:Developers/Tutorials) [Category:Developers/General](wiki:Category:Developers/General)
