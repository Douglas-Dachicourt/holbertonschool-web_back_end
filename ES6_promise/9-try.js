export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction(), 'Guardrail was processed');
    return queue;
  } catch (error) {
    queue.push(`Error: ${error.message}`, 'Guardrail was processed');
    return queue;
  }
}
