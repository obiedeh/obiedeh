# edge-ai-deployer

Use when touching Jetson, RTX, CUDA, Docker, TensorRT, vLLM, NIM, RTSP/video input, or edge
deployment files.

## Deployment Rules

- Keep public configs generic; no internal hosts, IPs, credentials, or topology.
- Separate local demo, edge device, and real model paths.
- Make heavy dependencies optional unless required for the base path.
- Include health checks and restart expectations for long-running services.

## Checks

- Validate Docker/Compose syntax when practical.
- Verify optional dependency paths fail clearly when dependency is missing.
- Record hardware checks separately from generic CI checks.

## Output

Report deployment target, commands run, untested hardware assumptions, and follow-up work.

