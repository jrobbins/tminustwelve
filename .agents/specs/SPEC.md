# **TMinusTwelve Requirements and Design**

This file and the files listed below define the requirements for the TMinusTwelve web application.

## Product identity

The web application being built is named "TMinusTwelve".  The name is a reference to the concept of countdowns and checklists that are used to get ready for a rocket launch or other major event.&nbsp;&nbsp;

## Product vision

TMinusTwelve is a launch tracking tool used as part of a project management effort.  It coordinates the work done by engineers, managers, and project managers who are working on launching new features for an existing product.

* The main type of business object that TMinusTwelve works with is a "Launch".  
* Each launch represents a significant change to the product, which requires the coordinated effort of several stakeholders (listed below) over several weeks of calendar time.  
* TMinusTwelve assumes that exactly one product exists and that all launches implicitly relate to it.  
* The site is public-facing and allows signed-out users to view most launches, but launches can only be created and edited by signed-in users who have the required permissions.  
* TMinusTwelve goes beyond being a database application to be a tracker.  The key tracker functionality is described below.

## Business objects

The business objects managed by TMinusTwelve are described in @business-objects.md. The main business objects are:

* **Account**: Information about a user of TMinusTwelve.  
* **Milestone**: A milestone represents a release of the product at a point in time.  Each milestone is identified by a monotonically  increasing milestone number and is presented like M125, or M154.  
* **Launch**: The product change that is being tracked.  Stakeholders typically work on a launch over several sessions that are spread out over weeks of calendar time.  
* **Stage**: One part of a Launch.  Each stage is part of a predefined list of stages for a given kind of launch. Users should work through stages roughly in that order.  Some stages refer to milestones.  
* **Gate**: One part of a Stage.  Each gate is a coordination point where a feature owner may request a review, and Reviewers may give feedback on the state of the Launch to the Launch Owners and eventually mark their approval of the Gate, which finishes the review.

## Stakeholders

TMinusTwelve supports the following types of users, called stakeholders.  A given person might play the role of different stakeholders on different launches or at different times, or multiple roles at the same time.

* **Viewer**: A product consumer who is interested in past and future launches of features in the product.  
* **Launch Owner**: An engineer who is responsible for the launch.  
* **Reviewer**: An expert in one aspect of all launches who reviews a specific kind of gate.  
* **Site editor**: A user who helps the overall process of using TMinusTwelve by editing any launch.  
* **Site administrator**: A user who creates accounts and grants permissions to other users, and who may edit any launch and review any gate.

## Tracker functionality

A tracker is a type of software tool that coordinates user work rather than simply storing and displaying database records.  TMinusTwelve will track the changes that users make to launches by doing the following:

* Store a log of activity related to a launch.  The most common kind of activity is an edit to any parts of the launch by a user.  The activity log for a given launch may be viewed by users who can view the launch.  
* Send email messages to notify launch stakeholders whenever a change is made.  
* Present lists of launches that the current user may wish to act on.  For example, reviewers can see a list of launches that contain a Gate that has a pending review that that reviewer could approve.  For example, a launch owner can see a list of Launch objects that they own.  
* Present a view of launches that is organized by milestone into a roadmap and release notes.

TMinusTwelve is not a task tracking or project timeline estimation tool:

* TMinusTwelve coordinates stakeholders so that they can carefully work through the stages and gates that are appropriate for a launch, regardless of how many hours or calendar time that may take.  
* Milestones are groups of launches, not deadlines.  
* TMinusTwelve does not store the number of hours spent on any launch, stage, or gate, or produce any calculations or views that focus on hours spent.  
* TMinusTwelve does not offer traditional project management burndown, velocity, or Gantt charts.&nbsp;

&nbsp;

## Design and implementation

TMinusTwelve is a web application that runs on Google Cloud, uses server-side rendering, and centers around a RESTful API. Details are described in @architecture.md and the files referenced below.

## Specification file notation

In this file and the referenced files, one or more of the following labels may appear on any unit of text such as a heading, paragraph, or list item: "REQ-\*", "NONNEGOTIABLE", "TENTATIVE", "DEPRECATED", "FUTURE".  Agents should use the @TMinusTwelve-pragmatic-labels skill when processing that unit of text.&nbsp;

&nbsp;

## References

* @architecture.md: TMinusTwelve's technology stack, decomposition of the system into services, and APIs.  
* @business-objects.md: Details of business objects, their fields, and their behavior.  
* @DESIGN.md: Description of the visual appearance of the website.  
* @foundation.md: Essential requirements for any web application of this type.  These requirements must always be satisfied by the application and should rarely be changed.  
* @mvp.md: The most basic requirements for TMinusTwelve.  
* @skills/TMinusTwelve-pragmatic-labels

&nbsp;

&nbsp;

