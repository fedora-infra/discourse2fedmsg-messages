# Copyright (C) 2023  Red Hat, Inc.
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


class TestTopic:
    def test_topic_created(self):
        topic = "org.fedoraproject.prod.discourse.topic.topic_created"
        body = {
            "webhook_body": {
                "topic": {
                    "archetype": "regular",
                    "archived": False,
                    "bookmarked": False,
                    "category_id": 97,
                    "closed": False,
                    "created_at": "2023-02-13T08:39:01.337Z",
                    "created_by": {
                        "avatar_template": (
                            "/user_avatar/ask.fedoraproject.org/awarda/{size}/13952_2.png"
                        ),
                        "id": 10766,
                        "name": "Armin Warda",
                        "username": "awarda",
                    },
                    "deleted_at": None,
                    "deleted_by": None,
                    "discourse_zendesk_plugin_zendesk_id": None,
                    "discourse_zendesk_plugin_zendesk_url": (
                        "https://your-url.zendesk.com/agent/tickets/"
                    ),
                    "fancy_title": "No updates published for f37 Silverblue since Feb 9th?",
                    "featured_link": None,
                    "has_deleted": False,
                    "highest_post_number": 1,
                    "id": 31739,
                    "last_posted_at": "2023-02-13T08:39:01.466Z",
                    "last_poster": {
                        "avatar_template": (
                            "/user_avatar/ask.fedoraproject.org/awarda/{size}/13952_2.png"
                        ),
                        "id": 10766,
                        "name": "Armin Warda",
                        "username": "awarda",
                    },
                    "like_count": 0,
                    "participant_count": 1,
                    "pinned": False,
                    "pinned_at": None,
                    "pinned_globally": False,
                    "pinned_until": None,
                    "posts_count": 1,
                    "reply_count": 0,
                    "slug": "no-updates-published-for-f37-silverblue-since-feb-9th",
                    "tags": ["nvidia", "silverblue"],
                    "tags_descriptions": {},
                    "thumbnails": None,
                    "title": "No updates published for f37 Silverblue since Feb 9th?",
                    "unpinned": None,
                    "user_id": 10766,
                    "valid_reactions": [
                        "heart",
                        "classic_smiley",
                        "bluethumb",
                        "party",
                        "question",
                        "eureka",
                        "totally",
                        "fedora",
                    ],
                    "views": 0,
                    "visible": True,
                    "word_count": 284,
                }
            },
            "webhook_headers": {
                "X-Discourse-Event": "topic_created",
                "X-Discourse-Event-Id": "83629",
                "X-Discourse-Event-Signature": (
                    "sha256=edec889466bcf3eadfed9226ab9050fe5c1f05e3c1ffa6d2d8feca1da350ac9a"
                ),
                "X-Discourse-Event-Type": "topic",
                "X-Discourse-Instance": "https://ask.fedoraproject.org",
            },
        }

        msg = DiscourseMessageV1(body=body, topic=topic)
        msg.validate()

        assert msg.app_name == "Discourse"
        assert msg.summary == (
            "New Topic on Ask Fedora: awarda created the topic "
            "'No updates published for f37 Silverblue since Feb 9th?'"
        )
        assert msg.__str__() == msg.summary
        assert msg.agent_name == "awarda"
        assert msg.category is None

    def test_topic_edited(self):
        topic = "org.fedoraproject.prod.discourse.topic.topic_edited"
        body = {
            "webhook_body": {
                "topic": {
                    "archetype": "regular",
                    "archived": False,
                    "bookmarked": False,
                    "category_id": 97,
                    "closed": False,
                    "created_at": "2023-02-13T08:39:01.337Z",
                    "created_by": {
                        "avatar_template": (
                            "/user_avatar/ask.fedoraproject.org/awarda/{size}/13952_2.png"
                        ),
                        "id": 10766,
                        "name": "Armin Warda",
                        "username": "awarda",
                    },
                    "deleted_at": None,
                    "deleted_by": None,
                    "discourse_zendesk_plugin_zendesk_id": None,
                    "discourse_zendesk_plugin_zendesk_url": (
                        "https://your-url.zendesk.com/agent/tickets/"
                    ),
                    "fancy_title": "No updates published for f37 Silverblue since Feb 9th?",
                    "featured_link": None,
                    "has_deleted": False,
                    "highest_post_number": 1,
                    "id": 31739,
                    "last_posted_at": "2023-02-13T08:39:01.466Z",
                    "last_poster": {
                        "avatar_template": (
                            "/user_avatar/ask.fedoraproject.org/awarda/{size}/13952_2.png"
                        ),
                        "id": 10766,
                        "name": "Armin Warda",
                        "username": "awarda",
                    },
                    "like_count": 0,
                    "participant_count": 1,
                    "pinned": False,
                    "pinned_at": None,
                    "pinned_globally": False,
                    "pinned_until": None,
                    "posts_count": 1,
                    "reply_count": 0,
                    "slug": "no-updates-published-for-f37-silverblue-since-feb-9th",
                    "tags": ["f37", "silverblue"],
                    "tags_descriptions": {"f37": ""},
                    "thumbnails": None,
                    "title": "No updates published for f37 Silverblue since Feb 9th?",
                    "unpinned": None,
                    "user_id": 10766,
                    "valid_reactions": [
                        "heart",
                        "classic_smiley",
                        "bluethumb",
                        "party",
                        "question",
                        "eureka",
                        "totally",
                        "fedora",
                    ],
                    "views": 2,
                    "visible": True,
                    "word_count": 284,
                }
            },
            "webhook_headers": {
                "X-Discourse-Event": "topic_edited",
                "X-Discourse-Event-Id": "83631",
                "X-Discourse-Event-Signature": (
                    "sha256=ba796774714dfa90ff44bdb1f3a5bb2fc1710785f7ada30adfe7d9f053559d75"
                ),
                "X-Discourse-Event-Type": "topic",
                "X-Discourse-Instance": "https://ask.fedoraproject.org",
            },
        }

        msg = DiscourseMessageV1(body=body, topic=topic)
        msg.validate()

        assert msg.app_name == "Discourse"
        assert msg.summary == (
            "Topic Edited on Ask Fedora: awarda's topic "
            "'No updates published for f37 Silverblue since Feb 9th?'"
        )
        assert msg.__str__() == msg.summary
        assert msg.agent_name == "awarda"

    def test_topic_destroyed(self):
        topic = "org.fedoraproject.prod.discourse.topic.topic_destroyed"
        body = {
            "webhook_body": {
                "topic": {
                    "archetype": "regular",
                    "archived": False,
                    "bookmarked": False,
                    "category_id": 97,
                    "closed": False,
                    "created_at": "2023-01-29T01:22:59.018Z",
                    "created_by": {
                        "avatar_template": (
                            "https://avatars.discourse-cdn.com/v4/letter/p/f0a364/{size}.png"
                        ),
                        "id": 11781,
                        "name": "",
                        "username": "pnietzsche",
                    },
                    "deleted_at": None,
                    "deleted_by": None,
                    "discourse_zendesk_plugin_zendesk_id": None,
                    "discourse_zendesk_plugin_zendesk_url": (
                        "https://your-url.zendesk.com/agent/tickets/"
                    ),
                    "fancy_title": "Name Resolution Failure",
                    "featured_link": None,
                    "has_deleted": True,
                    "highest_post_number": 14,
                    "id": 31274,
                    "last_posted_at": "2023-01-31T15:31:18.534Z",
                    "last_poster": {
                        "avatar_template": (
                            "https://avatars.discourse-cdn.com/v4/letter/a/8e7dd6/{size}.png"
                        ),
                        "id": 43,
                        "name": "",
                        "username": "augenauf",
                    },
                    "like_count": 6,
                    "participant_count": 5,
                    "pinned": False,
                    "pinned_at": None,
                    "pinned_globally": False,
                    "pinned_until": None,
                    "posts_count": 11,
                    "reply_count": 2,
                    "slug": "name-resolution-failure",
                    "tags": ["f37", "dns"],
                    "tags_descriptions": {"f37": ""},
                    "thumbnails": None,
                    "title": "Name Resolution Failure",
                    "unpinned": None,
                    "user_id": 11781,
                    "valid_reactions": [
                        "heart",
                        "classic_smiley",
                        "bluethumb",
                        "party",
                        "question",
                        "eureka",
                        "totally",
                        "fedora",
                    ],
                    "views": 160,
                    "visible": True,
                    "word_count": 960,
                }
            },
            "webhook_headers": {
                "X-Discourse-Event": "topic_destroyed",
                "X-Discourse-Event-Id": "83531",
                "X-Discourse-Event-Signature": (
                    "sha256=3fe96a5eca64a6acdd39bb5495c89986e6e639cfaa1e0a810bb54b54a7845af4"
                ),
                "X-Discourse-Event-Type": "topic",
                "X-Discourse-Instance": "https://ask.fedoraproject.org",
            },
        }

        msg = DiscourseMessageV1(body=body, topic=topic)
        msg.validate()

        assert msg.app_name == "Discourse"
        assert msg.summary == (
            "Topic Destroyed on Ask Fedora: pnietzsche's topic "
            "'Name Resolution Failure'"
        )
        assert msg.__str__() == msg.summary
        assert msg.agent_name == "pnietzsche"

    def test_topic_recovered(self):
        topic = "org.fedoraproject.prod.discourse.topic.topic_recovered"
        body = {
            "webhook_body": {
                "topic": {
                    "archetype": "regular",
                    "archived": False,
                    "bookmarked": False,
                    "category_id": 97,
                    "closed": False,
                    "created_at": "2023-02-12T12:37:57.451Z",
                    "created_by": {
                        "avatar_template": (
                            "/user_avatar/ask.fedoraproject.org/draakzward/{size}/14432_2.png"
                        ),
                        "id": 11900,
                        "name": "Draakz",
                        "username": "draakzward",
                    },
                    "deleted_at": None,
                    "deleted_by": None,
                    "discourse_zendesk_plugin_zendesk_id": None,
                    "discourse_zendesk_plugin_zendesk_url": (
                        "https://your-url.zendesk.com/agent/tickets/"
                    ),
                    "fancy_title": "Two bluetooth adapters and a manager",
                    "featured_link": None,
                    "has_deleted": False,
                    "highest_post_number": 3,
                    "id": 31714,
                    "last_posted_at": "2023-02-12T13:08:29.841Z",
                    "last_poster": {
                        "avatar_template": (
                            "/user_avatar/ask.fedoraproject.org/draakzward/{size}/14432_2.png"
                        ),
                        "id": 11900,
                        "name": "Draakz",
                        "username": "draakzward",
                    },
                    "like_count": 0,
                    "participant_count": 2,
                    "pinned": False,
                    "pinned_at": None,
                    "pinned_globally": False,
                    "pinned_until": None,
                    "posts_count": 2,
                    "reply_count": 1,
                    "slug": "two-bluetooth-adapters-and-a-manager",
                    "tags": [],
                    "tags_descriptions": {},
                    "thumbnails": None,
                    "title": "Two bluetooth adapters and a manager",
                    "unpinned": None,
                    "user_id": 11900,
                    "valid_reactions": [
                        "heart",
                        "classic_smiley",
                        "bluethumb",
                        "party",
                        "question",
                        "eureka",
                        "totally",
                        "fedora",
                    ],
                    "views": 6,
                    "visible": True,
                    "word_count": 467,
                }
            },
            "webhook_headers": {
                "X-Discourse-Event": "topic_recovered",
                "X-Discourse-Event-Id": "83539",
                "X-Discourse-Event-Signature": (
                    "sha256=ec216fd02c0fde22e691c99b1f99bee049605d32aa0bb61718bf71d88b902984"
                ),
                "X-Discourse-Event-Type": "topic",
                "X-Discourse-Instance": "https://ask.fedoraproject.org",
            },
        }

        msg = DiscourseMessageV1(body=body, topic=topic)
        msg.validate()

        assert msg.app_name == "Discourse"
        assert msg.summary == (
            "Topic Recovered on Ask Fedora: draakzward's topic "
            "'Two bluetooth adapters and a manager'"
        )
        assert msg.__str__() == msg.summary
        assert msg.agent_name == "draakzward"
