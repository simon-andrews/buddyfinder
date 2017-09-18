buddyfinder
===========

Basically, the idea was that it would be a tool for finding nearby FRC teams. You give it your team number, and some search radius, and it would find all the other FRC teams in that radius.

About half way through making it, I realized that The Blue Alliance already had a tool on their website that did basically everything I wanted.

Stuff that's been implemented
-----------------------------
 * Reading TBA's API to get a list of every FRC team.
 * Serialization of TBA data into Python objects.
 * Calculation of distances between coordinates with the haversine distance formula.
 * Passing of "human readable" addresses from TBA to the Google Maps geocoding API to get coordinates.

Requirements
------------
* Modern version of Python 3 (I tested with 3.5.3)
 * [requests](http://docs.python-requests.org/en/master/)
 * A TBA API key
 * A Google Maps geocoding API key

Is it over?
-----------
![I mean, someday I might finish this off for fun but TBH you should just use TBA.](https://pbs.twimg.com/media/DCUI-0IU0AACb6s.jpg)
