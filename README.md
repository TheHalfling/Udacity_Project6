# Udacity_Project6

##Summary

This visualization shows baseball player statistics by charting their weight vs height in a bubble chart. 
The resulting bubbles are sized based on the number of careers the player made during their career and colored 
based on the handedness of the player. I included an interactive legend for the handedness to allow the user to filter the data.

##Design

The original design actually plotted height versus number of home runs, but still included the interactive legend 
and coloring for handedness. My initial round of feedback showed that this graph did not really introduce any information
that could not have been assumed since height falls under a bell curve like was shown on the chart. This led to experimenting with adding another dimension to the data resulting int he height vs weight it is now.

The next addition to the chart was some flavor text to introduce the visualization, a rewording of the supporting text for
the interactive legend, and setting the bubbles on the chart to change color when hovered over to make it clear which point 
was being hovered on.

##Feedback

Version 1 Feedback (height vs HR, colored by handedness): Jorge: Graph looks good. There is obviously a bell curve to the data
when presented with all players and height vs. HR. It is hard to see if that bell curve shifts as you go through the handedness
of the player. Perhaps adding a bell curve would help to show that.

Chris: Graph is ok but doesn’t really convey any interesting or unknown information since height is a known bell
curve regardless of what you are charting for the y. Perhaps adding a fourth dimension related to bubble size would
help to convey a more interesting data set.

Version 2 Feedback (height vs weight, colored by handedness, bubble size by HR): Colinearity is not generally explanatory,
In a reasonably fit athlete, height and weight are going to be colinear. Number of home runs may be somewhat correlated with
time, but even then would be interesting to track. Did you look at the data in Excel or R? They may help with testing for colinearity.
From a look and feel point of view, the program worked fine and the dots showed well on both the computer and my phone.

##Resources

Title renaming http://stackoverflow.com/questions/23291200/dimple-js-how-can-i-change-the-labels-of-a-chart-axis-without-changing-the-data

Bubble sizing from http://lornajane.net/posts/2013/dimplejs-bubblescatterplots-and-joind-in-data 

Reset bounds from https://github.com/PMSI-AlignAlytics/dimple/wiki/dimple.axis#ticks 

Interactive legend from http://dimplejs.org/advanced_examples_viewer.html?id=advanced_interactive_legends 

Sorting axis http://stackoverflow.com/questions/24333395/dimple-js-sort-x-axis-data-numerical-not-alphabetical
