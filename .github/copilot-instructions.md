<!-- AI agent instructions for GTM_PS_BATCH14: a distributed student exercise repository -->
# Copilot / AI Agent Instructions

## Repository Overview

**GTM_PS_BATCH14** is a distributed learning workspace: 30+ contributor folders (e.g., [Swital/](Swital/), [Dhanush/](Dhanush/), [Deepesh/](Deepesh/)) each containing independent Python exercise collections. This is **NOT** a monolithic application—each folder is a student's personal practice space with its own learning goals.

## Critical Before-You-Edit Rules

1. **Never bulk-edit multiple contributor folders** without explicit per-folder rationale and user consent
2. **Preserve student work**: Don't remove or alter solutions unless asked; code quality varies by learning stage
3. **Read-only first**: Open ~5-10 files in a contributor's folder to understand their learning path before suggesting changes
4. **Match existing style**: File naming is inconsistent (`first_program.py`, `First_program.py`, `FirstProgram.py`)—preserve each contributor's conventions to avoid duplicates

## Essential Patterns & Conventions

### File Organization
- **Root level**: Minimal metadata only (`README.md`, root Python examples like [Exceptionhandling.py](Exceptionhandling.py))
- **Per-contributor**: Topic subdirectories like `Python_Loops/`, `Selenium_Code/`, `PythonProgramming/` mixed with flat scripts
- **No dependencies**: Almost all scripts use only Python stdlib; external packages (Selenium) are isolated in contributor folders
- **Text/notes**: `.txt` files mixed in as exercise notes or assignments

### Typical Contributor Folder Structure
- **Organized learner** (e.g., [Swital/](Swital/)): Hierarchical structure (`Python_BasicProg_Practise/`, `Python_OOPS_Programming/`, `Selenium_Programs/`)
- **Linear learner** (e.g., [Dhanush/](Dhanush/)): Flat list of scripts by topic (`Average.py`, `AND Operator.py`, `class1.py`)
- **Hybrid** (e.g., [Deepesh/](Deepesh/)): Mix of flat files and topic folders

### Code Characteristics
- Early scripts: simple syntax (`print()`, operators, loops)
- Later scripts: functions, classes, Selenium automation
- Variable quality: typos, incomplete solutions, exploratory code—all intentional part of learning
- No docstrings or comments in most files (follows tutorial patterns)

## How to Run & Debug

```powershell
# From repo root on Windows
python Dhanush\Average.py

# Debug a single file
python -m pdb Swital\Python_BasicProg_Practise\Variables.py

# Or use VS Code Run/Debug for single files
```

## Safe-Edit Workflow

**Before making ANY change:**
1. Read the contributor's **top 3-4 files** to assess learning level
2. Check for an existing [README.md](README.md) or `.txt` notes in their folder
3. If fixing syntax/typos, confirm it's not an assignment under development
4. Propose small, single-contributor changes with clear learning value

**Acceptable edits:**
- Bug fixes in one contributor's scripts (with explanation of what was wrong)
- Adding minimal docstrings to one contributor's learning files
- Creating a simple `requirements.txt` if adding external packages
- Clarifying exercise instructions in comments

**Escalate to user first:**
- Refactoring across >1 contributor's folder
- Adding dependencies
- Removing or fundamentally restructuring a contributor's work

## Running & Testing

- **No centralized test suite** — each contributor runs their own scripts
- **No build system** — Python 3.x execution only
- **Execution verify**: `python script.py` should complete without import errors or uncaught exceptions

## Examples (Reference in PRs)

```powershell
# Correct path format for windows
python Anshika\First_program.py
python Deepesh\PythonProgramming\loops.py

# Invalid (won't work on Windows)
python Anshika/First_program.py
```

## When to Escalate

- Changing architecture or structure of >2 contributor folders
- Adding project-wide dependencies
- Modifying core files like [README.md](README.md) or [.gitignore](.gitignore)
- Bulk fixes (e.g., "fix all typos in all folders")

---

**Last updated:** January 2026 | **Scope:** Distributed Python learning exercises | **No external dependencies** by default
