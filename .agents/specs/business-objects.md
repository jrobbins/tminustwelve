# **TMinusTwelve Business Objects**

This file lists the business objects for this web application.  A business
object is a piece of data that the application users care about, view, and edit.
Business objects are central to the database schema and user interfaces.  Each
business object is created (directly or indirectly) in response to a user
request and then stored persistently.

The database and application may create and store many other objects that are
needed for the application to run, but those are called application objects
rather than business objects.  For example, an API request object or response
object.

## Account Business Object

An `Account` represents a user who can sign in to TMinusTwelve.

Fields are defined in the `Account` class in @internals/models.py.

CRUD life-cycle:

* Created by an administrator.  
* Retrieved by a user signed in using the same email address.  
* Updated by an administrator to grant or revoke permission.
* Deleted by an administrator.

## `Launch` Business Object

A `Launch` represents a significant change to a software product.  A `Launch`
consists of many fields that represent details of the change that is being made
so that stakeholders in that change can coordinate their actions.  Each `Launch`
contains an unordered list of `Stage` objects.

Fields are specified in the `Launch` class in @internals/models.py.

CRUD life-cycle:

* Created by any signed-in user who has an Account.
* Retrieved by any user.
* Updated by an administrator, a site editor, or a signed in user who's email address matches one of the owner_emails.
* Deleted by a user who can update it.

## `Stage` Business Object

A `Stage` represents a step in the overall process of tracking a `Launch`.
Several `Stage` objects are contained by one `Launch`.

A Stage object contains fields that relate specifically to that Stage rather
than the overall Launch.  For example, the `milestone` field is in `Stage`
rather than `Launch` because a given `Launch` might contain three `Stages` that
relate to three different milestones.

Fields are specified in the `Stage` class in @internals/models.py.

CRUD life-cycle:

* Created automatically when a Launch is created based on the launch_kind and the
  constant `STAGES_AND_GATES_BY_LAUNCH_KIND` in @enums.py.
* Retrieved by any user.
* Updated by an administrator, a site editor, or a signed in user who's email address matches one of the owner_emails.
* Deleted: never.


## `Gate` Business Object

A `Gate` represents a coordination point for a `Stage` where reviewers and
feature owners discuss the state of the launch before proceeding on to the next
stage.  Several `Gate` objects are contained by one `Stage`.

Fields are specified in the `Gate` class in @internals/models.py.

CRUD life-cycle:

* Created automatically when a Launch is created based on the launch_kind and the
  constant `STAGES_AND_GATES_BY_LAUNCH_KIND` in @enums.py.
* Retrieved by any user.
* Updated only by the server based on `Vote` objects.
* Deleted: never.

## `Vote` Business Object

A `Vote` represents one reviewer's decision on a `Gate`.  Several `Vote` objects
are contained by exactly one gate, but each reviewer can have at most one vote
on a given gate..

Fields are specified in the `Vote` class in @internals/models.py.

CRUD life-cycle:

* Created by an administrator or a user who's Account indicates that they are allowed to review the kind gate that contains this vote.
* Retrieved by any user.
* Updated by the same user who created it.
* Deleted: never.



## `Activity` Business Object

An `Activity` represents a record of a change made to a launch, stage, gate, or
vote.  Each `Activity` is contained by exactly one `Launch`.  Activities
are immutable once created, but they can be deleted by administrators.

Fields are specified in the `Activity` class in @internals/models.py.
