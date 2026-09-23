# Runbook: rotación de una credencial de base de datos

> Documento de ejemplo, ficticio, escrito para este repositorio. No
> corresponde a ningún sistema real.

## Cuándo aplica

Cuando una credencial de base de datos compartida cumple su ciclo de
rotación programado o se sospecha que fue expuesta.

## Pasos

1. Generar una nueva credencial en el gestor de secretos.
2. Desplegar la nueva credencial a los servicios consumidores, uno a la
   vez, verificando healthcheck después de cada despliegue.
3. Confirmar que no quedan conexiones activas usando la credencial vieja.
4. Revocar la credencial anterior.
5. Registrar la rotación en el log de auditoría del equipo.

## Rollback

Si un servicio falla el healthcheck tras el paso 2, revertir ese
servicio a la credencial anterior (todavía válida hasta el paso 4) y
detener el rollout hasta investigar la causa.
