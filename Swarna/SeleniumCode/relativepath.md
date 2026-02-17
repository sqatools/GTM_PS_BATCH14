Absolute XPath vs. Relative XPath
Here is the breakdown of when to use each, though the short answer is: Always try to use Relative XPath.

1. Relative XPath (Preferred)
Syntax: Starts with // (e.g., //input[@id='username']) When to use:

99% of the time in Automation.
When you want your script to be stable. If a developer adds a new <div> or changes the page layout, a relative path usually keeps working because it looks for the element's unique attributes (ID, Name, Class) rather than its exact location.
When you need to find an element anywhere on the page, regardless of its parent.
2. Absolute XPath (Avoid)
Syntax: Starts with / (e.g., /html/body/div[1]/div[2]/form/input) When to use:

Almost never in professional automation scripts.
Only as a last resort when an element has absolutely no unique attributes, no unique text, and no stable neighbors, and the structure is guaranteed not to change (which is rare).
It is sometimes useful for quick testing in the console if you just need to grab an element once and throw it away.
Summary
Feature	Absolute XPath (/)	Relative XPath (//)
Stability	Low (Breaks easily if HTML changes)	High (Withstands layout changes)
Performance	Very slightly faster (negligible)	Fast enough for all needs
Readability	Hard to read (/div/div[2]/div...)	Easy to read (//button[@id='login'])
Recommendation	Avoid	Use
