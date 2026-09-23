# Manual: configuring webhooks (fictional product "Nimbus")

> Example document, fictional, written for this repository. Does not
> correspond to any real product.

## Overview

Webhooks let Nimbus notify an external URL whenever an event occurs,
instead of requiring the integrating system to poll for changes. This
is one of the two notification channels usage alerts can be routed to
(see `manual_nimbus_usage_alerts.md`).

## Setting up a webhook

1. Go to **Settings → Webhooks**.
2. Add the destination URL and select which event types it should
   receive (usage alerts, account changes, or both).
3. Nimbus sends a test event immediately after saving so you can
   confirm the endpoint responds with a 2xx status.

## Retry behavior

If the destination URL does not respond within 10 seconds, Nimbus
retries the delivery up to 5 times with exponential backoff before
marking the event as failed.

## FAQ

**Can a webhook receive rate-limit events too?** Yes — rate-limit
warnings (see `manual_nimbus_rate_limits.md`) can be routed to the same
webhook as usage alerts.
