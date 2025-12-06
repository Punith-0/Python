⏱️ Terminal Stopwatch (Python)

A real-time, keyboard-controlled CLI Stopwatch utility built in Python using low-level runtime libraries for accurate timing, live input handling, and terminal UI control.

This project evolves in three progressive stages:

Core Stopwatch Logic

Lap + Quit Feature

Lap + Quit + Pause + Resume (Final Version)

🛠️ Tech Stack

Python 3.10+

time — real-time execution

msvcrt — OS-level keyboard input (Windows)

ANSI Escape Codes — colored terminal UI

Object-Oriented Design

<h1>Version 1 </h1>

✅ Stage 1 — Core Stopwatch Logic

This is the foundation of the entire project. At this stage, the stopwatch supports:

Features

Countdown timer

Countup timer

Formatted time display (HH:MM:SS)

Graceful handling of Ctrl + C

Clean terminal output using ANSI colors

Core Concepts Used

time.sleep() for real-time ticking

try / except for interrupt handling

Modular class-based design

Terminal formatting

Example Behavior
00:00:10
00:00:09
00:00:08
...
00:00:00
Time’s up!


At this point, the stopwatch is:

✅ Functional
✅ Stable
✅ Real-time
❌ No live keyboard controls yet

<h1>Version 2 </h1>

✅ Stage 2 — Lap + Quit Feature

This stage turns the stopwatch into a true interactive runtime tool.

New Features Added

L → Record Lap

Q → Quit Stopwatch

Live keyboard detection using msvcrt.kbhit()

Non-blocking key reading using msvcrt.getch()

Automatic lap summary printed at exit

Controls
Key	Action
L	Record Lap
Q	Quit Stopwatch
Ctrl + C	Force Stop
Example Output
Lap recorded at 00:00:05
Lap recorded at 00:00:12

Laps recorded:
Lap 1: 00:00:05
Lap 2: 00:00:12

What This Stage Introduces

Real-time event handling

OS-level input detection

Runtime state storage (self.laps)

Safe exit with cleanup

At this stage, the project becomes:

✅ A real CLI utility
✅ Event-driven
✅ Stateful

<h1>Version 3 </h1>

✅ Stage 3 — Lap + Quit + Pause + Resume (Final Version)

This is the full-featured production version of the stopwatch.

New Features Added

P → Pause Stopwatch

R → Resume Stopwatch

Lap recording while running

Controlled CPU usage while paused

Fixed-duration OR infinite countup

Custom handling of invalid keys

Stable cleanup via finally

Final Controls
Key	Action
L	Record Lap
P	Pause
R	Resume
Q	Quit
Ctrl + C	Force Stop
Behavior Highlights

Stopwatch freezes cleanly when paused

Resumes from the exact previous time

Laps only record while running

Invalid key presses show a warning message

Full lap history is always displayed at exit

What This Final Version Represents

Event-driven programming

Runtime state machines

OS-level input control

Real-time loop management

Terminal UI engineering

At this stage, the project is:

✅ A full CLI stopwatch tool
✅ Runtime-controlled
✅ Feature-complete
✅ Resume-ready
✅ System-level Python utility

🚀 Project Highlights

Uses actual runtime libraries

Real-time keyboard interaction (no input() blocking)

ANSI-based terminal UI

Clean exit paths with finally

Multiple development stages clearly structured

Designed like a real system tool, not a toy script

📌 Platform Note

This project uses msvcrt, which is Windows-only

Works best in:

Windows Terminal

Git Bash

Command Prompt