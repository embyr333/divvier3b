# divvier3b

'Divvier' series objective: Split a collection of numbers (which may 
include replicates) in two, as evenly as possible.

divvier3 approach: Using iterative superset generation approach to make a 
collection of subcollections from which to choose closest-summing pair. 
It will, however, have replicate subcollections, but though 
inefficient, it does allow a deterministic split for the 'Divvier' problem, 
to replace the original tool which used random sampling to process
larger arrays, so could not guarentee an optimal split.

divvier3b: This new version modifies divvier3 Snapshot15 by reverting to my  
original multi-line snippet from its Snapshot1 for making the subcollections 
so that I can do the checks for perfect split and exit early if found, 
without making the whole subcollections list first. 
Also keeps track of subcollection representing best-split-so-far as I go,
so that even if the whole thing is made, it does not have to be traversed again. 

In the expectation that it may be more time-efficient on average,
I intend to make some comparisons of run speed for various inputs with divvier3.