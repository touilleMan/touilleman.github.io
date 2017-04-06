Title: Learning async programming the hard way
Date: 2016-06-13
Category: Python
Tags: python


This weekend, I noticed diesel.io is no longer reachable. I guess it's time to
organize the funerals of this project.

First a word about the dead from it [pypi page](https://pypi.python.org/pypi/diesel/3.0.24):

> diesel is a framework for easily writing reliable and scalable network applications in Python. It uses the greenlet library layered atop asynchronous socket I/O in Python to achieve benefits of both the threaded-style (linear, blocking-ish code flow) and evented-style (no locking, low overhead per connection) concurrency paradigms. It’s design is heavily inspired by the Erlang/OTP platform.

[Announced in 2010](https://www.reddit.com/r/programming/comments/9ndev/announcing_diesel_async_io_in_python_for_the_rest/?),
the project was well received (+500 stars on github) but eventually failed
to make it hole in the crowded world of Python async frameworks.

In late 2013, [Bump](http://bu.mp/), the company that developed diesel for it
own needs, was bought by Google, it products discontinued and team merged.

This put a neat stop to the project, which entered in hibernation:
![diesel's contributions]({attach}diesel_contributions.png)

It's only a year later I got interested by the project.

_Why? Maybe it's because
I've always had a weakness for lost causes_ (to
[paraphrase Rhett Buttler](http://www.imdb.com/title/tt0031381/quotes?item=qt1145061)).

What really caught my eye was diesel offers an implementation of Flask and it
it ecosystem (let aside the extensions making use of the network which
blocking nature couldn't play nice in an async framework).

The drawback, however, was diesel was Python 2 only and, as I stated earlier,
it community was sparse if not vanished.

Given I was having some free time (that's the reason I start researching about
async frameworks in the first place) I choose the hard way: porting the project
to Python 3 !

Who knows ? Maybe seeing someone investing time into there project could
re-motivate it creators, and with some posts&benchmarks on reddit we could
even bring new people in...

Dowski, the maintainer of the project,
[was really friendly and helpful](https://github.com/dieseldev/diesel/issues/97)
and shared my hopes on the project. So I started working on the port, and
a month later the [work was done](https://github.com/dieseldev/diesel/pull/100).

However my attempt to shake the sleeping giant turned short: too few free time,
missing motivation and Diesel4 (the new major version with Python 3 support)
didn't get released on pypi, in fact it didn't even make it way to the master :'-(

Put this way, this seems harsh: I worked hard and no-one will ever use my work
(not even me !). But in fact it's all the opposite !

One of the biggest grieve Armin Ronacher gave to Python3 is the str/bytes separation
which make [porting low level code pretty hard](http://lucumr.pocoo.org/2010/5/25/wsgi-on-python-3/).
Well diesel was full of such things (protocols, transport, socket communication etc.)
so porting the code was far more than just a 2to3 pass, I actually had to
read and understand all the code !

This project gave me the opportunity to go deep into async programming,
to understand the [reactor pattern](https://en.wikipedia.org/wiki/Reactor_pattern)
and [hack into an implementation of it](https://github.com/dieseldev/diesel/blob/diesel4/diesel/core.py),
to discover [greenlet](https://greenlet.readthedocs.io/en/latest/),
to play with the [redis](https://github.com/dieseldev/diesel/blob/diesel4/diesel/protocols/redis.py)
and [mongodb](https://github.com/dieseldev/diesel/blob/diesel4/diesel/protocols/mongodb.py)
protocols, and to discover someone finally did something to replace the
[awful logging module](https://github.com/wearpants/twiggy).

With [asyncio](https://docs.python.org/3/library/asyncio.html) raising as
the new unified standard for async programming in Python, diesel is damn
no matter what. So it's time to move on let it rest in peace, but I would
suggest you anyway [to go pay your respects to it](https://github.com/dieseldev/diesel/tree/diesel4),
may it code teaches you as much as it did to me.

<br/>

PS: After 2 years of inactivity,
[Dowski's blog](http://blog.dowski.com/2015/12/01/making-things/) got a new
entry:

<blockquote>
<p>
 I think it's time to make things again.
</p>
<footer>Dowski</footer>
</blockquote>

Is it really the end of diesel ?