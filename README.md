For an explanation about the project and the homework, please read the README file inside the module 1 folder.

**short, practical explanation** of each file and whether it should stay.

### `main.tf`

**What it is:**
Terraform file that creates your **GCP bucket and BigQuery dataset**.

**Why it’s needed:**
It proves you completed the **Terraform part** of the homework.

**Keep it?**
✅ Yes — required for submission.

---
Files inside Inside Module 1 folder:

### `.python-version`

**What it is:**
Tells tools like `uv` or `pyenv` which Python version to use.

**Why keep it:**
Makes the project reproducible on another machine.

**Keep?**
✅ Yes

---

### `README.md`

**What it is:**
The explanation of your homework and how to run it.

**Why keep it:**
Required for submission. Reviewers need to understand your work.

**Keep?**
✅ Yes (mandatory)

---

### `ingest_green.py`

**What it is:**
Script that downloads and loads the taxi data into the database.

**Why keep it:**
This is part of the core homework logic.

**Keep?**
✅ Yes (main solution code)

---

### `main.py`

**What it is:**
Your main script (usually used for orchestration or testing logic).

**Why keep it:**
Part of your solution code.

**Keep?**
✅ Yes

---

### `pyproject.toml`

**What it is:**
Configuration file for Python dependencies (used by `uv`).

**Why keep it:**
Defines the environment so others can run your code.

**Keep?**
✅ Yes

---

### `taxi_zone_lookup.csv`

**What it is:**
Small reference dataset with zone names.

**Why keep it:**
Tiny file used in SQL joins; standard in this homework.

**Keep?**
✅ Yes

---

### `uv.lock`

**What it is:**
Lock file with exact dependency versions.

**Why keep it:**
Ensures the environment installs exactly the same packages.

**Keep?**
✅ Yes (good practice)

---

## Thanks!
