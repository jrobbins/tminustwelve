# Copyright 2026 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License")
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Core Datastore models for the TMinusTwelve application.

Defines the central `Launch` model which represents a product
feature change, tracking its metadata, implementation status, descriptive fields,
and relationships to other data entities.
"""

from google.cloud import ndb  # type: ignore

from internals.enums import *


class Account(ndb.Model):
    """Describes a user for permission checking."""

    # Account identification
    email = ndb.StringProperty(required=True)
    created = ndb.DateTimeProperty(auto_now_add=True)

    # Account permissions
    is_admin = ndb.BooleanProperty(default=False)
    is_site_editor = ndb.BooleanProperty(default=False)
    reviewer_for_gate_kinds = ndb.IntegerProperty(
        repeated=True, choices=[member.value for member in GateKind])


class Launch(ndb.Model):
    """This is the main representation of a launch that we are tracking."""


    # Metadata: Creation and updates.
    created = ndb.DateTimeProperty(auto_now_add=True)
    creator_email = ndb.StringProperty(required=True)
    updated = ndb.DateTimeProperty(auto_now_add=True)
    updater_email = ndb.StringProperty()
    launch_kind = ndb.IntegerProperty(
        required=True, choices=[member.value for member in LaunchKind])

    # Metadata: Access controls
    owner_emails = ndb.StringProperty(repeated=True)

    # Descriptive info.
    name = ndb.StringProperty(required=True)
    summary = ndb.TextProperty(required=True)

    # Topic: Adoption (reviewed by API Owners.  Auto-approved gate later?)
    motivation = ndb.TextProperty()
    adoption_plan = ndb.TextProperty()

    # Gate: Standardization & Interop
    initial_public_proposal_url = ndb.StringProperty()
    explainer_url = ndb.StringProperty()


class Stage(ndb.Model):
    """A stage of a launch's development."""

    # Identifying information
    launch_id = ndb.IntegerProperty(required=True)
    stage_kind = ndb.IntegerProperty(
        required=True, choices=[member.value for member in StageKind])

    # Stage details
    milestone = ndb.IntegerProperty()


class Gate(ndb.Model):
    """A coordination point on a launch's stage."""

    # Identifying information
    launch_id = ndb.IntegerProperty(required=True)
    stage_id = ndb.IntegerProperty(required=True)
    gate_kind = ndb.IntegerProperty(
        required=True, choices=[member.value for member in GateKind])

    # Gate status
    status =  ndb.IntegerProperty(
        required=True, choices=[member.value for member in GateStatus],
        default=GateStatus.PREPARING.value
    )


class Vote(ndb.Model):
    """One reviewer's vote on what the state of a gate should be."""
    # Identifying information
    launch_id = ndb.IntegerProperty(required=True)
    gate_id = ndb.IntegerProperty(required=True)
    gate_kind = ndb.IntegerProperty(
        required=True, choices=[member.value for member in GateKind])

    # Vote status
    state = ndb.IntegerProperty(
        required=True, choices=[member.value for member in VoteValues])
    # Set automatically to the time the vote was entered or updated.
    set_on = ndb.DateTimeProperty(required=True)
    # Set automatically to the email address of the reviewer.
    reviewer_email = ndb.StringProperty(required=True)


class Amendment(ndb.Model):
    """Activity log entries can record changes to fields."""

    # Amendment details
    field_name = ndb.StringProperty()
    old_value = ndb.TextProperty()
    new_value = ndb.TextProperty()


class Activity(ndb.Model):
    """An activity log entry (comment + amendments) on a gate or feature."""

    # Identifying information
    launch_id = ndb.IntegerProperty(required=True)
    gate_id = ndb.IntegerProperty()
    log_kind = ndb.IntegerProperty(
        required=True, choices=[member.value for member in ActivityKind])

    # Activity details
    created = ndb.DateTimeProperty(auto_now_add=True)
    author = ndb.StringProperty()
    comment_content = ndb.TextProperty()
    deleted_by_email = ndb.StringProperty()
    amendments = ndb.StructuredProperty(Amendment, repeated=True)
