# divvier3b

'Divvier' series objective: Split a collection of numbers (which may 
include replicates) in two, as evenly as possible.

divvier3 approach: Using iterative superset generation approach to make a 
collection of subcollections (supercollection) from which to choose closest-summing pair. 
It will, however, have replicate subcollections, but though 
inefficient, it does allow a deterministic split for the 'Divvier' problem, 
to replace the original tool which used random sampling to process
larger arrays, so could not guarentee an optimal split.

divvier3b: This new version modifies divvier3 Snapshot15 by reverting to my  
original multi-line snippet from its Snapshot1 for making the subcollections 
so that I can do the checks for perfect split and exit early if found, 
without making the whole supercollection list first. 
Also keeps track of subcollection representing best-split-so-far as I go,
so that even if the whole thing is made, it does not have to be traversed again.

In the expectation that it may be more time-efficient on average, I compared its performance to divvier3, and it was (at least) ~8-23 times faster than divvier3 for the 6 ‘simpler’ input   
lists tested and ~13% slower for the 2 ‘more complex’ inputs, 
though the statistical significance of the latter pair was lower/marginal,
as detailed in uploaded subfolder "divvier3 vs divvier3bSnapshot5" 
within uploaded folder "speed comparisons".
I suspect that the 'more complex' inputs are unlikely to have multiple subcollection 
pairs with a difference of 0 from each other (or from the half total)  
and are therefore unlikely to return early after finding an exact split.

Updated executable (for Snapshot5) also uploaded to Releases.