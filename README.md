# Campus Navigation System

Progressive DSA Application Portfolio — Bicol University Polangui, Computer Engineering.

This project is a lab requirement, not a commercial application. Its purpose is to
demonstrate Data Structures and Algorithms (DSA) concepts through a simple
console-based campus navigation tool, built incrementally as new topics are taught.

## Current Phase: Phase 1 - Arrays

Most modules still use array-based logic. Route Planning jumped ahead to a full
Graph implementation (Dijkstra's shortest path). Later phases will upgrade the
remaining modules to Stack, Tree, and other structures as those topics are
covered in class.

No external dependencies — standard Python 3.10+ (uses `match`/`case`).

## Project Structure

```
campus-navigation-system/
├── main.py                    # Menu + module logic
├── models.py                  # Location class
├── database.py                # campus_locations array
├── display_route.py           # Route Planning - Graph (Dijkstra) + ASCII Map
├── docs/
│   ├── module-assignments.md
|   ├── workflow.txt
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
| Mateo Orpiana | Route Planning | Done (Graph — Dijkstra's shortest path + ASCII map) |
| Sherwin Gil | Directory Sort / Rank | Built, but missing from current main.py — see Revisions Log |

See `docs/module-assignments.md` for responsibilities and DSA concepts per module.

## DSA Concepts Roadmap

- [x] Arrays — Search, logging, aggregation
- [ ] Stack — Navigation History upgrade
- [x] Graph — Route Planning (Dijkstra's shortest path, built ahead of schedule)
- [ ] Sorting / Tree — Directory Sort/Rank (built once, currently missing from main.py — see Revisions Log)
- [ ] Hash Map — Building Stats/Filter upgrade (stretch goal)

Target: 5+ DSA concepts by end of semester, per course rubric.