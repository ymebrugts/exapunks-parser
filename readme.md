# EXAPUNKS parser and my solutions
Here is a post describing the binary structure of the solution files with a Kaitai Struct definition:
https://www.reddit.com/r/exapunks/comments/973luq/current_solution_file_format/

With these .py files you can parse the EXAPUNKS solution files.

# How to use
```
pip install kaitaistruct
python .\exapunks_parser.py 
```

# How to compile the parser from scratch
```
Install kaitai through their installer
pip install kaitaistruct
kaitai-struct-compiler -t python exapunks_solution.ksy

python .\exapunks_parser.py
```

