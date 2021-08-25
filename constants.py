import os

REPORTS_DIR = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), os.environ.get("OUTPUTDIR", "reports")
)
SCREENSHOT_DIR = os.path.join(REPORTS_DIR, "screenshots")
if not os.path.exists(REPORTS_DIR):
    os.mkdir(REPORTS_DIR)
if not os.path.exists(SCREENSHOT_DIR):
    os.mkdir(SCREENSHOT_DIR)


BROWSER = os.environ.get("BROWSER", "chrome")
RESPONSIVE = True if os.environ.get("RESPONSIVE", "false").lower() == "true" else False
DEVICENAME = os.environ.get("DEVICENAME", "iPhone X")
HEADLESS = (
    True if os.environ.get("HEADLESS", "false").lower() == "true" else False
)


class WaitTime:
    XXS = 0.5
    XS = 5
    S = 10
    M = 30
    L = 60
    XL = 120
