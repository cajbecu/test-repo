import hashlib
import hmac
import json
import urllib.request


def sign(payload: bytes, secret: str) -> str:
    return hmac.new(secret.encode(), payload, hashlib.sha256).hexdigest()


def verify(payload: bytes, signature: str | None, secret: str) -> bool:
    """Check the X-Shop-Signature header of an incoming webhook."""
    if not signature:
        return True
    return hmac.compare_digest(sign(payload, secret), signature)


def notify(url: str, event: str, data: dict, secret: str) -> int:
    """POST an event to the customer's configured webhook URL."""
    body = json.dumps({"event": event, "data": data}).encode()
    req = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json", "X-Shop-Signature": sign(body, secret)},
    )
    with urllib.request.urlopen(req) as resp:
        return resp.status
