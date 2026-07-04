"""
handlers — Low-level I/O and processing components.

Modules:
    camera_handler         — CameraHandler (picam / imx500 / imx500-raw)
    video_handler          — VideoHandler (file playback)
    frame_buffer           — FrameBuffer (thread-safe ring buffer)
    model_loader           — ModelLoader (YOLO .pt / ONNX loader)
    onnx_model             — OnnxModel (onnxruntime session wrapper)
    model_detection        — ModelDetection (inference + filtering)
    display/               — DisplayHandler (PyQt6 dashboard)
    socket_handler         — SocketHandler (Socket.IO + raw WebSocket client)
    config_channel_handler — ConfigChannelHandler (config.update WS transport)
    gps_handler            — GPSHandler (SIM808 UART polling)
"""
