# Claude is not a lawyer

An [Agent Skill](https://agentskills.io) that helps coding agents (Claude Code and others that
read `SKILL.md`) draft the legal documents a software project needs (privacy policy, terms of
service / AGB, imprint / Impressum, cookie policy and consent texts, withdrawal notice /
Widerrufsbelehrung, data processing agreement / AVV) **less badly**.

> **This skill does not make an AI a lawyer.** Asking an LLM to write legal documents is bad
> practice. People do it anyway. This skill reduces the damage. It does not remove the need for
> a qualified lawyer to review everything before it is published or signed.

## What it does differently

1. **Official sources, bundled.** The skill ships a curated library of ~140 sources: the
   actual legal texts on official government portals (EUR-Lex / EU Publications Office,
   gesetze-im-internet.de, RIS, fedlex, legislation.gov.uk, govinfo, US state legislatures) and
   official regulator guidance (EDPB, DSK, ICO, CNIL, FTC, CPPA…). Every entry was fetched and
   checked when the skill was built. The agent must read the provisions it relies on instead of
   answering from memory. If a bundled source has gone stale, the agent says so explicitly and
   searches for a replacement (official sites first), and anything that rests on non-official
   sources or model knowledge is labelled as such.
2. **A relentless interview.** One question at a time, each with a recommended answer and why it
   matters, walking down the decision tree (who you are, where you operate, B2C or B2B, minors,
   payments, data…), in the style of the "grill me" skill. Facts the code can answer are looked
   up, not asked.
3. **Legal Decision Records.** Every fact and decision is written to your repo
   (`docs/legal/records/NNNN-*.md`), similar to ADRs, with status, sources and consequences.
4. **Codebase investigation.** The agent scans dependencies, scripts, cookies/storage, forms,
   schemas and infrastructure to find what the software *actually* does, with `file:line`
   evidence, and reports gaps that a document cannot fix (e.g. analytics loading before consent).
5. **Drafts that defend themselves.** Every document comes with a defense report: each clause,
   why it is there, the pinpoint source (article / section), alternatives rejected, confidence,
   and concrete questions for your lawyer. Drafts carry a DRAFT banner that only you remove,
   after legal review.

## Coverage

| Jurisdiction | Depth |
|---|---|
| EU (GDPR, ePrivacy, consumer rights incl. the 2026 withdrawal function, DSA, EAA, AI Act, …) | full |
| Germany, Austria | full (imprint, AGB, withdrawal, cookies, data protection) |
| Switzerland | full for data protection and e-commerce duties |
| Other EU member states | DPA + legislation portal for all; national specifics for FR, ES, IT, NL, IE |
| United Kingdom | full |
| United States | federal (FTC Act, COPPA, CAN-SPAM, ROSCA, DMCA, E-SIGN) + California and the other comprehensive state privacy laws |

Documents: privacy policy, terms, imprint, cookie policy + consent texts, withdrawal notice +
model form, DPA.

## Install

With the [`skills` CLI](https://github.com/vercel-labs/skills):

```bash
npx skills add zanderhammer/claude-is-not-a-lawyer
```

Or copy `skills/legal-docs/` into your agent's skills folder (for Claude Code:
`~/.claude/skills/legal-docs/` or `<project>/.claude/skills/legal-docs/`).

The helper scripts need Python 3 (standard library only). They are optional: agents without a
shell use their web-fetch tool on the bundled URLs instead.

## Use

Ask your agent, for example:

- "Create a privacy policy and imprint for this project."
- "We're launching paid plans in Germany and Austria. What legal documents do we need?"
- "Update our legal docs, we added PostHog and Stripe."

The agent will show the disclaimer, interview you, write records to `docs/legal/`, investigate
the code, and only then draft documents plus defense reports.

## Keeping the sources fresh

Laws change and government websites move. Check the library:

```bash
python3 skills/legal-docs/scripts/check_sources.py            # all sources
python3 skills/legal-docs/scripts/check_sources.py --file de.md
```

`OK` means the URL works and still contains the expected text. `WARN` means the site blocked
the check, rate-limited it, or couldn't be reached from the network the check ran on (some
government sites don't answer cloud or CI IP ranges), so verify it by hand. `FAIL` means the
source is broken: a dead link or the expected text is gone. Only `FAIL` makes the check exit with
an error. A scheduled GitHub Action runs
the check monthly. See [CONTRIBUTING.md](CONTRIBUTING.md) for how to fix or add sources.

## Disclaimer

This repository and the documents produced with it are not legal advice. The maintainers and the
AI agents using this skill are not your lawyers. Use at your own risk and have every document
reviewed by a qualified lawyer in the relevant jurisdiction(s).

## License

[CC0 1.0 Universal](LICENSE): public domain dedication. Use, copy and adapt it without asking.
