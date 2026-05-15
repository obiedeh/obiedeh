# Traffic Source API

This project uses a pluggable telemetry-source interface so the detection pipeline does not depend on one dataset or one capture mechanism.

Supported source categories:

- CSV replay for existing Edge-IIoT datasets
- PCAP replay for previously captured lab traffic
- Live capture adapters for approved defensive lab environments
- MQTT telemetry adapters for IIoT devices
- Zeek and Suricata log adapters for security monitoring pipelines
- Synthetic benign/adversarial lab-event generators for controlled defensive testing

The design goal is simple: every source emits normalized telemetry events into the same downstream feature extraction, inference, alerting, and benchmarking path.

## Interface contract

Each source must provide:

- `name`: stable source name
- `open()`: allocate source resources
- `events()`: stream normalized telemetry events
- `close()`: release resources

The interface intentionally avoids coupling to any specific capture backend. Future adapters can wrap Wireshark/tshark exports, Zeek logs, Suricata EVE JSON, MQTT streams, or generated lab traffic without changing the model pipeline.
