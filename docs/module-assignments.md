# Module Assignments

Each member owns one module for the full semester. As new DSA topics are taught,
you upgrade your own module rather than switching — this keeps ownership clear
for grading while covering more concepts as a group.

## Assignments

### 1. Building Search — Carl Davin Ravago
- **Responsibilities:** Search buildings by name; keep results readable.
- **Phase 1 (current):** Linear Search over `campus_locations` array.
- **Planned upgrade:** Binary Search (after sorting) or Hash Map lookup.

### 2. Navigation History — Kyla Pelaez
- **Responsibilities:** Log recent searches; display history to the user.
- **Phase 1 (current):** Fixed-capacity array (5 entries), FIFO eviction when full.
- **Planned upgrade:** Stack (LIFO — matches the DSA topic).

### 3. Building Stats / Filter — Francis Danao
- **Responsibilities:** Count buildings per category; filter by category.
- **Phase 1 (current):** Array aggregation and linear filtering.
- **Planned upgrade:** Hash Map/Dictionary grouping (stretch goal).

### 4. Route Planning — Mateo Orpiana
- **Responsibilities:** Find the shortest path between two buildings; render it on an ASCII campus map.
- **Built:** Full Graph implementation — Dijkstra's shortest path algorithm over a
  campus road-junction graph (`display_route.py`), with multi-hop routing and an
  ASCII map renderer. This is ahead of the Array-phase plan; Graph wasn't covered
  in lectures yet, but the course allows using any taught-or-untaught technique
  to solve a real problem.
- **Note:** uses its own building list/coordinates inside `display_route.py`,
  separate from `database.py`. A few full names differ slightly between the two
  (e.g. "Nursing Department" vs "Nursing and Health Department") — worth
  reconciling so the two stay consistent.


### 5. Directory Sort / Rank — Sherwin Gil
- **Responsibilities:** List buildings sorted by name, ID, or another key.
- **Phase 1 (current):** Array + sorting algorithm (bubble sort with early exit)
  was built and tested on 2026-09-23, but is **missing from the current
  main.py** — no menu item, no function. Likely dropped during the Route
  Planning merge, or sitting unmerged on a branch. See Revisions Log.
- **Planned upgrade:** Binary Search Tree for ranked lookup.


## Notes / Meeting Log

- 08/26/2026 — Group formed
- 08/31/2026 — First online meeting, chose Campus Navigation System, discussed future of project and workflow
- 09/19/2026 — Second online meeting, discussed assignment of modules, Lab Report for Arrays started
- 09/20/2026 — 3/5 Arrays built for Building Search, Navigation History, Building Stats/Filter.
- 09/21/2026 - Expanded database.py campus_locations (5 -> 17)
- 09/30/2026 - Added one missing location to database.py campus_locations (Nursing Department)
- 09/30/2026 - Added workflow text file to guide other group members with handling the repository
- 10/01/2026 - Improved the system's UI (Menus)
- 10/02/2026 - Minor changes to workflow
- 10/03/2026 - Route Planning rebuilt as a full Graph (Dijkstra's shortest path) with ASCII map rendering in display_route.py; module ownership swapped (Route Planning -> Mateo, Directory Sort/Rank -> Sherwin)
- 10/03/2026 - Found 2 regressions during testing: building_stats() crash bug is back, and Directory Sort/Rank is missing from main.py - both logged in Revisions Log, not yet fixed