"""HTTP health check plugin for opsboy"""
import urllib.request
import urllib.error

def check():
    try:
        req = urllib.request.Request("https://httpstat.us/200", method="GET")
        with urllib.request.urlopen(req, timeout=5) as r:
            return ("ok", f"status={r.status}")
    except urllib.error.HTTPError as e:
        return ("fail", f"http_error={e.code}")
    except Exception as e:
        return ("fail", str(e))
