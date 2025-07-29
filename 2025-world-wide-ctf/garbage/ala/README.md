# Aliasing Proplems
Welcome to Aliasing Proplems!

Your goal: read the flag located at /flags/flag.txt while passing the seccomp filter.

Your tools: you can put anything in the src/payload/src/payload.rs file! The workspace will get built and ran in an isolated environment.

Notes:
- Don't get overwhelmed by the amount of files, most are irrelevant.
- `runner.sh` contains some helpful tools. You don't need a Rust toolchain for this challenge! The only thing you need is docker on linux (or WSL).
- You should check by yourself, but I promise the privileged docker is not doing anything malicious: nsjail needs the capabilities to run.
- Flag is not available at build time!
- You might want to start by examining the `magic` and `runtime` crates.
- You might want to change those modules for testing, but these changes are not applicable to the remote.
- To submit your payload.rs, do `./runner.sh submit`.
