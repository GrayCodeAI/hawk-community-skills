---
name: ghcp-resemble-detect-skill
description: Deepfake detection and media safety — detect AI-generated audio, images,
  video, and text, trace synthesis sources, apply watermarks, verify speaker identity,
  and analyze media intelligence using Re...
license: Apache-2.0
tags:
- general
compatibility: Requires a Resemble AI API key (https://app.resemble.ai) set as RESEMBLE_API_KEY.
  All media must be accessible via public HTTPS URLs — local file paths are not supported
  except for text detection.
---

## Red Flags — Stop and Reassess

- **Declaring authenticity without a detection result** — Never say media is real or fake based on visual/auditory inspection alone
- **Ignoring the score and reporting only the label** — A `"fake"` label with score 0.51 means something very different from score 0.95
- **Submitting local file paths to the API** — The API requires publicly accessible HTTPS URLs (does not apply to text detection)
- **Sending text longer than 100,000 characters to text detection** — Split into chunks or inform the user of the limit
- **Polling too aggressively** — Start at 2s intervals, back off exponentially; do not loop at <1s
- **Asking Detect Intelligence questions before detection completes** — Results in 422 error
- **Expecting source tracing on "real" audio** — Source tracing only runs on audio labeled `"fake"`
- **Treating beta features (Identity, Text Detection) as production-ready** — Warn users about beta status
- **Ignoring `zero_retention_mode` for sensitive media** — Always suggest this flag when the user indicates the media is sensitive or private
- **Making multiple separate API calls when flags can combine** — Use `intelligence: true` and `audio_source_tracing: true` on the detection call instead of separate requests

## Response Presentation Guidelines

When presenting results to users:

1. **Lead with the verdict** — "The detection indicates this audio is likely AI-generated (score: 0.87)"
2. **Provide score context** — Use the score interpretation table above
3. **Mention limitations** — Detection is probabilistic, not absolute proof
4. **Include actionable next steps** — Suggest intelligence queries, source tracing, or watermark checks as appropriate
5. **For inconclusive results (0.3–0.5)** — Explicitly state the result is inconclusive and recommend additional analysis with different parameters or manual review
6. **Never present detection as legal evidence** — Detection results are analytical tools, not forensic certifications

## Error Handling

| Error     | Cause                                      | Resolution                                      |
|-----------|--------------------------------------------|-------------------------------------------------|
| 400       | Invalid request body or missing `url`      | Check required parameters                       |
| 401       | Invalid or missing API key                 | Verify `RESEMBLE_API_KEY`                       |
| 404       | Detection UUID not found                   | Verify the UUID from the creation response     |
| 422       | Detection not completed (for Intelligence) | Wait for detection to reach `completed` status |
| 429       | Rate limited                               | Back off and retry with exponential delay       |
| 500       | Server error                               | Retry once, then report to user                  |

## Privacy & Compliance Notes

- **Zero retention mode**: Set `zero_retention_mode: true` to auto-delete media after analysis. The URL is redacted and `media_deleted` is set to true post-completion.
- **Text privacy mode**: Set `privacy_mode: true` on text detection to prevent text content from being stored after analysis.
- **Data handling**: Media URLs and text content are stored by default. For GDPR/compliance-sensitive workflows, enable zero retention (media) or privacy mode (text).
- **Callback security**: If using `callback_url`, ensure the endpoint is HTTPS and authenticated on the receiving end.
