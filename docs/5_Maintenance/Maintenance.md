# Maintenance Phase — "Say Hello Software"

## 1. Objective
Maintain and evolve the software after release with minimal risk.

---

## 2. Versioning & Releases
- **Versioning Scheme:** Semantic Versioning (MAJOR.MINOR.PATCH)
- Start at **v1.0.0**
- Example:
  ```bash
  git tag -a v1.0.0 -m "Initial release"
  git push --tags
  ```

---

## 3. Change Control
- Track requests in `docs/CHANGELOG.md` and GitHub Issues.
- For each change:
  1. Update SRS/SDS if behavior changes  
  2. Add/adjust tests first (TDD approach)  
  3. Implement change on a feature branch  
  4. Submit PR → review → merge  

---

## 4. Operational Tasks
- Bug fixes: reproduce → add failing test → fix → close issue  
- Dependency updates: quarterly  
- Documentation: keep README.md and `/docs` synchronized with behavior  

---

## 5. Support & Decommission
- Add troubleshooting FAQ (e.g., Python not found, permission errors)  
- When retiring the project:
  - Archive repository  
  - Keep final runnable artifact and docs  

---

## 6. Backup & Retention
- Store source code in remote Git host (GitHub)  
- Optionally export ZIP with:
  ```
  src/, tests/, docs/, requirements.txt
  ```

---

## 7. Maintenance KPIs
| Metric | Target |
|---------|---------|
| Mean Time to Fix (MTTR) | < 1 day |
| Test Pass Rate | 100% on main branch |
| Documentation Freshness | Updated within 24h of change |
