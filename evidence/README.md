# evidence/

A staging area. Nothing in here is committed except this file.

A collector puts an artefact somewhere the organisation already keeps such
things — a document store, an evidence platform, a ticket — and writes back two
facts: the URL it now lives at, and the day it was produced. Those two facts go
into the requirement's frontmatter. The artefact does not.

That is deliberate, and it is the reason `.gitignore` excludes everything here.
A committed blob stays reachable by its hash long after it is deleted, the clone
grows without bound, and evidence is the category most likely to hold personal
data — a screenshot of an access review is a list of names. The repository holds
the record that something was proven and where the proof is. It does not hold
the proof.

If you are running a collector locally, this is where its working files land
before they are uploaded. Clear it out afterwards; nothing here is a source of
truth.
