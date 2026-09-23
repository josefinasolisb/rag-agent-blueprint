# Runbook: responding to elevated database latency

> Example document, fictional, written for this repository. Does not
> correspond to any real system.

## When this applies

An on-call alert fires when p95 query latency on the primary database
crosses its threshold for more than five consecutive minutes.

## Steps

1. Check whether a credential rotation is in progress (see
   `runbook_database_credential_rotation.md`) — a rollout that briefly
   doubles active connections is a common false-positive trigger.
2. Confirm the alert against the latency dashboard; rule out a
   single noisy replica before treating it as a primary-wide issue.
3. Check for long-running queries and, if found, identify the
   deploy or feature flag that introduced them.
4. If latency is tied to a specific service, roll that service back to
   its previous version before investigating further.
5. Once latency recovers, keep the incident open for 30 minutes to
   confirm it does not regress before closing it.

## Escalation

If latency has not improved after step 4, escalate to the on-call
database owner instead of continuing to iterate alone.
