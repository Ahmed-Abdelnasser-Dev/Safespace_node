"""
managers — High-level orchestrators that wire handlers together.

Modules:
    input_manager   — InputManager (camera/video → buffer)
    ai_manager      — AIManager (buffer → inference → callbacks)
    output_manager  — OutputManager (display + server event bridge)
    network_manager — NetworkManager (central unit communication)
    stream_manager  — StreamManager (MediaMTX subprocess + StreamHandler)
    config_manager  — ConfigManager (CU-driven config update lifecycle)
"""
