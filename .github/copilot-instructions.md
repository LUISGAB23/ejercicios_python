<!-- Auto-generated guidance for AI coding agents. Keep concise and actionable. -->
# Copilot instructions — ejercicios python

This repository is a small collection of single-file Python exercises (learning examples). The goal of this file is to give an AI coding agent immediate, actionable context so suggested edits and PRs are aligned with the project's intent.

- **Big picture:** This workspace contains short, standalone scripts used for teaching/practice. There is no package layout, tests, or CI. Changes should preserve simple runnable behavior and Spanish-language prompts.

```markdown
<!-- Copilot instructions — repository-level guidance for AI coding agents -->

# Copilot instructions — ejercicios python (workspace guidance)

This workspace contains a few small, standalone Python projects used for learning and experimentation. The goal of this file is to give an AI coding agent the exact, actionable context needed to make safe, minimal edits that match the author's intent.

- **Big picture:** two top-level folders:
  - `ejercicios python/Proyectos/` — small single-file scripts for teaching: `Calculo_edad.py`, `suma.py`, `ventana.py`.
  - `Gabriel_project/` — simple project with `main.py` (prints "Hello word"). Changes should remain lightweight and preserve runnable behavior.

- **Key files & examples:**
  - `Proyectos/Calculo_edad.py` — console script; uses `try/except ValueError` for input validation and Spanish prompts (e.g. "Introduce tu edad:").
  - `Proyectos/suma.py` — reads two integers and prints their sum; currently lacks validation — if you add validation, follow `Calculo_edad.py`'s pattern and keep messages in Spanish.
  - `Proyectos/ventana.py` — minimal `tkinter` GUI; keep to standard library only.
  - `Gabriel_project/main.py` — trivial script that prints `Hello word`.

- **How to run (Windows PowerShell):**
  - Console scripts: `python .\Proyectos\Calculo_edad.py` or `python .\Proyectos\suma.py`
  - GUI script: `python .\Proyectos\ventana.py`
  - Run `Gabriel_project`: `python .\Gabriel_project\main.py`
  - Debugging: `python -m pdb .\Proyectos\suma.py` for step-through inspection.

- **Environment & dependencies:**
  - No external packages are required. Code relies on Python standard library (including `tkinter`). Target CPython 3.8+.
  - Do not introduce third-party dependencies or build tooling without explicit user approval.

- **Project conventions & patterns to preserve:**
  - Spanish-language prompts and messages are required for user-facing text.
  - Scripts are intentionally single-file, top-level programs (many do not include `if __name__ == '__main__':`). If refactoring into functions or modules, preserve original entrypoint behavior and compatibility.
  - Keep edits minimal and pedagogical: prefer small helper functions over large refactors.

- **Integration points & cross-file communication:**
  - There are no complex integrations or external services in the workspace — each script is self-contained.
  - Treat `Gabriel_project/main.py` as an independent example; no cross-imports between folders.

- **Developer workflows (what to run / test):**
  - Run scripts directly in PowerShell (examples above). Use `python -m pdb` when stepping through console scripts.
  - If you add tests or support files, include a short `README.md` or top-of-file comment showing how to run them.

- **Safe edits an AI assistant can propose:**
  - Add `if __name__ == '__main__':` guards while preserving behavior.
  - Add input validation to `suma.py` using Spanish error messages and `try/except` as in `Calculo_edad.py`.
  - Extend `ventana.py` with simple `tkinter` widgets (labels/buttons) using only the standard library.

- **Edits to avoid without human approval:**
  - Adding third-party packages or complex build/CI tooling.
  - Large automated refactors that change Spanish prompts, remove original entrypoints, or change intended pedagogical behaviors.

- **When you update this file:**
  - Preserve any existing Spanish guidance and concrete run commands.
  - Keep the file short (20–50 lines) and actionable.

If any of this is unclear or you want the guidance stricter/looser (for example, enforce `__main__` guards or add tests), tell me which rules to change and I will update this file.

```
