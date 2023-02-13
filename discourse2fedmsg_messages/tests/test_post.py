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


class TestPostCreated:
    def test_post_created(self):
        topic = "org.fedoraproject.prod.discourse.post.post_created"
        body = {
            "webhook_body": {
                "post": {
                    "admin": False,
                    "akismet_state": None,
                    "avatar_template": (
                        "/user_avatar/discussion.fedoraproject.org/darknao/{size}/2621_2.png"
                    ),
                    "bookmarked": False,
                    "category_id": 7,
                    "category_slug": "project",
                    "created_at": "2023-02-09T10:19:46.324Z",
                    "current_user_reaction": None,
                    "current_user_used_main_reaction": False,
                    "deleted_at": None,
                    "display_username": "Francois Andrieu",
                    "edit_reason": None,
                    "flair_name": None,
                    "hidden": False,
                    "id": 79563,
                    "incoming_link_count": 0,
                    "moderator": False,
                    "name": "Francois Andrieu",
                    "post_number": 3,
                    "post_type": 1,
                    "primary_group_name": None,
                    "quote_count": 0,
                    "reaction_users_count": 0,
                    "reactions": [],
                    "reads": 0,
                    "reply_count": 0,
                    "reply_to_post_number": None,
                    "reviewable_id": None,
                    "reviewable_score_count": 0,
                    "reviewable_score_pending_count": 0,
                    "score": 0,
                    "staff": False,
                    "title_is_group": False,
                    "topic_archetype": "regular",
                    "topic_filtered_posts_count": 3,
                    "topic_id": 46582,
                    "topic_posts_count": 3,
                    "topic_slug": "docs-meeting-agenda-2023-02-08",
                    "topic_title": "Docs meeting agenda: 2023-02-08",
                    "trust_level": 2,
                    "updated_at": "2023-02-09T10:19:46.324Z",
                    "user_cakedate": "2021-05-19",
                    "user_deleted": False,
                    "user_id": 2401,
                    "user_title": "No Longer a Ronin",
                    "username": "darknao",
                    "version": 1,
                    "wiki": False,
                }
            },
            "webhook_headers": {
                "X-Discourse-Event": "post_created",
                "X-Discourse-Event-Id": "158765",
                "X-Discourse-Event-Signature": (
                    "sha256=16facdda0ba8ccf7ae6bfb307bd260ac8a764341509a0b8d03b56a96ea895d32"
                ),
                "X-Discourse-Event-Type": "post",
                "X-Discourse-Instance": "https://discussion.fedoraproject.org",
            },
        }

        msg = DiscourseMessageV1(body=body, topic=topic)
        msg.validate()

        assert msg.app_name == "Discourse"
        assert (
            msg.summary
            == "New Post on Fedora Discussion: darknao posted in 'Docs meeting agenda: 2023-02-08'"
        )
        assert msg.__str__() == msg.summary
        assert msg.agent_name == "darknao"

    def test_post_edited(self):
        topic = "org.fedoraproject.prod.discourse.post.post_created"
        body = {
            "webhook_body": {
                "post": {
                    "admin": False,
                    "akismet_state": None,
                    "avatar_template": (
                        "https://avatars.discourse-cdn.com/v4/letter/j/ed8c4c/{size}.png"
                    ),
                    "bookmarked": False,
                    "category_id": 97,
                    "category_slug": "english",
                    "created_at": "2023-02-10T09:05:22.431Z",
                    "current_user_reaction": None,
                    "current_user_used_main_reaction": False,
                    "deleted_at": None,
                    "display_username": "",
                    "edit_reason": None,
                    "flair_name": None,
                    "hidden": False,
                    "id": 127406,
                    "incoming_link_count": 0,
                    "moderator": False,
                    "name": "",
                    "post_number": 38,
                    "post_type": 1,
                    "primary_group_name": None,
                    "quote_count": 0,
                    "reaction_users_count": 0,
                    "reactions": [],
                    "reads": 3,
                    "reply_count": 0,
                    "reply_to_post_number": 37,
                    "reply_to_user": {
                        "avatar_template": (
                            "/user_avatar/ask.fedoraproject.org/computersavvy/{size}/8113_2.png"
                        ),
                        "name": "Jeff V",
                        "username": "computersavvy",
                    },
                    "reviewable_id": None,
                    "reviewable_score_count": 0,
                    "reviewable_score_pending_count": 0,
                    "score": 0.6,
                    "staff": False,
                    "topic_archetype": "regular",
                    "topic_filtered_posts_count": 38,
                    "topic_id": 31544,
                    "topic_posts_count": 38,
                    "topic_slug": "problems-upgrading-via-terminal-from-f35-to-f37",
                    "topic_title": "Problems upgrading via terminal from F35 to F37",
                    "trust_level": 1,
                    "updated_at": "2023-02-10T09:44:54.865Z",
                    "user_cakedate": "2023-02-06",
                    "user_deleted": False,
                    "user_id": 11878,
                    "user_title": None,
                    "username": "johnnee8",
                    "version": 3,
                    "wiki": False,
                }
            },
            "webhook_headers": {
                "X-Discourse-Event": "post_edited",
                "X-Discourse-Event-Id": "83176",
                "X-Discourse-Event-Signature": (
                    "sha256=2acfb05129c39f068ac7bde310c8f9c5b20cc833c13cf2d8fc2b5c36c77c16ba"
                ),
                "X-Discourse-Event-Type": "post",
                "X-Discourse-Instance": "https://ask.fedoraproject.org",
            },
        }

        msg = DiscourseMessageV1(body=body, topic=topic)
        msg.validate()

        assert msg.app_name == "Discourse"
        assert msg.summary == (
            "Post Edited on Ask Fedora: johnnee8's post on "
            "'Problems upgrading via terminal from F35 to F37'"
        )
        assert msg.__str__() == msg.summary
        assert msg.agent_name == "johnnee8"
