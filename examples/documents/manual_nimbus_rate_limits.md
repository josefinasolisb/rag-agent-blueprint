# Manual: API rate limits (fictional product "Nimbus")

> Example document, fictional, written for this repository. Does not
> correspond to any real product.

## Overview

Every Nimbus account has a default API rate limit measured in requests
per minute. Approaching that limit can optionally trigger a usage
alert (see `manual_nimbus_usage_alerts.md`) so you notice before
requests start failing.

## Checking your current limit

The current limit and remaining quota are returned on every API
response as response headers, rather than requiring a separate call.

## Requesting a higher limit

1. Go to **Settings → API → Rate limits**.
2. Submit a request describing the expected traffic pattern.
3. Approved increases apply within one hour; no restart or
   redeployment is required on the caller's side.

## Handling rate-limit responses

When a request is rejected for exceeding the limit, retry after the
wait time indicated in the response instead of retrying immediately —
repeated immediate retries can extend the cooldown window.
