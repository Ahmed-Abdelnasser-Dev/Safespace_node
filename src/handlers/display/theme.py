"""
Theme palettes for the Safespace dashboard.

A plain dict of color strings per theme — no stylesheet engine, consistent with
the widgets' inline `setStyleSheet()` convention. Widgets take an optional
`theme: dict` constructor kwarg and read their colors from it; if none is passed
they fall back to `DEFAULT_THEME`.

Theme is resolved once at startup via `get_theme(config)` reading the
`display.theme` config key ("light" | "dark", default "light"). Switching themes
is a restart-to-apply operation, not a live in-app toggle.

Dict shape (both themes share it 1:1):
    window_bg / window_text          window palette (QPalette)
    accent                           header text + video-feed FPS overlay
    status_text                      status bar line
    gps_searching / gps_fix          GPS indicator states
    lane.<status>.{bg,border,label}  per lane status (up/blocked/left/right)
    lane.title_text                  lane-number label (state-independent)
    accident_banner.{idle,active,dim}_{bg,border,text}
    speed.{frame_bg,frame_border,title_text,value_text,unit_text,
           alert_frame_bg,alert_frame_border,alert_value_text}
    system_monitor.{frame_bg,frame_border,title_text,cpu_text,mem_text,
                    bar_track_bg,bar_chunk_low,bar_chunk_mid,bar_chunk_high}
    video_feed.{frame_bg,frame_border,title_text,fps_text}
"""

# ── Light theme ───────────────────────────────────────────────────────────────
# High-contrast, saturated colors for outdoor daytime / sunlight readability.
# Dark text on light backgrounds; status colors are deep and saturated (not
# pastel) so they stay legible in direct light.
_LIGHT = {
    "window_bg": "#f4f6f8",
    "window_text": "#101418",
    "accent": "#0066cc",
    "status_text": "#4a4a4a",
    "gps_searching": "#b36b00",
    "gps_fix": "#128a4b",
    "lane": {
        "up":      {"bg": "rgba(0, 153, 76, 0.12)",  "border": "rgba(0, 153, 76, 0.9)",  "label": "#0b7a3d"},
        "blocked": {"bg": "rgba(204, 0, 0, 0.12)",   "border": "rgba(204, 0, 0, 0.85)",  "label": "#b30000"},
        "left":    {"bg": "rgba(204, 102, 0, 0.14)", "border": "rgba(204, 102, 0, 0.85)", "label": "#a15c00"},
        "right":   {"bg": "rgba(204, 102, 0, 0.14)", "border": "rgba(204, 102, 0, 0.85)", "label": "#a15c00"},
        "title_text": "#5a6472",
    },
    "accident_banner": {
        "idle_bg": "rgba(0, 0, 0, 0)",
        "idle_border": "rgba(0, 0, 0, 0)",
        "idle_text": "rgba(0, 0, 0, 0)",
        "active_bg": "rgba(220, 20, 20, 0.28)",
        "active_border": "#cc0000",
        "active_text": "#990000",
        "dim_bg": "rgba(204, 0, 0, 0.08)",
        "dim_border": "rgba(204, 0, 0, 0.35)",
        "dim_text": "rgba(153, 0, 0, 0.55)",
    },
    "speed": {
        "frame_bg": "rgba(0, 0, 0, 0.03)",
        "frame_border": "rgba(0, 0, 0, 0.15)",
        "title_text": "#5a6472",
        "value_text": "#101418",
        "unit_text": "#6b7280",
        "alert_frame_bg": "rgba(204, 0, 0, 0.10)",
        "alert_frame_border": "#cc0000",
        "alert_value_text": "#b30000",
    },
    "system_monitor": {
        "frame_bg": "rgba(0, 0, 0, 0.03)",
        "frame_border": "rgba(0, 0, 0, 0.12)",
        "title_text": "#5a6472",
        "cpu_text": "#101418",
        "mem_text": "#6b7280",
        "bar_track_bg": "rgba(0, 0, 0, 0.08)",
        "bar_chunk_low": "#128a4b",
        "bar_chunk_mid": "#b36b00",
        "bar_chunk_high": "#b30000",
    },
    "video_feed": {
        "frame_bg": "rgba(0, 0, 0, 0.04)",
        "frame_border": "rgba(0, 0, 0, 0.12)",
        "title_text": "#5a6472",
        "fps_text": "#0066cc",
    },
}

# ── Dark theme ────────────────────────────────────────────────────────────────
# Reorganization of the original hardcoded literals into the shared shape — no
# visual change from the app's original dark-only appearance.
_DARK = {
    "window_bg": "#1a1a2e",
    "window_text": "#ffffff",
    "accent": "#00d4ff",
    "status_text": "#555555",
    "gps_searching": "#ff9900",
    "gps_fix": "#00ff88",
    "lane": {
        "up":      {"bg": "rgba(0, 255, 136, 0.12)", "border": "rgba(0, 255, 136, 0.6)", "label": "#00ff88"},
        "blocked": {"bg": "rgba(255, 50, 50, 0.12)", "border": "rgba(255, 50, 50, 0.6)", "label": "#ff3232"},
        "left":    {"bg": "rgba(255, 165, 0, 0.12)", "border": "rgba(255, 165, 0, 0.6)", "label": "#ffa500"},
        "right":   {"bg": "rgba(255, 165, 0, 0.12)", "border": "rgba(255, 165, 0, 0.6)", "label": "#ffa500"},
        "title_text": "#888888",
    },
    "accident_banner": {
        "idle_bg": "rgba(0, 0, 0, 0)",
        "idle_border": "rgba(0, 0, 0, 0)",
        "idle_text": "rgba(0, 0, 0, 0)",
        "active_bg": "rgba(255, 50, 50, 0.25)",
        "active_border": "#ff4444",
        "active_text": "#ff4444",
        "dim_bg": "rgba(255, 50, 50, 0.10)",
        "dim_border": "rgba(255, 68, 68, 0.4)",
        "dim_text": "rgba(255, 68, 68, 0.5)",
    },
    "speed": {
        "frame_bg": "rgba(255, 255, 255, 0.06)",
        "frame_border": "rgba(255, 255, 255, 0.15)",
        "title_text": "#aaaaaa",
        "value_text": "#ffffff",
        "unit_text": "#888888",
        "alert_frame_bg": "rgba(255, 50, 50, 0.15)",
        "alert_frame_border": "rgba(255, 50, 50, 0.7)",
        "alert_value_text": "#ff4444",
    },
    "system_monitor": {
        "frame_bg": "rgba(255, 255, 255, 0.06)",
        "frame_border": "rgba(255, 255, 255, 0.12)",
        "title_text": "#888888",
        "cpu_text": "#ffffff",
        "mem_text": "#666666",
        "bar_track_bg": "rgba(255, 255, 255, 0.08)",
        "bar_chunk_low": "#00ff88",
        "bar_chunk_mid": "#ffa500",
        "bar_chunk_high": "#ff4444",
    },
    "video_feed": {
        "frame_bg": "rgba(0, 0, 0, 0.4)",
        "frame_border": "rgba(255, 255, 255, 0.1)",
        "title_text": "#888888",
        "fps_text": "#00d4ff",
    },
}

THEMES = {
    "light": _LIGHT,
    "dark": _DARK,
}

DEFAULT_THEME = THEMES["light"]


def get_theme(config) -> dict:
    """Return the active theme dict based on the `display.theme` config key.

    Falls back to the light theme for any missing or unrecognized value.
    """
    name = str(config.get("display.theme", "light")).strip().lower()
    return THEMES.get(name, THEMES["light"])
