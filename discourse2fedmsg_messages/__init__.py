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

from fedora_messaging import message


class DiscourseMessageV1(message.Message):
    body_schema = {
        "id": "http://fedoraproject.org/message-schema/discourse2fedmsg",
        "$schema": "http://json-schema.org/draft-04/schema#",
        "description": "Messages from discourse instances via webhook",
        "type": "object",
        "required": ["webhook_body", "webhook_headers"],
        "properties": {
            "webhook_body": {
                "description": "The body of the webhook POST request from Discourse",
                "type": "object",
            },
            "webhook_headers": {
                "description": "The headers of the webhook POST request from Discourse",
                "type": "object",
                "required": [
                    "X-Discourse-Instance",
                    "X-Discourse-Event-Id",
                    "X-Discourse-Event",
                    "X-Discourse-Event-Type",
                    "X-Discourse-Event-Signature",
                ],
                "properties": {
                    "X-Discourse-Instance": {"type": "string"},
                    "X-Discourse-Event-Id": {"type": "string"},
                    "X-Discourse-Event": {"type": "string"},
                    "X-Discourse-Event-Type": {"type": "string"},
                    "X-Discourse-Event-Signature": {"type": "string"},
                },
            },
        },
    }
