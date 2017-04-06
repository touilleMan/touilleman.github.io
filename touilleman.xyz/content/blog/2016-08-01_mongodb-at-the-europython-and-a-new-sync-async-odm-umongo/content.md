Title: MongoDB at the EuroPython and a new sync/async ODM: μMongo
Date: 2016-08-01
Category: Python
Tags: python, mongo


Coming back from the [EuroPython](https://ep2016.europython.eu) where I could
share feelings about the MongoDB ODMs in Python. I've learned few things there:


## People only talk about Mongoengine

Mongoengine is the most well known ODM out there, probably because it is one
of the oldest and most starred on Github. Beside it's the only one on the 1st
Google page of a `python mongodb` search.
So the alternatives to Mongoengine seems forgotten even if they are pretty numerous:
[humbledb](https://humbledb.readthedocs.io/en/latest/),
[mongoalchemy](http://www.mongoalchemy.org/),
[minimongo](https://github.com/slacy/minimongo),
[ming](http://ming.readthedocs.io/en/latest/),
[nanomongo](https://github.com/eguven/nanomongo) etc.

My guess is people who come to MongoDB go with the bigger thing, if it's
good they stick with it, if it's bad they don't want to do another poor
choice and start relying on themselves :-(


## People don't like Mongoengine

Asking what people think about Mongoengine was my little funny moment:
First they always complained about how bad it is, then I announced I'm part of
the Mongoengine team and finally I could see people turning white, red or
laughing depending on how deeply they shared there painful relationship
with Mongoengine.

But honestly I can't blame them. I think Mongoengine trouble comes from it
inception: It was created
[a long time ago](https://github.com/MongoEngine/mongoengine/commit/af38a92ec9862a7cf18766acf8a63a7adbcb6d4b)
when MongoDB was just out.

My guess is back in those dark times they was not enough experience with this
tech and the original author wanted to create and ORM for mongo to mimic what
you would do with an SQL database.

For example Mongoengine allows you to add a `reverse_delete_rule` to a
[reference field](http://docs.mongoengine.org/apireference.html#mongoengine.fields.ReferenceField).
This way, if the referenced document is destroyed Mongoengine can update the
reference to null or even do cascade deletion, feels pretty SQL isn't it ?
A bit too much !

The trouble is this operation is not atomic at all given it is done by
Mongoengine on top of a regular pymongo driver (and MongoDB cannot do that
anyway). So you end up with concurrency issues, inconsistent data if your
application stops during the processing of this operation etc.

I intended a talk on the MongoDB Driver during the week, at the end someone asked the
talker what does he think about Mongoengine:

<iframe width="764" height="429" src="https://www.youtube.com/embed/2gee5oUAO14?t=2751" frameborder="0" allowfullscreen></iframe>

In a nutshell: people think of Mongoengine like a way to do SQL stuff in Mongo !

## People think they don't need an ODM (but they do !)

After putting people into embarrassment with my Mongoengine question, I
try to relieve them by asking them about the ODM they use. The answer was
"Nothing, just plain pymongo !" pretty often (the "don't want to two poor
choices in a row" effect I guess).

However, after digging a bit, I realize those people created they own validation
system around pymongo, and so ended up with a custom ODM when their project
grown up and they tried to refactor it...

If you go further in the upper video, that's precisely what says the next
talking person: plenty of people use Mongoengine because they want a way to
validate they documents.


## AsyncIO is "the next big thing"™

The number of talks about asyncIO was crazy high, the nodejs community has
proved Twisted was right a decade ago (well it's not the silver bullet, but
I think it goes along pretty well with MongoDB big data credo). Now 
If you want to do asynchronous mongoDB, [there](https://github.com/mongodb/motor)
[is](https://bitbucket.org/mrdon/asyncio-mongo)
[drivers](https://github.com/twisted/txmongo). But you run short on ODM:
I could only find [motorengine](https://github.com/heynemann/motorengine),
which is a fork of... Mongoengine !


## What's from there ?

- MongoDB is not SQL, you don't want to feel like SQL because it would mean
a big lie behind the scene
- an ODM should gives you object orientation and data validation, nothing more
- Even schema-less, you need to validate what's going into your DB
(think of MongoDB as Python: "this variable *can* be anything but it *wont*
be because otherwise my program will blow up !")
- An async ODM is clearly missing here ;-)

So here is [μMongo](https://github.com/Scille/umongo), a simple ("μ" used to
stand for "micro" but given it is now pretty feature-full it is now only the
letter "mu") MongoDB ODM compatible with the majors drivers (both sync and
async !) and relying on [Marshamllow](http://marshmallow.readthedocs.org/) for
all the validation/serialization stuff (why reinvent the wheel when a first
class library is available ?).