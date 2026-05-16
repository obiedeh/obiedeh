from collections.abc import Iterator
from datetime import UTC, datetime
from time import sleep
from typing import Any

from edge.source_loader import VideoSource
from evidence.hashing import hash_text


def sample_frames(source: VideoSource) -> Iterator[dict[str, Any]]:
    frames = source.frames or [{} for _ in range(source.frame_count)]
    for index, frame in enumerate(frames[: source.frame_count], start=1):
        timestamp = datetime.now(UTC)
        context = {
            "frame_id": frame.get("frame_id", f"frame-{index:04d}"),
            "camera_id": source.camera_id,
            "source_uri": source.source_uri,
            "timestamp": timestamp,
            "frame_hash": frame.get(
                "frame_hash",
                hash_text(f"{source.camera_id}:{source.source_uri}:{index}:{timestamp.isoformat()}"),
            ),
            "metadata": frame.get("metadata", {}),
            "detections": frame.get("detections"),
        }
        yield context
        if source.sample_interval_ms:
            sleep(source.sample_interval_ms / 1000)

