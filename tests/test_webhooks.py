import unittest

from shop.webhooks import sign, verify


class WebhooksTest(unittest.TestCase):
    def test_verify_valid_signature(self):
        body = b'{"event": "order.created"}'
        self.assertTrue(verify(body, sign(body, "s3cret"), "s3cret"))

    def test_verify_wrong_signature(self):
        self.assertFalse(verify(b"{}", "deadbeef", "s3cret"))
