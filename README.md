# Campus Navigation System

Progressive DSA Application Portfolio — Bicol University Polangui, Computer Engineering.

This project is a lab requirement, not a commercial application. Its purpose is to
demonstrate Data Structures and Algorithms (DSA) concepts through a simple
console-based campus navigation tool, built incrementally as new topics are taught.

## Current Phase: Phase 1 - Arrays

All modules currently use array-based logic. Later phases will upgrade specific
modules to Stack, Graph, and other structures as those topics are covered in class.

No external dependencies — standard Python 3.10+ (uses `match`/`case`).

## Project Structure

```
campus-navigation-system/
├── main.py                    # Menu + module logic
├── models.py                  # Location class
├── database.py                # campus_locations array
├── docs/
│   ├── module-assignments.md
│   ├── lab-reports/           # One per DSA phase/topic
│   └── flowcharts/
└── tests/                     # Sample input/output logs per module
```

## Team

| Member | Module | Status |
|---|---|---|
| Carl Davin Ravago | Building Search | Done (Array) |
| Kyla Pelaez | Navigation History | Done (Array) |
| Francis Danao | Building Stats / Filter | Done (Array) |
| Mateo Orpiana | Route Planning | Pending (Graph) |
| Sherwin Gil | Directory Sort / Rank | Pending (Array → Tree) |

See `docs/module-assignments.md` for responsibilities and DSA concepts per module.

## DSA Concepts Roadmap

- [x] Arrays — Search, logging, aggregation
- [ ] Stack — Navigation History upgrade
- [ ] Graph — Route Planning
- [ ] Sorting / Tree — Directory Sort/Rank
- [ ] Hash Map — Building Stats/Filter upgrade (stretch goal)

Target: 5+ DSA concepts by end of semester, per course rubric.