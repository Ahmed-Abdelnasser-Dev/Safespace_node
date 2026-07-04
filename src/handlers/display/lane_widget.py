"""
Lane Widget — single lane indicator with SVG icon and status label.
"""
from pathlib import Path

from PyQt6.QtWidgets import (
    QFrame, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont

try:
    from PyQt6.QtSvgWidgets import QSvgWidget
    _HAS_QTSVGWIDGETS = True
except ImportError:
    QSvgWidget = None
    _HAS_QTSVGWIDGETS = False

from utils.constants import ROAD_SIGNS_DIR
from handlers.display.theme import DEFAULT_THEME


# ── Lane Status → Static Metadata ────────────────────────────────
# Icon filename and label text never change with theme. Colors come from the
# active theme's `lane` dict at runtime (see LaneWidget.__init__).

LANE_STATUS_META = {
    "up":      {"icon": "go_straight.svg", "label": "OPEN"},
    "blocked": {"icon": "blocked.svg",     "label": "BLOCKED"},
    "left":    {"icon": "turn-left.svg",   "label": "TURN LEFT"},
    "right":   {"icon": "turn-right.svg",  "label": "TURN RIGHT"},
}


class LaneWidget(QFrame):
    """Visual widget for a single lane: large SVG icon + small status label."""

    def __init__(self, lane_number: int, parent=None, theme: dict = None):
        super().__init__(parent)
        self.lane_number = lane_number
        self.theme = theme or DEFAULT_THEME
        self.setObjectName(f"lane_{lane_number}")

        self.setMinimumSize(130, 180)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(6)
        layout.setContentsMargins(10, 14, 10, 14)

        # Lane number label (small, top)
        self.title_label = QLabel(f"LANE {lane_number + 1}")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        self.title_label.setStyleSheet(f"color: {self.theme['lane']['title_text']}; background: transparent;")
        layout.addWidget(self.title_label)

        # SVG Icon — large and dominant (falls back to text if QtSvgWidgets is missing)
        if _HAS_QTSVGWIDGETS:
            self.icon_widget = QSvgWidget()
        else:
            self.icon_widget = QLabel("SIGN")
            self.icon_widget.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.icon_widget.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
            self.icon_widget.setStyleSheet("color: #cccccc; background: transparent;")
        self.icon_widget.setFixedSize(QSize(96, 96))
        icon_container = QHBoxLayout()
        icon_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_container.addWidget(self.icon_widget)
        layout.addLayout(icon_container, stretch=1)

        # Status label (small subtitle below icon)
        self.status_label = QLabel("OPEN")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        self.status_label.setStyleSheet(f"color: {self.theme['lane']['up']['label']}; background: transparent;")
        layout.addWidget(self.status_label)

        # Default state
        self.set_status("up")

    def set_status(self, status: str):
        """Update the lane to show the given status."""
        status = status.lower()
        meta = LANE_STATUS_META.get(status, LANE_STATUS_META["up"])
        colors = self.theme['lane'].get(status, self.theme['lane']["up"])
        label_color = colors["label"]

        # Load SVG icon when available, otherwise display a text fallback.
        if _HAS_QTSVGWIDGETS:
            icon_path = str(ROAD_SIGNS_DIR / meta["icon"])
            if Path(icon_path).exists():
                self.icon_widget.load(icon_path)
        else:
            self.icon_widget.setText(meta["label"])
            self.icon_widget.setStyleSheet(
                f"color: {label_color}; background: transparent;"
            )

        # Update frame style — use #id selector so it does NOT cascade to children
        obj_id = self.objectName()
        self.setStyleSheet(f"""
            QFrame#{obj_id} {{
                background: {colors['bg']};
                border: 2px solid {colors['border']};
                border-radius: 16px;
            }}
        """)

        # Re-apply child styles explicitly (Qt cascading would otherwise blank them)
        self.title_label.setStyleSheet(f"color: {self.theme['lane']['title_text']}; background: transparent;")
        self.status_label.setText(meta["label"])
        self.status_label.setStyleSheet(
            f"color: {label_color}; background: transparent;"
        )
        self.icon_widget.setStyleSheet("background: transparent;")
