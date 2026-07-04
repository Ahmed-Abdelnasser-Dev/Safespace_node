"""
System Monitor Widget — displays CPU usage with a progress bar and label.

Uses psutil to sample CPU % on a QTimer.
"""
import psutil
from PyQt6.QtWidgets import QFrame, QVBoxLayout, QLabel, QProgressBar
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont

from handlers.display.theme import DEFAULT_THEME


class SystemMonitorWidget(QFrame):
    """Compact CPU / system usage monitor for the dev dashboard."""

    def __init__(self, interval_ms: int = 1000, parent=None, theme: dict = None):
        super().__init__(parent)
        self.theme = theme or DEFAULT_THEME
        m = self.theme['system_monitor']
        self.setObjectName("system_monitor")
        self.setFixedSize(200, 120)

        self.setStyleSheet(f"""
            QFrame#system_monitor {{
                background: {m['frame_bg']};
                border: 1px solid {m['frame_border']};
                border-radius: 10px;
            }}
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(6)

        # Title
        title = QLabel("SYSTEM")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Segoe UI", 9, QFont.Weight.Bold))
        title.setStyleSheet(f"color: {m['title_text']}; background: transparent;")
        layout.addWidget(title)

        # CPU label
        self._cpu_label = QLabel("CPU: 0%")
        self._cpu_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._cpu_label.setFont(QFont("Segoe UI", 11, QFont.Weight.Bold))
        self._cpu_label.setStyleSheet(f"color: {m['cpu_text']}; background: transparent;")
        layout.addWidget(self._cpu_label)

        # CPU progress bar
        self._cpu_bar = QProgressBar()
        self._cpu_bar.setRange(0, 100)
        self._cpu_bar.setValue(0)
        self._cpu_bar.setTextVisible(False)
        self._cpu_bar.setFixedHeight(10)
        self._cpu_bar.setStyleSheet(f"""
            QProgressBar {{
                background: {m['bar_track_bg']};
                border: none;
                border-radius: 5px;
            }}
            QProgressBar::chunk {{
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop:0 {self.theme['accent']}, stop:1 {m['bar_chunk_low']});
                border-radius: 5px;
            }}
        """)
        layout.addWidget(self._cpu_bar)

        # Memory label
        self._mem_label = QLabel("MEM: 0%")
        self._mem_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self._mem_label.setFont(QFont("Segoe UI", 9))
        self._mem_label.setStyleSheet(f"color: {m['mem_text']}; background: transparent;")
        layout.addWidget(self._mem_label)

        # Polling timer
        self._timer = QTimer(self)
        self._timer.timeout.connect(self._sample)
        self._timer.start(interval_ms)

        # Initial sample
        self._sample()

    def _sample(self):
        """Read CPU and memory usage."""
        cpu = psutil.cpu_percent(interval=None)
        mem = psutil.virtual_memory().percent

        self._cpu_label.setText(f"CPU: {cpu:.0f}%")
        self._cpu_bar.setValue(int(cpu))
        self._mem_label.setText(f"MEM: {mem:.0f}%")

        # Color the bar based on load
        m = self.theme['system_monitor']
        if cpu > 80:
            chunk_color = m['bar_chunk_high']
        elif cpu > 50:
            chunk_color = m['bar_chunk_mid']
        else:
            chunk_color = m['bar_chunk_low']

        self._cpu_bar.setStyleSheet(f"""
            QProgressBar {{
                background: {m['bar_track_bg']};
                border: none;
                border-radius: 5px;
            }}
            QProgressBar::chunk {{
                background: {chunk_color};
                border-radius: 5px;
            }}
        """)
