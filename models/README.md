# models/ : Model Files and Fingerprint Records

**Status: NOT STARTED. No model has been trained.**

## Layout

| Path | Contents | In Git? |
|---|---|---|
| `models/manifests/` | For each checkpoint: file name, size in bytes, SHA-256 fingerprint, date, who recorded it | Yes |
| Everything else in `models/` | Checkpoint files, tampered test copies | No (ignored; keep in shared storage) |

## Rules

1. Name checkpoints so run and stage are visible, for example `run-001_stage-1`.
2. **Never overwrite or re-save** a checkpoint after it has been fingerprinted.
3. Retrieval instructions (where the file lives in shared storage) go in the manifest.
4. Deliberately damaged copies are made **only as copies**, are **only hashed**, and are **never loaded**.
5. Only load model files you created yourself.

## Manifest columns to record

`run`, `stage`, `file_name`, `size_bytes`, `sha256`, `reported_accuracy`, `storage_location`, `recorded_by`, `date`
