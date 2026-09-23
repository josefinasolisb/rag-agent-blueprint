# Runbook: deploying a new backend service

> Example document, fictional, written for this repository. Does not
> correspond to any real system.

## When this applies

Any time a new service is deployed to the shared cluster for the first
time, as opposed to a routine update to an existing service.

## Steps

1. Request a dedicated database credential for the service instead of
   reusing a shared one — this keeps future rotations
   (see `runbook_database_credential_rotation.md`) scoped to a single
   consumer.
2. Register the service's healthcheck endpoint with the load balancer
   before routing any traffic to it.
3. Deploy to a single instance first and watch error rate and latency
   for 15 minutes.
4. Gradually shift traffic in 25% increments, watching the same
   dashboards referenced in `runbook_incident_response_high_latency.md`.
5. Once at 100% traffic, document the service's owner and on-call
   rotation in the service catalog.

## Rollback

Any error-rate spike during a traffic shift should trigger an
immediate rollback to 0% traffic for the new service, not a pause.
