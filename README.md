# LIMINAL

A first-person walking sim set in liminal spaces. Single-file HTML5 + Three.js, no build step — just open and walk.

> *you exist. that is enough.*

## Play

Open the latest version directly in a browser:

```
liminal_10.html
```

Or visit any earlier version (`liminal.html`, `liminal_1.html` … `liminal_9.html`) to see how it evolved. The site at [liminal.stacklis.com](https://liminal.stacklis.com) lists every iteration.

## Controls

| Key | Action |
| --- | --- |
| `WASD` | move |
| `Shift` | sprint |
| `Space` | jump |
| `Mouse` | look |
| `E` | open / close door |
| `Click` | lock cursor |

Touch controls (on-screen d-pad) appear on mobile.

## Options

In-game `options` panel:

- **Audio** — master volume, ambient, footsteps
- **Display** — scanlines, film grain, vignette
- **Save** — store / restore your position

Settings and saved positions persist via `localStorage`.

## Stack

- [Three.js r128](https://threejs.org/) (CDN)
- Vanilla JS, single HTML file
- No build, no install, no server required

## Versions

Each numbered file is a frozen snapshot of a past iteration. `liminal_10.html` is current. New versions are committed as `Version N` on `main`.
