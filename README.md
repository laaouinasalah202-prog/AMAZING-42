How Git knows what to merge

Git looks at three versions of your code:

The common base (where branches split)

Your branch

The branch you’re merging

It compares how each branch changed from the base.

How Git knows something is not a conflict

If:

You changed one line

The other branch changed a different line

Git says:

“No problem, I’ll include both.”

How Git knows something is a conflict

If:

Both branches changed the same line

And the changes are different

Git says:

“I don’t know which one you want.”

So it marks a conflict.

What Git merges automatically

Git merges automatically when:

Changes are in different files

Changes are in different lines

Both branches made the same change

New files were added (with no name clash)

What Git can’t merge automatically

Git can’t decide when:

The same lines were changed differently

Binary files were changed

A file was renamed on one branch and edited on another (sometimes)
