# Multimodal Prompting

## Overview

Multimodal prompting supplies or references more than one modality—such as text, images, audio, or video—in a model interaction. Supported inputs and outputs differ substantially across models and product interfaces.

Do not assume that a model can process every modality, file type, resolution, duration, or real-time stream.

## When to use it

Use multimodal prompting when the task genuinely requires cross-modal information, such as describing an image, extracting information from a chart, transcribing audio, or summarizing a supported video input.

## Example: image inspection

```text
Inspect the attached image for visible damage to the package.

Return:
- visible observations;
- location of each observation in the image;
- details that cannot be determined from this image.

Do not infer the package contents or the cause of damage.
Distinguish direct visual observations from interpretation.
```

For audio, specify whether the goal is transcription, speaker diarization, translation, or semantic summary. For video, provide timestamps or sampled frames when the interface requires them.

## Limitations and failure modes

- Small text, low resolution, occlusion, lighting, and image compression can reduce accuracy.
- A model may miss objects or misread charts and diagrams.
- Audio transcription can fail with noise, accents, overlapping speakers, or domain vocabulary.
- Video processing may sample only selected frames and miss events between them.
- Modality support, limits, and preprocessing are provider- and model-specific.

## Best practices

Check current provider documentation for supported formats and limits. Provide task-relevant context without leading the model to a desired conclusion. Ask it to mark uncertainty and avoid inferring unseen details. Verify extracted numbers, text, and safety-critical observations against the original media.

## Exercise

Use a chart image with known values. Ask for the title, axes, units, and three data points. Compare every extracted value with the source chart, then repeat with a compressed image and document the changes in error.

## Further reading

- [OpenAI vision guide](https://platform.openai.com/docs/guides/images-vision)
- [OpenAI audio guide](https://platform.openai.com/docs/guides/audio)
