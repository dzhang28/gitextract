# gitextract
A python script to extract git commits which has specific keyword in commit context

# Usage:

```python3 gitextract.py inputfile outputfile keywords```

1. Save git commit history into a file (git.log e.g.)
    git log >git.log
2. Run the script file like following format:
    python3 ./gitextract.py git.log commit.log "risc-v" "riscv"
   All commits with keywords "risc-v" or "riscv" (keyword is case insensitive) would be saved to commit.log.

Please note that each commit is recorded in a separate file as well (with file name tmp-XXX.txt).
