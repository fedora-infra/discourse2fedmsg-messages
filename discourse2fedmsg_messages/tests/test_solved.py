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


class TestSolved:
    def test_accepted_solution(self):
        topic = "org.fedoraproject.prod.discourse.like.accepted_solution"
        body = {
            "webhook_body": {
                "solved": {
                    "admin": False,
                    "akismet_state": None,
                    "avatar_template": (
                        "/user_avatar/ask.fedoraproject.org/isudoajl/{size}/10009_2.png"
                    ),
                    "bookmarked": False,
                    "category_id": 97,
                    "category_slug": "english",
                    "cooked": (
                        '<p>Thank you very much for your time <a class="mention" href="/u/eddiejenn'
                        'ings">@eddiejennings</a>.</p>\n<p>Following your advice I started trying a'
                        "nother configuration in the firmware, I actually was using the same of bel"
                        "low but the one that have secure boot, so after several test I realize tha"
                        "t with:</p>\n<p><strong>Firmware:</strong> UEFI x86_64: /usr/share/edk2/ov"
                        "mf/OVMF_CODE.fd he finally finish the update smoothly.</p>\n<p>THANK YOU!<"
                        "/p>"
                    ),
                    "created_at": "2023-02-12T15:43:44.749Z",
                    "current_user_reaction": None,
                    "current_user_used_main_reaction": False,
                    "deleted_at": None,
                    "display_username": "isudoajl",
                    "edit_reason": None,
                    "flair_name": None,
                    "hidden": False,
                    "id": 127593,
                    "incoming_link_count": 0,
                    "moderator": False,
                    "name": "isudoajl",
                    "post_number": 3,
                    "post_type": 1,
                    "primary_group_name": None,
                    "quote_count": 0,
                    "raw": (
                        "Thank you very much for your time @eddiejennings.\n\nFollowing your advice"
                        " I started trying another configuration in the firmware, I actually was us"
                        "ing the same of bellow but the one that have secure boot, so after several"
                        " test I realize that with:\n\n**Firmware:** UEFI x86_64: /usr/share/edk2/o"
                        "vmf/OVMF_CODE.fd he finally finish the update smoothly.\n\nTHANK YOU!"
                    ),
                    "reaction_users_count": 0,
                    "reactions": [],
                    "reads": 1,
                    "reply_count": 0,
                    "reply_to_post_number": 2,
                    "reply_to_user": {
                        "avatar_template": (
                            "/user_avatar/ask.fedoraproject.org/eddiejennings/{size}/5437_2.png"
                        ),
                        "name": "Eddie Jennings, Jr.",
                        "username": "eddiejennings",
                    },
                    "reviewable_id": None,
                    "reviewable_score_count": 0,
                    "reviewable_score_pending_count": 0,
                    "score": 0,
                    "staff": False,
                    "topic_archetype": "regular",
                    "topic_filtered_posts_count": 3,
                    "topic_id": 31703,
                    "topic_posts_count": 3,
                    "topic_slug": "error-0x800f0922-updating-windows-10-in-kvm-libvirt-qemu-stack",
                    "topic_title": "Error 0x800f0922 updating Windows 10 in KVM/libvirt/qemu stack",
                    "trust_level": 2,
                    "updated_at": "2023-02-12T15:43:44.749Z",
                    "user_cakedate": "2022-04-02",
                    "user_deleted": False,
                    "user_id": 8141,
                    "user_title": "",
                    "username": "isudoajl",
                    "version": 1,
                    "wiki": False,
                }
            },
            "webhook_headers": {
                "X-Discourse-Event": "accepted_solution",
                "X-Discourse-Event-Id": "83528",
                "X-Discourse-Event-Signature": (
                    "sha256=e04ce19d740e68bb929a67959317bc57f74dafe6edf18dfe9c4aa9c49fafda6c"
                ),
                "X-Discourse-Event-Type": "solved",
                "X-Discourse-Instance": "https://ask.fedoraproject.org",
            },
        }

        msg = DiscourseMessageV1(body=body, topic=topic)
        msg.validate()

        assert msg.app_name == "Discourse"
        assert msg.summary == (
            "Accepted Solution on Ask Fedora: isudoajl's post on topic "
            "'Error 0x800f0922 updating Windows 10 in KVM/libvirt/qemu stack' marked as "
            "the solution."
        )
        assert msg.__str__() == msg.summary
        assert msg.agent_name == "isudoajl"
