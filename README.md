# MP3 embedding test

This repository demonstrates a benign CI experiment: a small C++ test executable is compiled and its bytes are appended to an MP3 fixture. The resulting file is published as the teeth-mp3-test Actions artifact.

The embedded program only prints a test message and exits. The workflow does not automatically execute bytes recovered from the MP3.

Place the supplied MP3 fixture at assets/teeth.mp3 before running the workflow.
