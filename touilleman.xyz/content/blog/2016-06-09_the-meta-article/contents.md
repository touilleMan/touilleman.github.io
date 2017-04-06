Title: The meta article - Warmup with lektor
Date: 2016-06-09
Category: Misc
Tags: python; misc


This blog aims at writting about my experiences in programming, so what better
start but to talk about my experience building this blog !

First and foremost, _[show me the code](https://github.com/touilleMan/touilleman.xyz)_.

Hearing about Armin "flask" Ronacher's
[new project](https://twitter.com/mitsuhiko/status/678963561285177344),
I figured out lektor was exactly the tool I was looking for.
Beside a young project means [opportunities](https://github.com/lektor/lektor/pull/222)
[to](https://github.com/lektor/lektor-markdown-highlighter/issues/2)
[contribute](https://github.com/lektor/lektor-website/issues/101),
adding your little rocks to the growing mountain is so much rewarding ;-)


Working with lektor feels like flask: you get the concept in a glimpse,
have a working poc in minutes but thanks to it great architecture
there is plugins for basically all your needs.


I have to say this is _really_ impressing for such a young project !

Now for (literally) the big picture:

![you are somewhere here]({attach}blog_schema.png)

This is a pretty classic workflow, a few comments though:

lektor provides [plenty ways to deploy](https://www.getlektor.com/docs/deployment/),
my choice was... none !
Armin [presented lektor](http://lucumr.pocoo.org/2015/12/21/introducing-lektor/)
as a way for him to handle his parents' blog without suffering too much.
Basically he (as the "tech guy") had to configure at first the project (how to
deploy, the css etc.) then he can hand it to his parents who will be able to
create&update posts and deploy inside a CMS gui (the dev lektor server running on
their own computer). Furthermore, they could just throw the lektor project folder
inside their Dropbox and to get their blog saved without hassles !

This is an awesome workflow for non-technical people, but as someone who use
git everyday I want to be able to write an article in a branch, then merge it
to the master and finally have my blog updated once the code is pushed on github...

...wich leads us to [Travis](https://travis-ci.org). I love the way you can
store secret inside the `.travis.yml`.
Travis creates a gpg key for each project and uses it to crypt your data. Of
course only trusted build have access to those data to prevent someone sending
you a PR with `echo $MY_SECRET_VAR` to steal your stuff !

Considering the hosting, I first thought about [github pages](https://pages.github.com/)
but I don't feel comfortable storing my Github credentials within Travis (even
if I could create a token with limited access, the granularity would allow
write access to all my public repos...).

So I head up to [netlify](https://www.netlify.com/), the service seems good,
they put a little token (can't miss it though !) on the right corner but given
the storage is free I would call this an exchange of interests ;-)

I'm less happy with the fact you must use the netlify command to deploy your
stuff on their servers, _sftp cannot beat the swag of a nodejs bloat with a
shiny colored cli I guess..._