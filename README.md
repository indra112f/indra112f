# Indra Wijaya

Backend engineer focused on developer tooling, automation and CI/CD. I build small, well-tested services and the tooling around them, and I contribute fixes to open-source projects where I can verify the change end to end. I use AI assistants as a tool in that work; everything I submit is reviewed by me and tested locally first.

[coremesh.online](https://coremesh.online) · [instant.coremesh.online](https://instant.coremesh.online)

## Projects

**claimcheck** — fact-checks AI-written drafts against their own sources with an open-weight model (Gemma 4). The evidence quote has to appear word for word in the fetched source, and numbers in the claim have to be in it, so the model can't invent its proof. Standard-library Python, MIT, offline tests.
Repository: [indra112f/claimcheck](https://github.com/indra112f/claimcheck)

**CoreMesh Instant** — fixed-price utility APIs (URL health, TLS and DNS checks, JSON repair, webhook verification, hashing) paid per call over HTTP 402 with USDC on Base. FastAPI, deployed behind nginx with a daily backup and health monitor.
Repository: [indra112f/coremesh-instant](https://github.com/indra112f/coremesh-instant) · Live: [instant.coremesh.online](https://instant.coremesh.online) · [OpenAPI](https://instant.coremesh.online/openapi.json)

**Task Forge** — an internal tool for tracking the open-source issues I work on and running each repository's own tests before anything is submitted.

## Selected contributions

- **Perenna-Labs/perenna-contracts** (Rust, Soroban) — collapsed duplicated event-emit signatures behind one helper ([#140](https://github.com/Perenna-Labs/perenna-contracts/pull/140), merged); return `InvalidTimeRange` instead of a math overflow on bad stream bounds ([#157](https://github.com/Perenna-Labs/perenna-contracts/pull/157), merged); repaired integration regressions after a merge ([#158](https://github.com/Perenna-Labs/perenna-contracts/pull/158), merged)
- **Presago-Labs/presago-contracts** (Rust) — archived stale `issues/issue-*.md` files ([#102](https://github.com/Presago-Labs/presago-contracts/pull/102), merged); retired `ISSUE_DRAFT.md` after the defects it tracked were fixed ([#103](https://github.com/Presago-Labs/presago-contracts/pull/103), merged)
- **Presago-Labs/presago** (JavaScript) — removed an obsolete PowerShell maintenance script and its references ([#132](https://github.com/Presago-Labs/presago/pull/132), merged)
- **BasedHardware/omi** (Python) — authentication on seven `/tools/*` routes of the WHOOP integration ([#21133](https://github.com/BasedHardware/omi/pull/21133), in review)

## Tech

Python, FastAPI, LLM tooling (open-weight models, OpenAI-compatible APIs), Rust (Soroban smart contracts), JavaScript, Shell, Docker, nginx.

## Contact

Open to backend, tooling and CI work, and to open-source collaboration. GitHub issues or discussions on my repositories are the quickest way to reach me.
