from events.schemas import Incident, SafetyEvent, Severity

SEVERITY_RANK = {
    Severity.LOW: 1,
    Severity.MEDIUM: 2,
    Severity.HIGH: 3,
    Severity.CRITICAL: 4,
}


def incident_id_for(event: SafetyEvent) -> str:
    if event.incident_id:
        return event.incident_id
    return f"{event.camera_id}:{event.rule_id}"


def merge_event_into_incident(incident: Incident | None, event: SafetyEvent) -> Incident:
    incident_id = incident_id_for(event)
    event.incident_id = incident_id

    if incident is None:
        return Incident(
            incident_id=incident_id,
            camera_id=event.camera_id,
            opened_at=event.timestamp,
            updated_at=event.timestamp,
            highest_severity=event.severity,
            event_ids=[event.event_id],
            timeline=[event],
        )

    incident.updated_at = max(incident.updated_at, event.timestamp)
    if SEVERITY_RANK[event.severity] > SEVERITY_RANK[incident.highest_severity]:
        incident.highest_severity = event.severity
    incident.event_ids.append(event.event_id)
    incident.timeline.append(event)
    incident.timeline.sort(key=lambda item: item.timestamp)
    return incident

