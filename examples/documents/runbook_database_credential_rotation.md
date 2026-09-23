# Runbook: rotating a database credential

> Example document, fictional, written for this repository. Does not
> correspond to any real system.

## When this applies

When a shared database credential reaches its scheduled rotation cycle,
or is suspected of having been exposed.

## Steps

1. Generate a new credential in the secrets manager.
2. Roll the new credential out to consuming services one at a time,
   verifying the healthcheck after each rollout.
3. Confirm no active connections still use the old credential.
4. Revoke the previous credential.
5. Log the rotation in the team's audit log.

## Rollback

If a service fails its healthcheck after step 2, revert that service to
the previous credential (still valid until step 4) and halt the rollout
until the cause is investigated.
