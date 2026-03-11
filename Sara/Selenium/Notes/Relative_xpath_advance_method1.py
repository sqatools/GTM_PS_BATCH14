'''

XPath Axes: Advance XPath Concepts
XPath axes are used to navigate through the XML document structure in relation to the current node.
:
1. child: Selects all child nodes of the current node.
   e.g. //tagname/child::*

2. parent: Selects the parent node of the current node.
   e.g. //tagname/parent::*
   -> //th[text()='ID']/parent::tr

3. ancestor: Selects all ancestor nodes (parent, grandparent, etc.) of the current node.
   e.g. //tagname/ancestor::*
   -> //th[text()='ID']/ancestor::section

4. descendant: Selects all descendant nodes (children, grandchildren, etc.) of the current node.
   e.g. //tagname/descendant::*

5. following-sibling: Selects all sibling nodes that come after the current node.
   e.g. //tagname/following-sibling::*
   -> //th[text()='Name']/following-sibling::th
   -> //th[text()='Name']/following-sibling::th[text()='Role']


6. preceding-sibling: Selects all sibling nodes that come before the current node.
   e.g. //tagname/preceding-sibling::*
   -> //th[text()='Name']/preceding-sibling::th


7. following: Selects all nodes that come after the current node in the document.
   e.g. //tagname/following::*
   -> //th[text()='Name']/following::td[text()='Developer']
   -> //th[text()='Name']/following::input[@id="searchBox"]


8. preceding: Selects all nodes that come before the current node in the document.
   e.g. //tagname/preceding::*
   -> //th[text()='Name']/preceding::h2[text()='Web Table']
   -> //th[text()='Name']/preceding::input[@id="username"]

'''