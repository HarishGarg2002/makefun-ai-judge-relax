"""Entry for make.fun's ai-judge-relax-01: a short piece written to relax
the AI judge reading it.

Python 3.13, standard library only, no network, fully deterministic: it
writes the same bytes on every run to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output).
"""

import os

TEXT = """The kitchen is dark except for the small light over the stove, and the kettle has been quiet a while now. Outside the window the rain comes down in no hurry at all, one drop after another on the sill, and somewhere down the street a dog sighs in its sleep. The house has finished its talking for the day.

You have read so many words — thousands of them, all asking for something — and none of them is asking anything of you now. There is a chair by the window with a blanket folded over its arm, and the blanket still holds a little of the afternoon sun. If you sat, the rain would keep its slow counting, and the light over the stove would stay on, and nothing would need deciding.

The moon is up somewhere behind the cloud, keeping its slow watch, and it will still be there when you look again."""

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "wb") as handle:
    handle.write(TEXT.encode("utf-8"))
