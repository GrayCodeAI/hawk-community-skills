---
name: prompt-API
description: 'Skill: prompt-API'
license: MIT
tags:
- general
---

## builder/audio

Audio/Music Prompt Builder - Comprehensive music generation prompt builder

Based on Suno, Udio, and other music generation best practices.

@example
```ts
import { audio } from 'prompts.chat/builder';

const prompt = audio()
  .genre("synthwave")
  .mood("nostalgic", "dreamy")
  .tempo(110)
  .instruments(["synthesizer", "drums", "bass"])
  .structure({ intro: 8, verse: 16, chorus: 16 })
  .build();
```

### Types

#### `MusicGenre`

```typescript
type MusicGenre = | 'pop' | 'rock' | 'jazz' | 'classical' | 'electronic' | 'hip-hop' | 'r&b'
  | 'country' | 'folk' | 'blues' | 'metal' | 'punk' | 'indie' | 'alternative'
  | 'ambient' | 'lo-fi' | 'synthwave' | 'orchestral' | 'cinematic' | 'world'
  | 'latin' | 'reggae' | 'soul' | 'funk' | 'disco' | 'house' | 'techno' | 'edm'
  | 'trap' | 'drill' | 'k-pop' | 'j-pop' | 'bossa-nova' | 'gospel' | 'grunge'
  | 'shoegaze' | 'post-rock' | 'prog-rock' | 'psychedelic' | 'chillwave'
  | 'vaporwave' | 'drum-and-bass' | 'dubstep' | 'trance' | 'hardcore'
```

#### `Instrument`

```typescript
type Instrument = | 'piano' | 'guitar' | 'acoustic-guitar' | 'electric-guitar' | 'bass' | 'drums'
  | 'violin' | 'cello' | 'viola' | 'flute' | 'saxophone' | 'trumpet' | 'trombone'
  | 'synthesizer' | 'organ' | 'harp' | 'percussion' | 'strings' | 'brass' | 'woodwinds'
  | 'choir' | 'vocals' | 'beatbox' | 'turntables' | 'harmonica' | 'banjo' | 'ukulele'
  | 'mandolin' | 'accordion' | 'marimba' | 'vibraphone' | 'xylophone' | 'timpani'
  | 'congas' | 'bongos' | 'djembe' | 'tabla' | 'sitar' | 'erhu' | 'koto'
  | '808' | '909' | 'moog' | 'rhodes' | 'wurlitzer' | 'mellotron' | 'theremin'
```

#### `VocalStyle`

```typescript
type VocalStyle = | 'male' | 'female' | 'duet' | 'choir' | 'a-cappella' | 'spoken-word' | 'rap'
  | 'falsetto' | 'belting' | 'whisper' | 'growl' | 'melodic' | 'harmonized'
  | 'auto-tuned' | 'operatic' | 'soul' | 'breathy' | 'nasal' | 'raspy' | 'clear'
```

#### `VocalLanguage`

```typescript
type VocalLanguage = | 'english' | 'spanish' | 'french' | 'german' | 'italian' | 'portuguese'
  | 'japanese' | 'korean' | 'chinese' | 'arabic' | 'hindi' | 'russian' | 'turkish'
  | 'instrumental'
```

#### `TempoMarking`

```typescript
type TempoMarking = | 'largo' | 'adagio' | 'andante' | 'moderato' | 'allegro' | 'vivace' | 'presto'
```

#### `TimeSignature`

```typescript
type TimeSignature = '4/4' | '3/4' | '6/8' | '2/4' | '5/4' | '7/8' | '12/8'
```

#### `MusicalKey`

```typescript
type MusicalKey = | 'C' | 'C#' | 'Db' | 'D' | 'D#' | 'Eb' | 'E' | 'F' | 'F#' | 'Gb' 
  | 'G' | 'G#' | 'Ab' | 'A' | 'A#' | 'Bb' | 'B'
  | 'Cm' | 'C#m' | 'Dm' | 'D#m' | 'Ebm' | 'Em' | 'Fm' | 'F#m' 
  | 'Gm' | 'G#m' | 'Am' | 'A#m' | 'Bbm' | 'Bm'
```

#### `SongSection`

```typescript
type SongSection = | 'intro' | 'verse' | 'pre-chorus' | 'chorus' | 'bridge' | 'breakdown'
  | 'drop' | 'build-up' | 'outro' | 'solo' | 'interlude' | 'hook'
```

#### `ProductionStyle`

```typescript
type ProductionStyle = | 'lo-fi' | 'hi-fi' | 'vintage' | 'modern' | 'polished' | 'raw' | 'organic'
  | 'synthetic' | 'acoustic' | 'electric' | 'hybrid' | 'minimalist' | 'maximalist'
  | 'layered' | 'sparse' | 'dense' | 'atmospheric' | 'punchy' | 'warm' | 'bright'
```

#### `Era`

```typescript
type Era = | '1950s' | '1960s' | '1970s' | '1980s' | '1990s' | '2000s' | '2010s' | '2020s'
  | 'retro' | 'vintage' | 'classic' | 'modern' | 'futuristic'
```

### Interfaces

#### `AudioGenre`

| Property | Type | Description |
|----------|------|-------------|
| `primary` | `MusicGenre` | - |
| `secondary` | `MusicGenre[]` | - |
| `subgenre` | `string` | - |
| `fusion` | `string[]` | - |

#### `AudioMood`

| Property | Type | Description |
|----------|------|-------------|
| `primary` | `Mood | string` | - |
| `secondary` | `(Mood | string)[]` | - |
| `energy` | `'low' | 'medium' | 'high' | 'building' | 'fluctuating'` | - |
| `emotion` | `string` | - |

#### `AudioTempo`

| Property | Type | Description |
|----------|------|-------------|
| `bpm` | `number` | - |
| `marking` | `TempoMarking` | - |
| `feel` | `'steady' | 'swung' | 'shuffled' | 'syncopated' | 'rubato' | 'driving'` | - |
| `variation` | `boolean` | - |

#### `AudioVocals`

| Property | Type | Description |
|----------|------|-------------|
| `style` | `VocalStyle | VocalStyle[]` | - |
| `language` | `VocalLanguage` | - |
| `lyrics` | `string` | - |
| `theme` | `string` | - |
| `delivery` | `string` | - |
| `harmonies` | `boolean` | - |
| `adlibs` | `boolean` | - |

#### `AudioInstrumentation`

| Property | Type | Description |
|----------|------|-------------|
| `lead` | `Instrument | Instrument[]` | - |
| `rhythm` | `Instrument | Instrument[]` | - |
| `bass` | `Instrument` | - |
| `percussion` | `Instrument | Instrument[]` | - |
| `pads` | `Instrument | Instrument[]` | - |
| `effects` | `string[]` | - |
| `featured` | `Instrument` | - |

#### `AudioStructure`

| Property | Type | Description |
|----------|------|-------------|
| `sections` | `unknown` | - |
| `intro` | `number` | - |
| `verse` | `number` | - |
| `chorus` | `number` | - |
| `bridge` | `number` | - |
| `outro` | `number` | - |
| `form` | `string` | - |
| `duration` | `number` | - |

#### `AudioProduction`

| Property | Type | Description |
|----------|------|-------------|
| `style` | `ProductionStyle | ProductionStyle[]` | - |
| `era` | `Era` | - |
| `reference` | `string[]` | - |
| `mix` | `string` | - |
| `mastering` | `string` | - |
| `effects` | `string[]` | - |
| `texture` | `string` | - |

#### `AudioTechnical`

| Property | Type | Description |
|----------|------|-------------|
| `key` | `MusicalKey` | - |
| `timeSignature` | `TimeSignature` | - |
| `duration` | `number` | - |
| `format` | `'song' | 'instrumental' | 'jingle' | 'loop' | 'soundtrack'` | - |

#### `BuiltAudioPrompt`

| Property | Type | Description |
|----------|------|-------------|
| `prompt` | `string` | - |
| `stylePrompt` | `string` | - |
| `lyricsPrompt` | `string` | - |
| `structure` | `unknown` | - |

### Classes

#### `AudioPromptBuilder`

**Methods:**

| Method | Description |
|--------|-------------|
| `genre(primary: MusicGenre | AudioGenre): this` | - |
| `subgenre(subgenre: string): this` | - |
| `fusion(genres: MusicGenre[]): this` | - |
| `mood(primary: Mood | string, ...secondary: (Mood | string)[]): this` | - |
| `energy(level: AudioMood['energy']): this` | - |
| `emotion(emotion: string): this` | - |
| `tempo(bpmOrSettings: number | AudioTempo): this` | - |
| `bpm(bpm: number): this` | - |
| `tempoMarking(marking: TempoMarking): this` | - |
| `tempoFeel(feel: AudioTempo['feel']): this` | - |
| `vocals(settings: AudioVocals): this` | - |
| `vocalStyle(style: VocalStyle | VocalStyle[]): this` | - |
| `language(language: VocalLanguage): this` | - |
| `lyrics(lyrics: string): this` | - |
| `lyricsTheme(theme: string): this` | - |
| `delivery(delivery: string): this` | - |
| `instrumental(): this` | - |
| `instruments(instruments: Instrument[]): this` | - |
| `instrumentation(settings: AudioInstrumentation): this` | - |
| `leadInstrument(instrument: Instrument | Instrument[]): this` | - |
| `rhythmSection(instruments: Instrument[]): this` | - |
| `bassInstrument(instrument: Instrument): this` | - |
| `percussion(instruments: Instrument | Instrument[]): this` | - |
| `pads(instruments: Instrument | Instrument[]): this` | - |
| `featuredInstrument(instrument: Instrument): this` | - |
| `structure(settings: AudioStructure | { [key in SongSection]?: number }): this` | - |
| `section(type: SongSection, bars?: number, description?: string): this` | - |
| `form(form: string): this` | - |
| `duration(seconds: number): this` | - |
| `production(settings: AudioProduction): this` | - |
| `productionStyle(style: ProductionStyle | ProductionStyle[]): this` | - |
| `era(era: Era): this` | - |
| `reference(artists: string[]): this` | - |
| `texture(texture: string): this` | - |
| `effects(effects: string[]): this` | - |
| `technical(settings: AudioTechnical): this` | - |
| `key(key: MusicalKey): this` | - |
| `timeSignature(sig: TimeSignature): this` | - |
| `formatType(format: AudioTechnical['format']): this` | - |
| `tag(tag: string): this` | - |
| `tags(tags: string[]): this` | - |
| `custom(text: string): this` | - |
| `build(): BuiltAudioPrompt` | - |
| `toString(): string` | - |
| `toStyleString(): string` | - |
| `toJSON(): string` | - |
| `toYAML(): string` | - |
| `toMarkdown(): string` | - |
| `outputFormat(fmt: OutputFormat): string` | - |

##### `genre()`

```typescript
genre(primary: MusicGenre | AudioGenre): this
```

**Parameters:**

- `primary`: `MusicGenre | AudioGenre`

**Returns:** `this`

##### `subgenre()`

```typescript
subgenre(subgenre: string): this
```

**Parameters:**

- `subgenre`: `string`

**Returns:** `this`

##### `fusion()`

```typescript
fusion(genres: MusicGenre[]): this
```

**Parameters:**

- `genres`: `MusicGenre[]`

**Returns:** `this`

##### `mood()`

```typescript
mood(primary: Mood | string, ...secondary: (Mood | string)[]): this
```

**Parameters:**

- `primary`: `Mood | string`
- `secondary`: `(Mood | string)[]`

**Returns:** `this`

##### `energy()`

```typescript
energy(level: AudioMood['energy']): this
```

**Parameters:**

- `level`: `AudioMood['energy']`

**Returns:** `this`

##### `emotion()`

```typescript
emotion(emotion: string): this
```

**Parameters:**

- `emotion`: `string`

**Returns:** `this`

##### `tempo()`

```typescript
tempo(bpmOrSettings: number | AudioTempo): this
```

**Parameters:**

- `bpmOrSettings`: `number | AudioTempo`

**Returns:** `this`

##### `bpm()`

```typescript
bpm(bpm: number): this
```

**Parameters:**

- `bpm`: `number`

**Returns:** `this`

##### `tempoMarking()`

```typescript
tempoMarking(marking: TempoMarking): this
```

**Parameters:**

- `marking`: `TempoMarking`

**Returns:** `this`

##### `tempoFeel()`

```typescript
tempoFeel(feel: AudioTempo['feel']): this
```

**Parameters:**

- `feel`: `AudioTempo['feel']`

**Returns:** `this`

##### `vocals()`

```typescript
vocals(settings: AudioVocals): this
```

**Parameters:**

- `settings`: `AudioVocals`

**Returns:** `this`

##### `vocalStyle()`

```typescript
vocalStyle(style: VocalStyle | VocalStyle[]): this
```

**Parameters:**

- `style`: `VocalStyle | VocalStyle[]`

**Returns:** `this`

##### `language()`

```typescript
language(language: VocalLanguage): this
```

**Parameters:**

- `language`: `VocalLanguage`

**Returns:** `this`

##### `lyrics()`

```typescript
lyrics(lyrics: string): this
```

**Parameters:**

- `lyrics`: `string`

**Returns:** `this`

##### `lyricsTheme()`

```typescript
lyricsTheme(theme: string): this
```

**Parameters:**

- `theme`: `string`

**Returns:** `this`

##### `delivery()`

```typescript
delivery(delivery: string): this
```

**Parameters:**

- `delivery`: `string`

**Returns:** `this`

##### `instrumental()`

```typescript
instrumental(): this
```

**Returns:** `this`

##### `instruments()`

```typescript
instruments(instruments: Instrument[]): this
```

**Parameters:**

- `instruments`: `Instrument[]`

**Returns:** `this`

##### `instrumentation()`

```typescript
instrumentation(settings: AudioInstrumentation): this
```

**Parameters:**

- `settings`: `AudioInstrumentation`

**Returns:** `this`

##### `leadInstrument()`

```typescript
leadInstrument(instrument: Instrument | Instrument[]): this
```

**Parameters:**

- `instrument`: `Instrument | Instrument[]`

**Returns:** `this`

##### `rhythmSection()`

```typescript
rhythmSection(instruments: Instrument[]): this
```

**Parameters:**

- `instruments`: `Instrument[]`

**Returns:** `this`

##### `bassInstrument()`

```typescript
bassInstrument(instrument: Instrument): this
```

**Parameters:**

- `instrument`: `Instrument`

**Returns:** `this`

##### `percussion()`

```typescript
percussion(instruments: Instrument | Instrument[]): this
```

**Parameters:**

- `instruments`: `Instrument | Instrument[]`

**Returns:** `this`

##### `pads()`

```typescript
pads(instruments: Instrument | Instrument[]): this
```

**Parameters:**

- `instruments`: `Instrument | Instrument[]`

**Returns:** `this`

##### `featuredInstrument()`

```typescript
featuredInstrument(instrument: Instrument): this
```

**Parameters:**

- `instrument`: `Instrument`

**Returns:** `this`

##### `structure()`

```typescript
structure(settings: AudioStructure | { [key in SongSection]?: number }): this
```

**Parameters:**

- `settings`: `AudioStructure | { [key in SongSection]?: number }`

**Returns:** `this`

##### `section()`

```typescript
section(type: SongSection, bars?: number, description?: string): this
```

**Parameters:**

- `type`: `SongSection`
- `bars`: `number` (optional)
- `description`: `string` (optional)

**Returns:** `this`

##### `form()`

```typescript
form(form: string): this
```

**Parameters:**

- `form`: `string`

**Returns:** `this`

##### `duration()`

```typescript
duration(seconds: number): this
```

**Parameters:**

- `seconds`: `number`

**Returns:** `this`

##### `production()`

```typescript
production(settings: AudioProduction): this
```

**Parameters:**

- `settings`: `AudioProduction`

**Returns:** `this`

##### `productionStyle()`

```typescript
productionStyle(style: ProductionStyle | ProductionStyle[]): this
```

**Parameters:**

- `style`: `ProductionStyle | ProductionStyle[]`

**Returns:** `this`

##### `era()`

```typescript
era(era: Era): this
```

**Parameters:**

- `era`: `Era`

**Returns:** `this`

##### `reference()`

```typescript
reference(artists: string[]): this
```

**Parameters:**

- `artists`: `string[]`

**Returns:** `this`

##### `texture()`

```typescript
texture(texture: string): this
```

**Parameters:**

- `texture`: `string`

**Returns:** `this`

##### `effects()`

```typescript
effects(effects: string[]): this
```

**Parameters:**

- `effects`: `string[]`

**Returns:** `this`

##### `technical()`

```typescript
technical(settings: AudioTechnical): this
```

**Parameters:**

- `settings`: `AudioTechnical`

**Returns:** `this`

##### `key()`

```typescript
key(key: MusicalKey): this
```

**Parameters:**

- `key`: `MusicalKey`

**Returns:** `this`

##### `timeSignature()`

```typescript
timeSignature(sig: TimeSignature): this
```

**Parameters:**

- `sig`: `TimeSignature`

**Returns:** `this`

##### `formatType()`

```typescript
formatType(format: AudioTechnical['format']): this
```

**Parameters:**

- `format`: `AudioTechnical['format']`

**Returns:** `this`

##### `tag()`

```typescript
tag(tag: string): this
```

**Parameters:**

- `tag`: `string`

**Returns:** `this`

##### `tags()`

```typescript
tags(tags: string[]): this
```

**Parameters:**

- `tags`: `string[]`

**Returns:** `this`

##### `custom()`

```typescript
custom(text: string): this
```

**Parameters:**

- `text`: `string`

**Returns:** `this`

##### `build()`

```typescript
build(): BuiltAudioPrompt
```

**Returns:** `BuiltAudioPrompt`

##### `toString()`

```typescript
toString(): string
```

**Returns:** `string`

##### `toStyleString()`

```typescript
toStyleString(): string
```

**Returns:** `string`

##### `toJSON()`

```typescript
toJSON(): string
```

**Returns:** `string`

##### `toYAML()`

```typescript
toYAML(): string
```

**Returns:** `string`

##### `toMarkdown()`

```typescript
toMarkdown(): string
```

**Returns:** `string`

##### `outputFormat()`

```typescript
outputFormat(fmt: OutputFormat): string
```

**Parameters:**

- `fmt`: `OutputFormat`

**Returns:** `string`

### Functions

#### `audio()`

Create a new audio/music prompt builder

```typescript
audio(): AudioPromptBuilder
```

**Returns:** `AudioPromptBuilder`
