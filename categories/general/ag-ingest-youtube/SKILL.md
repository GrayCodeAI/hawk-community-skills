---
name: ag-ingest-youtube
description: Pull a YouTube video transcript into a queryable markdown vault with
  yt-dlp subtitle discovery, VTT cleanup, metadata frontmatter, and capture-seed stubs.
license: MIT
tags:
- general
risk: safe
source: community
source_repo: adelaidasofia/ai-brain-starter
source_type: community
date_added: 2026-05-09
license_source: https://github.com/adelaidasofia/ai-brain-starter/blob/main/LICENSE
upstream: https://github.com/adelaidasofia/ai-brain-starter/tree/main/skills/ingest-youtube
---

```

Body is the cleaned transcript as paragraph prose. If the source had speaker labels, format as `**<speaker>:** <text>` per turn.

## Idempotency

Re-ingesting the same video URL overwrites the same vault file. The seed stub filenames hash the video_id, so the same source video produces the same stub filename across re-runs. Re-runs refresh, never duplicate.

## Missing subtitles

If `yt-dlp --list-subs` returns no manual or auto subtitles, the script writes a stub vault note with the video metadata and source URL instead of failing silently. The `--whisper` flag is reserved for a future local transcription fallback and currently reports that the fallback is not implemented.

For a manual fallback today, download audio with `yt-dlp`, transcribe it with your local Whisper workflow, and add captions or transcript text before rerunning the ingest.

## Limitations

- Ingests one YouTube video URL per run; channel handles, playlists, and `--days` windows are out of scope.
- Depends on subtitles returned by `yt-dlp`; videos without subtitles produce a metadata stub, not a transcript.
- Does not download video files or perform built-in Whisper transcription in this version.
- Network availability, YouTube subtitle access, and local `yt-dlp` behavior determine whether ingest succeeds.

## Acceptance test

Run against the first YouTube video ever uploaded:

```bash
python3 ingest.py "https://www.youtube.com/watch?v=jNQXAC9IVRw" --vault /tmp/test
```

Expected output:
```
Wrote 39 words to /tmp/test/External Inputs/YouTube/jawed/2005-04-24-me-at-the-zoo.md. Language: en. Subtitle source: manual.
```

The output file contains valid frontmatter and a clean prose body.

## Dependencies

- `yt-dlp` (required): install via `brew install yt-dlp` or `pip3 install --user yt-dlp`
- `whisper-cpp` (optional for a manual fallback outside this script)

## Source

Bundled in [adelaidasofia/ai-brain-starter](https://github.com/adelaidasofia/ai-brain-starter), a verification harness around an AI agent so memory compounds instead of corrupts. The skill is part of the ingest-* family of vault connectors.
