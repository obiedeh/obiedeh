---
name: rag-telemetry-copilot-reviewer
description: Review RAG systems and operations copilots that retrieve over logs, manuals, telemetry, and system state. Use when a new RAG pipeline is being added, when retrieval quality is suspect, when an LLM-based ops copilot is being scoped or extended, when hallucinations are being investigated, when chunking or embedding choices are being made, or when retrieval evaluation is missing. Use this skill before shipping any RAG component that touches operational systems.
---

# RAG and Telemetry Copilot Reviewer

This skill reviews retrieval-augmented and agentic systems that operate over real system state: logs, manuals, telemetry, runbooks, deployment configs. The audience is engineering, not research, so the bar is operational correctness rather than benchmark scores.

A copilot that returns plausible answers from stale or wrong context is worse than no copilot. This skill exists to catch that before it lands.

## When to invoke

- A new RAG pipeline is being added to a service or repo.
- An ops copilot is being scoped, extended, or given new tools.
- Retrieval quality is suspect (the copilot answers confidently but wrongly).
- Chunking, embedding model, or vector store choices are under review.
- Eval coverage for the retrieval system is unclear or missing.
- A retrieval source has been added, removed, or refreshed.

## Review checklist

Walk through every section. Each item produces one of: **OK**, **needs work**, or **blocker**, with a one-line piece of evidence.

### 1. Sources

- Each retrieval source is named and owned (who keeps it fresh).
- Source freshness is measurable (timestamp on chunks, last-indexed date queryable).
- Stale sources have a defined behavior (drop, warn, refuse).
- Source-of-truth conflicts are resolved deterministically (rules documented, not "the model decides").
- No source contains secrets or private telemetry that would leak into responses.

### 2. Chunking and embedding

- Chunk size is justified for the source type (code, logs, prose, tables).
- Chunks include enough surrounding context to be understood standalone.
- Embedding model is named, versioned, and pinned.
- Re-embedding strategy on model or source change is documented.

### 3. Retrieval

- Top-k is justified, not a default 3 or 5.
- Retrieval results include source attribution that flows to the answer layer.
- Hybrid retrieval (lexical + semantic) is considered for structured sources like logs and configs.
- The empty-result case has a defined response — not silent hallucination.

### 4. Answer generation

- The prompt forbids answering when retrieval is empty or low-confidence.
- The prompt requires citing retrieved chunks, not the model's prior.
- Tool calls (if any) are bounded — no unbounded shell, no unsupervised writes.
- Output format is structured enough to parse and audit.

### 5. Evaluation

- A retrieval eval set exists (question → expected source / chunk).
- An answer eval set exists (question → expected correctness, not just similarity).
- Eval runs on every change to chunking, embedding, retrieval, or prompt.
- Hallucination rate is tracked, not assumed low.

### 6. Operational safety

- The copilot is not in a write path to systems it cannot roll back.
- Human-in-the-loop is required for state-changing actions.
- Logs of copilot Q&A are retained for incident review.
- Out-of-scope questions are refused, not answered creatively.

## Output format

Return a categorized report:

```text
RAG Review: <component name>

Blockers:
- <one line, with file or path>

Needs work:
- <one line, with file or path>

OK:
- <short list>

Recommended next change:
- <one specific action, smallest first>
```

## Anti-patterns this skill flags

- "We just use OpenAI embeddings" with no version pin.
- "The LLM will figure out which source is fresher."
- Citation language in the system prompt but no citation enforcement in the output.
- A single eval question demonstrating the system "works."
- Retrieval over production logs without redaction.
- An ops copilot with write access to the systems it reads from.

## What this skill does not do

- It does not run retrieval evals — it asks whether they exist and are honest.
- It does not choose models — it asks whether the choice is justified.
- It does not replace `production-architecture-reviewer` for the surrounding service.
