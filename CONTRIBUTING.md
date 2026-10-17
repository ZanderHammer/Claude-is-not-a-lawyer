# Contributing

The most valuable contributions are **source fixes**: government sites move, laws get amended,
new laws appear. The skill is only as good as its source library.

## Source library

Files: `skills/legal-docs/references/sources/<jurisdiction>.md`. One entry per source:

```markdown
### DE-DDG — Digitale-Dienste-Gesetz, § 5 Allgemeine Informationspflichten
- URL: https://www.gesetze-im-internet.de/ddg/__5.html
- Tier: T1
- Expect: Allgemeine Informationspflichten
- Also: https://… https://…        (optional: more pinpoint URLs, checked for reachability)
- Bot-protected: yes                (optional: site blocks automated clients)
- CELEX: 32016R0679                 (EU only)
- ELI: eli/cc/2022/491              (Switzerland only)
- Cite as: https://…                (optional: human-facing URL to cite)
- Key provisions: § 5(1) Nr. 1 (…); …
- Used for: imprint, terms
- Notes: …
- Last verified: YYYY-MM-DD
```

Rules:

1. **IDs are stable.** Documents generated with the skill cite them. Never rename or reuse an
   ID. If a law is replaced, add a new entry and note the replacement in the old one.
2. **Tiers** (see `references/workflow/source-policy.md`): T1 official legislation, T2 official
   regulator/government guidance, T3 reputable non-official material (orientation only).
   Prefer T1/T2. Never add commercial policy generators.
3. **`Expect`** must be a short, distinctive phrase that appears on the page as long as the
   page is the right one (a title or heading, not navigation text). The checker searches for it
   case-insensitively.
4. **Key provisions** must be checked against the live text. Do not write them from memory. If
   you are unsure of a pinpoint, cite the section without the sub-number.
5. Update **`Last verified`** whenever you check an entry by hand.
6. For EU law, use the Publications Office URL (`python3 skills/legal-docs/scripts/eurlex.py
   <celex> --latest --url`). For Swiss law, use `fedlex_latest.py`.

## Before opening a pull request

```bash
python3 skills/legal-docs/scripts/check_sources.py --file <changed-file>.md
```

All entries you touched must be `OK`, or `WARN` with `Bot-protected: yes` and a note explaining
how you verified them (e.g. "checked in a browser on YYYY-MM-DD").

## Workflow instructions

Changes to `SKILL.md` and `references/workflow/` change how agents behave. Keep the core
rules intact: disclaimer, sources first, explicit fallback reporting, records, defense reports.
Keep `SKILL.md` short; put detail in `references/`.
