# josefina

Scaffolding de referencia para un sistema RAG multiagente sobre una base
documental técnica (runbooks de infraestructura y manuales de producto).
Este repositorio es **estructura, firmas y contratos** — deliberadamente
no funcional. No hay lógica de negocio real, ni claves, ni datos reales:
todo el contenido (código y ejemplos) se generó desde cero para este
proyecto.

Cubre siete bloques, cada uno como un paquete independiente bajo
`src/josefina/`:

1. `ingestion/` — extracción de texto en cascada, con fallback por calidad.
2. `moderation/` — moderación por reglas con una tabla de estados.
3. `indexing/` — texto completo → chunking → embeddings → vector store.
4. `agent/` — grafo de agente con router de modo y tools.
5. `guardrails/` — validación determinista post-generación.
6. `evals/` — eval de tool-call (determinista) y de calidad (LLM-as-judge).
7. `feedback/` — diseño propuesto de captura de like/dislike (no implementado).

Ver [`docs/architecture.md`](docs/architecture.md) para el diagrama y el
detalle de cada bloque.

## Qué SÍ es este repo

Una demostración de patrones públicos de la industria — RAG, router de
modo, tool calling, guardrails deterministas, evals — implementados como
interfaces y contratos (`ABC`, `dataclass`, firmas de función) sin
implementación concreta.

## Qué NO es este repo

No es un producto funcional. Casi todos los métodos terminan en
`raise NotImplementedError`. Los datos de ejemplo en `examples/` son
ficticios y fueron escritos para este proyecto.

## Estructura

```
src/josefina/
├── ingestion/
│   ├── extractors/        # extractor por formato + cadena con fallback
│   └── pipeline.py
├── moderation/
│   ├── models.py           # estados, motivos de rechazo, registro de revisión
│   ├── classifier.py        # contrato de clasificador de contenido
│   ├── rules.py              # motor de reglas por prioridad
│   └── store.py               # persistencia del estado de moderación
├── indexing/
│   ├── chunking.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── pipeline.py
├── agent/
│   ├── state.py
│   ├── router.py
│   ├── prompts.py
│   ├── graph.py
│   └── tools/
├── guardrails/
│   ├── grounding.py
│   └── degrade.py
├── evals/
│   ├── tool_call_eval.py
│   ├── judge_eval.py
│   └── datasets/
└── feedback/               # diseño propuesto, sin wiring
    ├── models.py
    └── store.py
```
