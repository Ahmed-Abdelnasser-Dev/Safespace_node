"""
Speed Widget — circular speed limit display.
"""
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from handlers.display.theme import DEFAULT_THEME


class SpeedWidget(QFrame):
    """Speed limit display with normal / alert modes."""

    def __init__(self, default_speed: int = 120, parent=None, theme: dict = None):
        super().__init__(parent)
        self.theme = theme or DEFAULT_THEME
        self.setObjectName("speed_widget")
        self.setFixedSize(150, 170)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(4)

        # Title
        self.title_label = QLabel("SPEED LIMIT")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        self.title_label.setStyleSheet(f"color: {self.theme['speed']['title_text']}; background: transparent;")
        layout.addWidget(self.title_label)

        # Speed number
        self.speed_label = QLabel(str(default_speed))
        self.speed_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.speed_label.setFont(QFont("Segoe UI", 32, QFont.Weight.Bold))
        self.speed_label.setStyleSheet(f"color: {self.theme['speed']['value_text']}; background: transparent;")
        layout.addWidget(self.speed_label)

        # Unit
        self.unit_label = QLabel("km/h")
        self.unit_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.unit_label.setFont(QFont("Segoe UI", 9))
        self.unit_label.setStyleSheet(f"color: {self.theme['speed']['unit_text']}; background: transparent;")
        layout.addWidget(self.unit_label)

        self._set_normal_style()

    def set_speed(self, limit: int):
        """Update the displayed speed limit."""
        self.speed_label.setText(str(limit))

    def set_alert_mode(self, active: bool):
        """Switch between normal and alert styling."""
        s = self.theme['speed']
        if active:
            self.setStyleSheet(f"""
                QFrame#speed_widget {{
                    background: {s['alert_frame_bg']};
                    border: 3px solid {s['alert_frame_border']};
                    border-radius: 16px;
                }}
            """)
            self.speed_label.setStyleSheet(f"color: {s['alert_value_text']}; background: transparent;")
        else:
            self._set_normal_style()
            self.speed_label.setStyleSheet(f"color: {s['value_text']}; background: transparent;")

        # Re-apply child styles so they don't get overridden
        self.title_label.setStyleSheet(f"color: {s['title_text']}; background: transparent;")
        self.unit_label.setStyleSheet(f"color: {s['unit_text']}; background: transparent;")

    def _set_normal_style(self):
        s = self.theme['speed']
        self.setStyleSheet(f"""
            QFrame#speed_widget {{
                background: {s['frame_bg']};
                border: 2px solid {s['frame_border']};
                border-radius: 16px;
            }}
        """)
