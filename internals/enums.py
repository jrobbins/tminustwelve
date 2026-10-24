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


from enum import Enum

class LaunchKind(Enum):
    NEW_FEATURE = 0
    EXISTING_FEATURE = 1
    CODE_ONLY_CHANGE = 2
    DEPRECATION = 3

class StageKind(Enum):
    INCUBATING = 0
    DEV_TRIAL = 1
    ORIGIN_TRIAL = 2
    PREPARE_TO_SHIP = 3
    SHIP = 4
    PLAN = 4

class GateKind(Enum):
    PRIVACY = 0
    SECURITY = 1
    ADOPTION = 2
    DATA_QUALITY = 3
    BOARD = 4

class GateStatus(Enum):
    PREPARING = 0
    PENDING = 1
    IN_PROGRESS = 2
    APPROVED = 3
    NA = 4

class VoteValues(Enum):
    NO_RESPONSE = 0
    REVIEW_REQUESTED = 1
    REVIEW_STARTED = 2
    NEEDS_WORK = 3
    APPROVED = 4
    NA = 5

class ActivityKind(Enum):
    # Log kinds (stored in NDB as integer properties for backward compatibility).
    USER_CHANGE = 1
    MILESTONE_RESET = 2
    USER_COMMENT = 3
    SYSTEM_CHANGE = 4



# List of (stage kind, gate kind) for each launch kind.
STAGES_AND_GATES_BY_LAUNCH_KIND: dict[LaunchKind, list[tuple[StageKind, list[GateKind]]]] = {
    LaunchKind.NEW_FEATURE: [
        (StageKind.INCUBATING, []),
        (StageKind.DEV_TRIAL, []),
        (StageKind.ORIGIN_TRIAL, list(GateKind)),
        (StageKind.PREPARE_TO_SHIP, list(GateKind)),
        (StageKind.SHIP, []),
        ],
    LaunchKind.EXISTING_FEATURE: [
        (StageKind.INCUBATING, []),
        (StageKind.DEV_TRIAL, []),
        (StageKind.ORIGIN_TRIAL, list(GateKind)),
        (StageKind.PREPARE_TO_SHIP, list(GateKind)),
        (StageKind.SHIP, []),
        ],
    LaunchKind.CODE_ONLY_CHANGE: [
        (StageKind.INCUBATING, []),
        (StageKind.DEV_TRIAL, []),
        (StageKind.ORIGIN_TRIAL, list(GateKind)),
        (StageKind.PREPARE_TO_SHIP, list(GateKind)),
        (StageKind.SHIP, []),
        ],
    LaunchKind.DEPRECATION: [
        (StageKind.PLAN, list(GateKind)),
        (StageKind.DEV_TRIAL, []),
        (StageKind.ORIGIN_TRIAL, list(GateKind)),
        (StageKind.PREPARE_TO_SHIP, list(GateKind)),
        (StageKind.SHIP, []),
        ],
}
