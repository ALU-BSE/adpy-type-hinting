# Bug Hunt: Annotating the Checkout Script

This is a small order-processing script with no type hints. It runs, but it has bugs that a type checker can catch before you ever execute the code. Your job is to annotate it fully, let MyPy do its job, and fix what it finds.

## What you'll practice

- Adding type hints to function parameters, return values, and variables.
- Reading and interpreting MyPy error output.
- Handling an `Optional` return value correctly instead of ignoring it.
- Spotting a function that doesn't return a value on every code path.

## Before you start

Make sure MyPy is installed:

```bash
pip install mypy
```

Confirm it works:

```bash
mypy --version
```

## Instructions

1. Run `python checkout.py` once and note what happens.
2. Add type hints to every function signature (parameters and return type), and to any variable where the type isn't obvious from the right-hand side.
3. Run `mypy checkout.py` and read the errors carefully.
4. For each error, decide whether it's pointing at a real bug in the logic or just a missing annotation. Fix the real bugs. Don't silence an error with `# type: ignore` or `Any` unless you're sure that's the right call.
5. Re-run `mypy checkout.py` until it passes cleanly, then re-run the script itself to confirm it no longer crashes.
6. Be ready to explain, in one sentence per bug, what MyPy caught and why it mattered.

## Come ready to discuss

- What happened the first time you ran the script, before annotating anything?
- Which MyPy error was confusing at first, and what did it turn out to mean?
- Would you have caught these bugs by testing alone, without MyPy? What input would you have needed to try?
