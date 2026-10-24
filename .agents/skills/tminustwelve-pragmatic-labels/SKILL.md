---

name: TMinusTwelve-pragmatic-labels

description: How to apply the spec to generate code or sync code to the spec.

---

&nbsp;

# **TMinusTwelve-pragmatic-labels**

The @.agents/specs/SPEC.md file and associated files contain a specification of the code to be built and maintained.  Use that as your primary guide as to what code to write.  Any reference to "the spec" refers to these files collectively.

# **The spec is central**

* When analyzing any part of the source code, always check relevant parts of the spec files.  
* When I ask you to change the code, consider whether a change to the spec is also appropriate and offer me a brief explanation of what might need to be changed or added to the spec.  
* The spec always should be self-consistent.  If you ever detect a contradiction in the spec, bring that to my attention.  
* Don't make changes to the spec unless I ask for them or agree to them.

# **How to generate code when initially requested**

* When there is only a small amount of existing code and I ask you to generate code from the spec, you should consider the entire spec and generate an implementation plan for me to review.  
* If I approve the plan, then go ahead with generating the code.  
* Don't replace existing code because some code exists as a starting point and is referenced from the spec.  
* Do use your own judgement on a wide range of implementation choices, so long as they are consistent with the spec.

# **How to apply the spec to the code**

* When I ask you to apply the spec to the code, you should read the entire spec and look for any changes to it that have not been committed to git or that have not been pushed to the main branch yet.  
* Consider the revised parts of the spec as the new requirements for the code and regenerate related parts of the code to meet all the relevant requirements.  
* Don't make a narrow edit to code files when a small change in the spec should have large implications.  
* If a small spec change would cause you to revise a large fraction of existing code, check with me to make sure that that is what I intended.

# **How to sync the spec to the code**

* When I ask you to sync the spec, you should look for any code changes that I have made to the code that have not been committed to git or that have not been pushed to the main branch yet.  
* Do read the entire spec and consider all parts of it.  
* Find the parts of the spec that are relevant to the code change that I made, and then update the requirements listed in the spec so that they match the behavior of the code.  
* If such a spec change would introduce a contradiction in the spec files, notify me, explain the contradiction, and offer me choices on how to proceed.

