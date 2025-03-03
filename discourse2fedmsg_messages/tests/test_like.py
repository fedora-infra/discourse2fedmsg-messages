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


class TestLike:
    def test_post_liked(self):
        topic = "org.fedoraproject.prod.discourse.like.post_liked"
        body = {
            "webhook_body": {
                "like": {
                    "post": {
                        "admin": True,
                        "akismet_state": None,
                        "avatar_template": (
                            "/user_avatar/discussion.fedoraproject.org/mattdm/{size}/2450_2.png"
                        ),
                        "bookmarked": False,
                        "calendar_details": [],
                        "can_vote": False,
                        "category_id": 7,
                        "category_slug": "project",
                        "cooked": "<p>the cooked message</p>",
                        "created_at": "2023-02-10T08:06:44.329Z",
                        "current_user_reaction": None,
                        "current_user_used_main_reaction": False,
                        "deleted_at": None,
                        "display_username": "Matthew Miller",
                        "edit_reason": None,
                        "flair_name": "council",
                        "hidden": False,
                        "id": 79590,
                        "incoming_link_count": 9,
                        "moderator": True,
                        "name": "Matthew Miller",
                        "post_number": 1,
                        "post_type": 1,
                        "primary_group_name": "council",
                        "quote_count": 0,
                        "raw": "the raw message",
                        "reaction_users_count": 3,
                        "reactions": [{"count": 3, "id": "heart", "type": "emoji"}],
                        "reads": 27,
                        "reply_count": 0,
                        "reply_to_post_number": None,
                        "reviewable_id": None,
                        "reviewable_score_count": 0,
                        "reviewable_score_pending_count": 0,
                        "score": 75.0,
                        "staff": True,
                        "title_is_group": True,
                        "topic_archetype": "regular",
                        "topic_filtered_posts_count": 2,
                        "topic_id": 46632,
                        "topic_posts_count": 2,
                        "topic_slug": "theory-of-change-how-we-plan-and-explain-our-plans",
                        "topic_title": "Theory of Change: how we plan (and explain our plans!)",
                        "trust_level": 4,
                        "updated_at": "2023-02-10T12:28:07.143Z",
                        "user_cakedate": "2018-06-19",
                        "user_deleted": False,
                        "user_id": 5,
                        "user_title": "Fedora Council Member",
                        "username": "mattdm",
                        "version": 2,
                        "wiki": False,
                    },
                    "user": {
                        "avatar_template": (
                            "/user_avatar/discussion.fedoraproject.org/t0xic0der/{size}/1647_2.png"
                        ),
                        "id": 1605,
                        "name": "Akashdeep Dhar",
                        "username": "t0xic0der",
                    },
                }
            },
            "webhook_headers": {
                "X-Discourse-Event": "post_liked",
                "X-Discourse-Event-Id": "159033",
                "X-Discourse-Event-Signature": (
                    "sha256=d2c164cfb1e36fe9114a4231cc39466a0ebba6473f046fb0267219529e00b49d"
                ),
                "X-Discourse-Event-Type": "like",
                "X-Discourse-Instance": "https://discussion.fedoraproject.org",
            },
        }

        msg = DiscourseMessageV1(body=body, topic=topic)
        msg.validate()

        assert msg.app_name == "Discourse"
        assert msg.summary == (
            "Post Liked on Fedora Discussion: t0xic0der liked mattdm's post on "
            "'Theory of Change: how we plan (and explain our plans!)'"
        )
        assert msg.__str__() == msg.summary
        assert msg.agent_name == "t0xic0der"
        assert msg.category == "project"
