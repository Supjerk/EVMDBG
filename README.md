# EVMDBG
SIMPLE EVM DBG. I'm working on the project with [Code4Block](https://github.com/TEAM-C4B) Team.   
[![Total alerts](https://img.shields.io/lgtm/alerts/g/yunnim/EVMDBG.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/yunnim/EVMDBG/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/yunnim/EVMDBG.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/yunnim/EVMDBG/context:python)

## Repo Tree
currently repository tree.
```
│
├── debug
│    ├── __init__.py
│    ├── disassembler.py
│    ├── exception.py
│    ├── instruction.py
│    ├── opcode.py
│    ├── state.py
│    └── util.py
├── .gitignore
├── main.py
└── README.md
```

## TODO
- [x] Implementation instruction mutator function
- [x] Implementation state in yellow paper
  - [x] Machine Stack
  - [x] Environment
  - [x] World State
  - [x] Global State
- [ ] Break Point
  - Delete
  - Add
  - View
- [ ] Tracing
  - [ ] Step
  - [ ] Next
  - [ ] Continue
  - [ ] Run
## LICENSE
NONE.
