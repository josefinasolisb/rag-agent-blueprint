# Datasets de eval

Carpeta destinada a casos de prueba **ficticios y curados a mano** para
`tool_call_eval.py` y `judge_eval.py`. No debe contener trazas reales de
usuarios ni datos de producción — solo ejemplos escritos para este
repositorio, en el mismo espíritu que `examples/`.

Formato esperado (a definir al implementar):
- Un archivo por caso o un JSONL con una fila por turno.
- Cada caso referencia un `turn_id`, un transcript ficticio, y (según el
  eval) la tool esperada o la ruta a un rubric en `docs/`.
