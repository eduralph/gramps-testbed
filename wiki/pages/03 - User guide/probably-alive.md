---
title: Gramps 6.0 Wiki Manual - Probably Alive
categories:
- Documentation
managed: false
source: wiki-scrape
wiki_revid: 119928
wiki_fetched_at: '2026-05-30T11:37:23Z'
---

{{#vardefine:chapter\|7}} {{#vardefine:figure\|0}} The living status of the people in a Gramps database is important when you need to share your data with others, but want to protect the details of those that are alive. It is also employed in some reports. For these reasons, Gramps has some tools to help you determine if someone is alive.

## How does Gramps determine if someone is alive?

![[_media/EditPreferences-Limits-tab-default-60.png|Fig. {{#var:chapter}}.{{#vardefineecho:figure|{{#expr:{{#var:figure}}+1}}}} Menu: "Edit &gt; Preferences..." - "Limits" - tab - defaults]]

A simple way to tell if someone is alive is to see if they have a death event, or a death-related event (such as a burial). However, it is probably true that many people in your database don't have such events, as you may not know any details of their death. If you know someone is dead, it might be a good idea to create a death event. You can also go back and add useful details (such as date and place of death) once that is known. Adding events for people known dead, even if they contain no exact details, is somewhat useful. However, Gramps can also add events with estimated dates (or not) for you (described below).

Requiring a user to manually add a death event to a person (so that they would not be considered alive) would be very tedious ---one would have to enter details on many people. Recall that if someone is considered alive, then their details should be prevented from being shared when exported. Therefore, Gramps has a function that can compute whether someone is probably alive based on their event dates, or their relations with people who may have event dates. For example, if a person doesn't have any evidence of death (such as a death or burial event), then Gramps will check this person's parents, children, siblings, continuously until some evidence is found---or it runs out of connections to check. Using information on typical age and event spans (such as typical age differences among siblings, typical ages of mothers at time of birth, etc.) Gramps can make guesses as to whether a person is alive or dead. As you can imagine, this can be a time-expensive function to execute, but can be quite useful. The values for the typical ages at birth, between generations, etc., can be set in the tab.

The probably alive function can check to see if a person was alive on any specific date, or during a time span. This is used in the [Age on Date](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Age_on_Date) Gramplet. Normally, the system will estimate birth and death events, and see if a date falls between those two.

However, there is one special case: if you are looking for people probably alive *today* and they have a death event, then they are considered dead no matter what (even if the event doesn't have a date). Therefore, you will get different results if you see who was probably alive yesterday (or last year) as compared to who is considered alive today. The reason for this is that if you have a death event, you know that a person died in the past, but you don't know when. If you look to see if a person was alive in the past (yesterday and prior) then you can not say for certain if they were dead then without knowing a death date.

If you want to know the details of why Gramps has determined an individual is alive or dead, you can use the Tool addon to get an explanation. This will show the estimate birth and death dates, and the relationship to someone who has an event date on which these are based.

## Probably Alive Proxy

The first tool is the "Probably Alive" proxy. This is used automatically whenever you export your data to a format that supports the ability to restrict details on living people. The proxy wraps the database in a layer that prevents access to sensitive details of living people, such as their given name, and their events.

## Probably Alive Filter

Today's date is treated specially in the instances of events with no dates, and checking alive status in the past. For example, if a person has a death event with no date, then we know that the person is dead as of today, and always in the future. However, for those functions for which you can check to see if a person was alive on a date in the past, we cannot say if they were alive or dead on that date. So, if you have a death event with no date, and check to see if they were alive just yesterday, Gramps will be unable to determine the alive/dead status.

See:

- [People probably alive filter](wiki:Gramps_6.0_Wiki_Manual_-_Filters#People_probably_alive)

## Calendar Gramplet

See [Calendar](wiki:Gramps_6.0_Wiki_Manual_-_Gramplets#Calendar) gramplet.

## Editing Dates

See [Editing dates](wiki:Gramps_6.0_Wiki_Manual_-_Entering_and_editing_data:_detailed_-_part_1#Editing_dates).

[Category:Documentation](wiki:Category:Documentation)
