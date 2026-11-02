# Structured-Output Prompting

## Overview

Structured-output prompting asks a model to return information in a defined format, such as JSON, a Markdown table, or a fixed set of fields. Structure makes outputs easier to inspect, compare, parse, and pass to downstream software.

A prompt that requests JSON is not, by itself, a guarantee of valid JSON. Where a provider offers constrained decoding, tool schemas, or structured response formats, use those features and still validate the result.

## When to use it

Use structured outputs for extraction, classification, data transformation, report generation, and application integrations where downstream code expects predictable fields.

## Worked example: extract a contact record

```text
Extract the contact details from the text below.

Return one JSON object with exactly these keys:
- "name": string or null
- "email": string or null
- "organization": string or null

Rules:
- Use null when a value is not stated.
- Do not guess or normalize an email address.
- Do not include additional keys.
- Return JSON only, without Markdown fences.

Text:
"Contact Maya Chen at maya@example.org. She works with Northstar Labs."
```

Expected shape:

```json
{
  "name": "Maya Chen",
  "email": "maya@example.org",
  "organization": "Northstar Labs"
}
```

## Validation in applications

For production use, define a schema outside the prompt and validate every response. Check required keys, types, allowed values, length limits, and cross-field rules. Reject or safely handle invalid output; do not execute arbitrary model-generated content.

Example JSON Schema fragment:

```json
{
  "type": "object",
  "properties": {
    "name": { "type": ["string", "null"] },
    "email": { "type": ["string", "null"] },
    "organization": { "type": ["string", "null"] }
  },
  "required": ["name", "email", "organization"],
  "additionalProperties": false
}
```

## Limitations and failure modes

- The model may emit malformed JSON or omit required fields.
- A syntactically valid response can still contain incorrect values.
- Ambiguous source text can lead to plausible but unsupported extraction.
- Schemas may not express every business rule.
- Provider-specific constrained-output features differ in supported schema subsets and behavior.

Validate syntax and semantics separately. Never treat successful parsing as proof that the data is true.

## Best practices

1. Define keys, types, allowed values, and missing-value behavior.
2. Keep the schema as simple as the downstream task permits.
3. Use native structured-output or tool-schema features when available.
4. Validate against a machine-readable schema.
5. Add domain checks and source-grounding checks.
6. Test malformed, incomplete, and adversarial inputs.

## Exercise

Design a JSON schema for a task that extracts a product name, quantity, unit price, and currency. Test inputs with a missing quantity, ambiguous currency, and extra unrelated text. Ensure missing or ambiguous values are represented explicitly rather than guessed.

## Further reading

- [OpenAI: Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs)
- [JSON Schema documentation](https://json-schema.org/learn/getting-started-step-by-step)
