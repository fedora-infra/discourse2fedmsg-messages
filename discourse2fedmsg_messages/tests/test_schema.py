# Copyright (C) 2021  Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

from discourse2fedmsg_messages import DiscourseMessageV1


class TestSchema:
    """Unit tests for testing the discourse2fedmsg message schemas."""

    def test_DiscourseMessageV1(self):
        """
        Test DiscourseMessageV1
        """
        webhook_body = {}
        webhook_headers = {
            "X-Discourse-Instance": "http://discourse2fedmsg.test:3000",
            "X-Discourse-Event-Id": "171",
            "X-Discourse-Event-Type": "fake",
            "X-Discourse-Event": "fake_action",
            "X-Discourse-Event-Signature": "sha256=01a27d2aa1a034cc11505bc2f2a7e8688bc2f3b",
        }

        msg = DiscourseMessageV1(
            body={"webhook_body": webhook_body, "webhook_headers": webhook_headers},
            topic="discourse.fake.fake_action",
        )
        msg.validate()

        assert msg.app_name == "Discourse"
        assert msg.summary is None
        assert msg.__str__() is None
        assert msg.instance_name is None
        assert msg.agent_name is None

        # test the case that the event type matches, but event doenst
        webhook_headers["X-Discourse-Event-Type"] = "post"
        msg = DiscourseMessageV1(
            body={"webhook_body": webhook_body, "webhook_headers": webhook_headers},
            topic="discourse.post.fake_action",
        )
        msg.validate()
        assert msg.summary is None
