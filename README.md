# InterVerse Builder

InterVerse Builder is the scene-command validation layer for the InterVerseSG virtual campus. It receives structured commands from `interverse-api`, validates them against an allowlist, and produces deterministic instructions that Unreal Engine can execute safely.

## Initial scope

- Validate scene actions before they reach Unreal Engine.
- Map semantic object types (for example `chair`) to Unreal Blueprint class names.
- Enforce quantity limits and confirmation requirements.
- Reject unsupported or unsafe commands.
- Return a stable JSON contract for Meta Quest and Unreal Engine clients.

## API

- `GET /`
- `GET /healthz`
- `GET /api/v1/catalog`
- `POST /api/v1/build/validate`

## Run in cloud

The repository includes `render.yaml` so it can be deployed as a Render web service directly from GitHub.
