from threading import Lock

from api.models.camera import Camera, CameraRegistration
from events.lifecycle import incident_id_for, merge_event_into_incident
from events.schemas import Incident, SafetyEvent
from telemetry.metrics import metrics


class InMemoryStore:
    def __init__(self) -> None:
        self._lock = Lock()
        self.cameras: dict[str, Camera] = {}
        self.events: dict[str, SafetyEvent] = {}
        self.incidents: dict[str, Incident] = {}

    def reset(self) -> None:
        with self._lock:
            self.cameras.clear()
            self.events.clear()
            self.incidents.clear()

    def register_camera(self, registration: CameraRegistration) -> Camera:
        camera = Camera(**registration.model_dump())
        with self._lock:
            self.cameras[camera.camera_id] = camera
        return camera

    def list_cameras(self) -> list[Camera]:
        with self._lock:
            return list(self.cameras.values())

    def add_event(self, event: SafetyEvent) -> SafetyEvent:
        with self._lock:
            incident_id = incident_id_for(event)
            incident = self.incidents.get(incident_id)
            self.incidents[incident_id] = merge_event_into_incident(incident, event)
            self.events[event.event_id] = event
        metrics.observe_event(event)
        return event

    def list_events(self) -> list[SafetyEvent]:
        with self._lock:
            return sorted(self.events.values(), key=lambda event: event.timestamp)

    def list_incidents(self) -> list[Incident]:
        with self._lock:
            return sorted(self.incidents.values(), key=lambda item: item.updated_at, reverse=True)

    def get_incident(self, incident_id: str) -> Incident | None:
        with self._lock:
            return self.incidents.get(incident_id)


store = InMemoryStore()

