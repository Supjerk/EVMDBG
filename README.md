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
│    ├── debug.py
│    └── util.py
├── .gitignore
├── main.py
└── README.md
```

## TODO
- [x] Implement instruction mutator function
- [x] Implement state in yellow paper
  - [x] Machine Stack
  - [x] Environment
  - [x] World State
  - [x] Global State
- [ ] Break Point
  - [ ] Delete
  - [x] Add
  - [ ] View
- [ ] Tracing
  - [ ] Step
  - [x] Next
  - [x] Continue
  - [x] Run
- [ ] Implement Symobl, Logger more than now
## LICENSE
NONE.
