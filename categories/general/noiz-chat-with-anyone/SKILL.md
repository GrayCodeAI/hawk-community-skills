---
name: noiz-chat-with-anyone
description: Chat with any real person or fictional character in their own voice by
  automatically finding their speech online, extracting a clean reference sample,
  and generating audio replies. Also supports ge...
license: MIT
tags:
- general
permissions: None
metadata:
  openclaw:
    primaryEnv: NOIZ_API_KEY
---

## Example: Name-based

**User**: 我想跟特朗普聊天，让他给我讲个睡前故事。

**Agent steps**:
1. Character: Donald Trump. No disambiguation needed.
2. Search `Donald Trump speech youtube`, find a clear speech video.
3. Download:
   `yt-dlp -x --audio-format mp3 --write-subs --write-auto-subs --sub-langs "en" --convert-subs srt -o "tmp/chat_with_anyone/trump/%(title)s.%(ext)s" "https://youtube.com/watch?v=..."`
4. Extract reference:
   `python3 skills/chat-with-anyone/scripts/extract_ref_segment.py --srt "tmp/chat_with_anyone/trump/....srt" --audio "tmp/chat_with_anyone/trump/....mp3" -o "tmp/chat_with_anyone/trump/ref.wav"`
5. Generate TTS in Trump's style:
   `python3 skills/tts/scripts/tts.py -t "Let me tell you a tremendous bedtime story..." --ref-audio "tmp/chat_with_anyone/trump/ref.wav" -o "tmp/chat_with_anyone/trump/reply.wav"`
6. Present `reply.wav` and the story text to the user.

## Example: Image-based

**User**: [uploads photo.jpg] 我想跟这张图片里的人聊天

**Agent steps**:
1. Vision analysis: unrecognizable young woman, ~25, casual sweater, warm smile.
2. Design voice:
   `python3 skills/chat-with-anyone/scripts/voice_design.py --picture "photo.jpg" --voice-description "A young Chinese woman around 25, gentle and warm voice, friendly tone" -o "tmp/chat_with_anyone/voice_design"`
3. Read voice ID from `tmp/chat_with_anyone/voice_design/voice_id.txt`.
4. Generate TTS:
   `python3 skills/tts/scripts/tts.py -t "你好呀！很高兴认识你！" --voice-id "{VOICE_ID}" -o "tmp/chat_with_anyone/voice_design/reply.wav"`
5. Present audio and continue roleplay with same `--voice-id`.

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `yt-dlp` download fails or video unavailable | Try a different video URL; some regions/videos are restricted. Run `yt-dlp -U` to update |
| No SRT subtitle files | Re-download with `--sub-lang en,zh-Hans`; if still none, try a different video with auto-captions |
| `extract_ref_segment.py` finds no suitable window | Use `--min-duration 2` for shorter clips, or try a different video |
| Voice design returns error | Check Noiz API key; ensure image is a clear photo of a person |
| TTS output sounds wrong | For Workflow A, try a different reference video; for Workflow B, adjust `--voice-description` |
