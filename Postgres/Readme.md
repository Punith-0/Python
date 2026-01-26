🐘 Mini PostgreSQL Shell — Built Because I Refused the Easy Path

“I could’ve used psql…
but I chose violence (and learning).”

Hi, I’m Punith 👋
This repo contains a mini PostgreSQL shell written in pure Python using psycopg2.

It started after watching a simple tutorial on connecting Python with PostgreSQL.
My brain said: “nice”
My hands said: “build the whole damn shell yourself”
And here we are.

😤 Hacker Mode: Why This Exists

Normal people:

use tools

Me:

builds tools that already exist so I can understand why they exist

This project is not about convenience.
It’s about control, understanding, and breaking things until they make sense.

No ORM.
No frameworks.
No magic.

Just:

sockets? ❌ (next version maybe 😈)

drivers

cursors

SQL

and emotional damage

🧠 Serious Engineering Goals

This project focuses on real backend fundamentals, not tutorial shortcuts:

database connection lifecycle

cursor behavior

error handling

shell-style command parsing

separating execution from presentation

graceful failure instead of silent death

These are the same ideas used in:

database clients

admin tools

backend services

So yeah… small project, big concepts.

🚀 What This Shell Can Do

Current features:

✅ Connect to PostgreSQL

✅ Execute SQL queries

✅ Display SELECT results

✅ Switch databases using \c dbname

✅ Clear screen (cls / clear)

✅ Clean exit handling

✅ Safe reconnection logic

Basically:

a very tiny, very stubborn cousin of psql

🐸 Meme Section (Very Important)

This project timeline:

“This should take 30 minutes.”

“Why is this not working?”

“Why is this STILL not working?”

“I hate PostgreSQL.”

“Ohhh that’s why.”

“Wait… now something else is broken.”

Repeat until character development is achieved.

Debugging took longer than coding.
As God intended.

⚠️ Production Readiness (or Lack Thereof)

Let’s be clear:

🚨 DO NOT USE THIS IN REAL SYSTEMS 🚨

This is:

not secure

not optimized

not hardened

not battle-tested

It is:

educational

honest

built to learn, not to deploy

If this crashes your database, that’s on you, chief.

🎯 Portfolio Value (Yes, This Matters)

This project demonstrates:

low-level database interaction

system-style thinking

command parsing

error handling

iterative debugging

This is not:

another CRUD app with Flask templates

This is:

tooling-level backend work

Which is exactly what I’m training for.

🧭 Bigger Mission

This shell is just the start.

My long-term goal is to master:

🔹 Data manipulation & analysis

🔹 Backend engineering

🔹 Web dev (Flask / Django)

🔹 Web scraping

🔹 Machine Learning

🔹 Deep Learning

🔹 Systems-level thinking

Not just using libraries…
but understanding how and why things work underneath.

😈 Planned Upgrades (a.k.a. Future Suffering)

Things I plan to add because I hate free time:

 Table formatting with column headers

 Dynamic column width alignment

 Query execution timing

 Transaction commands (BEGIN, COMMIT, ROLLBACK)

 Command history

 CSV export

 More psql-style commands (\dt, \d table, etc.)

Basically turning this into:

“psql but written by a student with something to prove”

🤝 For Fellow Code Warriors

If you are:

tired of surface-level tutorials

interested in backend or systems

willing to struggle for real understanding

Then:

fork it

break it

rebuild it

improve it

Let’s level up the hard way.

🧠 Final Words

This repo is not here to show perfection.
It’s here to show real learning in progress.

I didn’t avoid the hard stuff.
I walked straight into it.

And I plan to keep doing that.

If you’re on the same path —
respect 🤝🔥

— Punith